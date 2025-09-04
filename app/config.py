
import os

# Absolute path to where this script (main.py) lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Where Selenium stores cache and rendered HTMLs
CACHE_DIR = os.path.join(BASE_DIR, "cache")

# Terraform Provider Docs
CLOUD_CONFIGS = {
    "GCP": {
        "url": "https://registry.terraform.io/providers/hashicorp/google/latest/docs",
        "cache_file": os.path.join(CACHE_DIR, "gcp_service_cache.json"),
    },
    # "AWS": {
    #     "url": "https://registry.terraform.io/providers/hashicorp/aws/latest/docs",
    #     "cache_file": os.path.join(CACHE_DIR, "aws_service_cache.json"),
    # },
    "Azure": {
        "url": "https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs",
        "cache_file": os.path.join(CACHE_DIR, "azure_service_cache.json"),
    },
    # "Oracle": {
    #     "url": "https://registry.terraform.io/providers/oracle/oci/latest/docs",
    #     "cache_file": os.path.join(CACHE_DIR, "oracle_service_cache.json"),
    # },
}

# GUI session state
STATE_FILE = os.path.join(CACHE_DIR, "user_state.json")

# External folders
TEMPLATE_BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "templates"))
INPUT_BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "inputs"))
POLICY_BASE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "policies"))

# Template file names (standardized)
TEMPLATE_FILES_TF = ["c.tf", "config.tf", "nc.tf"]
TEMPLATE_POLICY = "policy.rego"
TEMPLATE_VARS = "vars.rego"
