import requests
from collections import defaultdict

# Config
REPO_OWNER = "hashicorp"
REPO_NAME = "terraform-provider-google"
BRANCH = "main"
BASE_PATH = "google/services"
GITHUB_API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/git/trees/{BRANCH}?recursive=1"


# Load the txt resource names
with open("gcp_services.txt") as f:
    txt_resources = [line.strip() for line in f]

# Prepare normalized txt resource names without 'google_' prefix for matching
normalized_txt_resources = {}
for res in txt_resources:
    norm_res = res
    if res.startswith("google_"):
        norm_res = res[len("google_"):]
    normalized_txt_resources[norm_res] = res

# Fetch all files from repo recursively once
response = requests.get(GITHUB_API_URL)
response.raise_for_status()
data = response.json()

# Filter only resource files inside google/services with 'resource_*.go' pattern
all_resource_files = [
    item['path'] for item in data.get('tree', [])
    if (
        item['type'] == 'blob'
        and item['path'].startswith(BASE_PATH)
        and item['path'].endswith(".go")
        and item['path'].split('/')[-1].startswith("resource_")
    )
]

# Group matched resources by service folder
service_to_resources = defaultdict(list)

for file_path in all_resource_files:
    # e.g. "google/services/apigee/resource_vmwareengine_external_access_rule.go"
    parts = file_path.split('/')
    if len(parts) < 4:
        continue
    service_folder = parts[2]  # apigee in the example

    filename = parts[-1]  # resource_vmwareengine_external_access_rule.go
    core_repo_name = filename[len("resource_"):-len(".go")]  # vmwareengine_external_access_rule

    # Check if this core_repo_name exists in normalized_txt_resources keys
    if core_repo_name in normalized_txt_resources:
        original_resource_name = normalized_txt_resources[core_repo_name]
        service_to_resources[service_folder].append(original_resource_name)

# Print grouped result
for service, resources in service_to_resources.items():
    print(f"Service: {service}")
    for r in sorted(resources):
        print(f"  - {r}")
    print()
