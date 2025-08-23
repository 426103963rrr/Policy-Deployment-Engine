import os
import json
import shutil
import requests
from collections import defaultdict
import customtkinter as ctk
from tkinter import messagebox

# ---------- CONFIG ----------
REPO_OWNER = "hashicorp"
REPO_NAME = "terraform-provider-google"
BRANCH = "main"
BASE_PATH = "google/services"
GITHUB_API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/git/trees/{BRANCH}?recursive=1"
CACHE_FILE = "gcp_service_cache.json"
STATE_FILE = "user_state.json"

TEMPLATE_DIR = os.path.join("templates", "gcp")
TEMPLATE_FILES_TF = ["c.tf", "config.tf", "nc.tf"]
TEMPLATE_POLICY = "policy.rego"
TEMPLATE_VARS = "vars.rego"

INPUT_ROOT = os.path.join("inputs", "gcp")
POLICY_ROOT = os.path.join("policies", "gcp")


# ---------- UTILITIES ----------
def ensure_jsonable_service_map(d):
    """Convert defaultdict to plain dict of sorted lists for JSON safety."""
    return {k: sorted(list(v)) for k, v in d.items()}


def get_subfolder_from_resource(resource_name: str) -> str:
    """
    Match the second script logic:
    subfolder = everything after 'google_' and the next part.
    Example: google_compute_instance_template -> 'instance_template'
    """
    if not resource_name.startswith("google_"):
        return resource_name
    parts = resource_name.split("_", 2)  # ['google', '<prefix>', '<rest>']
    return parts[2] if len(parts) >= 3 else resource_name


# ---------- DATA LOADING ----------
def fetch_gcp_services_from_github():
    # Load allowed resources from local list
    try:
        with open("gcp_services.txt", encoding="utf-8") as f:
            txt_resources = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        messagebox.showerror("Missing file", "gcp_services.txt not found.")
        return {}

    normalized_txt_resources = {}
    for res in txt_resources:
        norm_res = res[len("google_"):] if res.startswith("google_") else res
        normalized_txt_resources[norm_res] = res

    # Optional: use token to avoid strict rate limits if you have one in env
    headers = {}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    # Fetch tree
    resp = requests.get(GITHUB_API_URL, headers=headers, timeout=60)
    resp.raise_for_status()
    data = resp.json()

    all_resource_files = [
        item["path"]
        for item in data.get("tree", [])
        if (
            item.get("type") == "blob"
            and item.get("path", "").startswith(BASE_PATH)
            and item.get("path", "").endswith(".go")
            and item.get("path", "").split("/")[-1].startswith("resource_")
        )
    ]

    service_to_resources = defaultdict(list)

    for file_path in all_resource_files:
        # e.g. google/services/apigee/resource_vmwareengine_external_access_rule.go
        parts = file_path.split("/")
        if len(parts) < 4:
            continue
        service_folder = parts[2]
        filename = parts[-1]
        core_repo_name = filename[len("resource_"):-len(".go")]  # vmwareengine_external_access_rule

        if core_repo_name in normalized_txt_resources:
            original_resource_name = normalized_txt_resources[core_repo_name]
            service_to_resources[service_folder].append(original_resource_name)

    return ensure_jsonable_service_map(service_to_resources)


def load_gcp_services(force_refresh=False):
    if not force_refresh and os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    try:
        service_map = fetch_gcp_services_from_github()
    except Exception as e:
        messagebox.showerror("GitHub error", f"Failed to fetch services: {e}")
        # Try cache as a fallback
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(service_map, f, indent=2)

    return service_map


def save_state(state):
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
    except Exception:
        pass


def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


# ---------- FILE OPS ----------
def copy_files(files, src_dir, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    for file in files:
        shutil.copyfile(os.path.join(src_dir, file), os.path.join(dest_dir, file))


def create_policy_files(service, resource, policy_name):
    if not policy_name:
        messagebox.showerror("Error", "Policy name cannot be empty.")
        return

    base_folder = service.replace(" ", "_")
    subfolder = get_subfolder_from_resource(resource)

    input_dir = os.path.join(INPUT_ROOT, base_folder, subfolder, policy_name)
    policy_dir = os.path.join(POLICY_ROOT, base_folder, subfolder, policy_name)
    vars_dir = os.path.join(POLICY_ROOT, base_folder, subfolder)

    # Terraform templates
    copy_files(TEMPLATE_FILES_TF, TEMPLATE_DIR, input_dir)
    # policy.rego
    copy_files([TEMPLATE_POLICY], TEMPLATE_DIR, policy_dir)
    # vars.rego once
    if not os.path.exists(os.path.join(vars_dir, TEMPLATE_VARS)):
        os.makedirs(vars_dir, exist_ok=True)
        shutil.copyfile(os.path.join(TEMPLATE_DIR, TEMPLATE_VARS), os.path.join(vars_dir, TEMPLATE_VARS))

    messagebox.showinfo("Success", f"Created structure for {service}/{resource}/{policy_name}")


# ---------- UI: Searchable, Scrollable Picker ----------
class SearchableDropdown(ctk.CTkFrame):
    """
    A compact field with a button that opens a popup
    containing a search box and a scrollable list of items.

    - values: list[str]
    - variable: ctk.StringVar to hold selection
    - command: optional callback called with selected value
    """

    def __init__(self, master, values=None, variable=None, placeholder="Select...", command=None, width=400):
        super().__init__(master)
        self.values_all = list(values or [])
        self.variable = variable or ctk.StringVar()
        self.command = command
        self.placeholder = placeholder
        self.dropdown = None

        self.grid_columnconfigure(0, weight=1)

        self.entry = ctk.CTkEntry(self, width=width)
        self.entry.insert(0, self.variable.get() or self.placeholder)
        self.entry.configure(state="disabled")
        self.entry.grid(row=0, column=0, sticky="ew", padx=(0, 6))

        self.btn = ctk.CTkButton(self, text="▼", width=36, command=self.open_dropdown)
        self.btn.grid(row=0, column=1)

    def set_values(self, values):
        self.values_all = list(values or [])
        # If current selection not in new list, clear field
        if self.variable.get() not in self.values_all:
            self.variable.set("")
            self.entry.configure(state="normal")
            self.entry.delete(0, "end")
            self.entry.insert(0, self.placeholder)
            self.entry.configure(state="disabled")

    def set(self, value):
        if value in self.values_all:
            self.variable.set(value)
            self.entry.configure(state="normal")
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
            self.entry.configure(state="disabled")
            if self.command:
                self.command(value)

    def get(self):
        return self.variable.get()

    def open_dropdown(self):
        if self.dropdown is not None and self.dropdown.winfo_exists():
            self.dropdown.focus()
            return

        # popup
        self.dropdown = ctk.CTkToplevel(self)
        self.dropdown.title("Select")
        self.dropdown.geometry("+%d+%d" % (self.winfo_rootx(), self.winfo_rooty() + self.winfo_height()))
        self.dropdown.transient(self.winfo_toplevel())
        self.dropdown.grab_set()

        # Resize
        self.dropdown.minsize(400, 380)
        self.dropdown.grid_columnconfigure(0, weight=1)
        self.dropdown.grid_rowconfigure(2, weight=1)

        # Search box
        search_var = ctk.StringVar()
        search_entry = ctk.CTkEntry(self.dropdown, placeholder_text="Type to filter...", textvariable=search_var)
        search_entry.grid(row=0, column=0, sticky="ew", padx=12, pady=(12, 6))

        # Count label
        self.count_label = ctk.CTkLabel(self.dropdown, text="")
        self.count_label.grid(row=1, column=0, sticky="w", padx=12, pady=(0, 6))

        # Scrollable list
        list_frame = ctk.CTkScrollableFrame(self.dropdown)
        list_frame.grid(row=2, column=0, sticky="nsew", padx=12, pady=(0, 12))

        # Build button list
        btn_holder = {"buttons": []}

        def rebuild_list(filter_text=""):
            # Clear previous buttons
            for b in btn_holder["buttons"]:
                b.destroy()
            btn_holder["buttons"].clear()

            ft = filter_text.strip().lower()
            if ft:
                filtered = [v for v in self.values_all if ft in v.lower()]
            else:
                filtered = list(self.values_all)

            # Update count
            self.count_label.configure(text=f"{len(filtered)} items")

            for v in filtered:
                b = ctk.CTkButton(list_frame, text=v, anchor="w",
                                  command=lambda val=v: on_select(val))
                b.pack(fill="x", padx=6, pady=4)
                btn_holder["buttons"].append(b)

        def on_select(value):
            self.set(value)
            # Save and close
            try:
                self.dropdown.destroy()
            except Exception:
                pass

        search_entry.bind("<KeyRelease>", lambda e: rebuild_list(search_var.get()))
        rebuild_list()
        search_entry.focus_set()

        # Close on focus out of popup
        def on_focus_out(_):
            if self.dropdown and not self.dropdown.focus_displayof():
                try:
                    self.dropdown.destroy()
                except Exception:
                    pass

        self.dropdown.bind("<FocusOut>", on_focus_out)


# ---------- MAIN APP ----------
class PolicyApp(ctk.CTk):
    def __init__(self, service_map, saved_state):
        super().__init__()
        self.title("Cloud Policy Generator")
        self.geometry("720x560")

        self.service_map = service_map  # dict: service -> [resources]
        self.saved_state = saved_state

        # Layout
        container = ctk.CTkFrame(self, corner_radius=12)
        container.pack(fill="both", expand=True, padx=16, pady=16)
        container.grid_columnconfigure(1, weight=1)

        row = 0

        # Cloud
        ctk.CTkLabel(container, text="Cloud").grid(row=row, column=0, sticky="w", padx=10, pady=10)
        self.cloud_var = ctk.StringVar(value=saved_state.get("cloud", "GCP"))
        self.cloud_field = SearchableDropdown(container, values=["GCP"], variable=self.cloud_var, width=420)
        self.cloud_field.grid(row=row, column=1, sticky="ew", padx=10, pady=10)
        row += 1

        # Service
        ctk.CTkLabel(container, text="Service").grid(row=row, column=0, sticky="w", padx=10, pady=10)
        self.service_var = ctk.StringVar(value="")
        self.service_field = SearchableDropdown(
            container,
            values=sorted(list(self.service_map.keys())),
            variable=self.service_var,
            command=self.on_service_change,
            width=420
        )
        self.service_field.grid(row=row, column=1, sticky="ew", padx=10, pady=10)
        row += 1

        # Resource
        ctk.CTkLabel(container, text="Resource").grid(row=row, column=0, sticky="w", padx=10, pady=10)
        self.resource_var = ctk.StringVar(value="")
        self.resource_field = SearchableDropdown(
            container,
            values=[],
            variable=self.resource_var,
            width=420
        )
        self.resource_field.grid(row=row, column=1, sticky="ew", padx=10, pady=10)
        row += 1

        # Policy name
        ctk.CTkLabel(container, text="Policy Name").grid(row=row, column=0, sticky="w", padx=10, pady=10)
        self.policy_entry = ctk.CTkEntry(container, width=420, placeholder_text="e.g. policy1")
        self.policy_entry.grid(row=row, column=1, sticky="ew", padx=10, pady=10)
        if saved_state.get("policy_name"):
            self.policy_entry.insert(0, saved_state["policy_name"])
        row += 1

        # Buttons
        btn_row = ctk.CTkFrame(container, fg_color="transparent")
        btn_row.grid(row=row, column=0, columnspan=2, sticky="ew", padx=10, pady=16)
        create_btn = ctk.CTkButton(btn_row, text="Create Policy", command=self.on_create)
        create_btn.pack(side="left", padx=(0, 10))
        refresh_btn = ctk.CTkButton(btn_row, text="Refresh Services", command=self.refresh_services)
        refresh_btn.pack(side="left")

        # Restore saved selections
        self.restore_saved_state()

        # Save on exit
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

    def restore_saved_state(self):
        saved_service = self.saved_state.get("service", "")
        saved_resource = self.saved_state.get("resource", "")

        # Service
        if saved_service in self.service_map:
            self.service_field.set(saved_service)
        else:
            # pick first for convenience
            services = sorted(list(self.service_map.keys()))
            if services:
                self.service_field.set(services[0])

        # Ensure resources list is built before setting resource
        self.on_service_change(self.service_var.get())

        # Resource
        resources = self.service_map.get(self.service_var.get(), [])
        if saved_resource in resources:
            self.resource_field.set(saved_resource)
        elif resources:
            self.resource_field.set(resources[0])

    def on_service_change(self, service_value):
        resources = sorted(self.service_map.get(service_value, []))
        self.resource_field.set_values(resources)
        # Clear resource selection if invalid
        if self.resource_var.get() not in resources:
            if resources:
                self.resource_field.set(resources[0])
            else:
                self.resource_var.set("")
                self.resource_field.entry.configure(state="normal")
                self.resource_field.entry.delete(0, "end")
                self.resource_field.entry.insert(0, self.resource_field.placeholder)
                self.resource_field.entry.configure(state="disabled")
        # Auto-save when selection changes
        self.save_current_state()

    def on_create(self):
        cloud = self.cloud_var.get()
        service = self.service_var.get()
        resource = self.resource_var.get()
        policy_name = self.policy_entry.get().strip()

        if cloud != "GCP":
            messagebox.showerror("Unsupported", "Only GCP is supported right now.")
            return

        if not service:
            messagebox.showerror("Error", "Please select a service.")
            return
        if not resource:
            messagebox.showerror("Error", "Please select a resource.")
            return

        create_policy_files(service, resource, policy_name)
        self.save_current_state()

    def refresh_services(self):
        new_map = load_gcp_services(force_refresh=True)
        if not new_map:
            messagebox.showerror("Error", "Could not refresh services.")
            return

        self.service_map = new_map
        self.service_field.set_values(sorted(list(self.service_map.keys())))
        # Keep current service if possible, else pick first
        curr_service = self.service_var.get()
        if curr_service in self.service_map:
            self.on_service_change(curr_service)
        else:
            services = sorted(list(self.service_map.keys()))
            if services:
                self.service_field.set(services[0])
                self.on_service_change(services[0])
        messagebox.showinfo("Refreshed", "Services refreshed from GitHub.")

    def current_state(self):
        return {
            "cloud": self.cloud_var.get(),
            "service": self.service_var.get(),
            "resource": self.resource_var.get(),
            "policy_name": self.policy_entry.get().strip()
        }

    def save_current_state(self):
        save_state(self.current_state())

    def on_exit(self):
        self.save_current_state()
        self.destroy()


if __name__ == "__main__":
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")

    service_map = load_gcp_services()
    app = PolicyApp(service_map, load_state())
    app.mainloop()
