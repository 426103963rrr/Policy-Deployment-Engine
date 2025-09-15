resource "google_scc_organization_scc_big_query_export" "nc_default_dataset" {
  organization        = "organizations/123456789"
  big_query_export_id = "nc1"
  dataset             = "default"
}

resource "google_scc_organization_scc_big_query_export" "nc_unapproved_dataset" {
  organization        = "organizations/123456789"
  big_query_export_id = "nc2"
  dataset             = "bad_dataset"
}
