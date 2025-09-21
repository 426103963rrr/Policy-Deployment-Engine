package terraform.gcp.env

variables := {
    "location": "australia-southeast2",
    "allowed_regions": ["australia-southeast1","australia-southeast2"],
    "company_domain": "clientbusiness.com.au",
    "company_ip_range": "10.0.0.0/16",
    "project_id": "my-gcp-project",
    "org_id": "1234567890",
    "billing_account_id": "AAAAAA-BBBBBB-CCCCCC",
    "trusted_vpc_networks": ["prod-vpc","shared-services-vpc"],
    "allowed_roles": ["roles/viewer","roles/storage.objectViewer"],
    "disallowed_roles": ["roles/owner","roles/editor"],
    "require_labels": ["environment","cost_center","owner"],
    "encryption_required": true,
    "kms_key_id": "projects/my-gcp-project/locations/global/keyRings/main/cryptoKeys/cmek-key",
    "environment": "prod",
    "owner_team": "platform-team",
    "logging_bucket": "org-logging-bucket",
    "monitoring_project": "central-monitoring"
}
