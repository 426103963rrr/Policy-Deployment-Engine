resource "google_scc_organization_scc_big_query_export" "nc_default_dataset" {
  organization        = "organizations/123456789"
  big_query_export_id = "scc_export_bad_default_ds"
  dataset             = "default"
}

resource "google_scc_organization_scc_big_query_export" "nc_unapproved_dataset" {
  organization        = "organizations/123456789"
  big_query_export_id = "scc_export_bad_unapproved_ds"
  dataset             = "bad_dataset"
}
