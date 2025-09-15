resource "google_scc_organization_scc_big_query_export" "c" {
  organization        = "organizations/123456789"
  big_query_export_id = "c"
  dataset             = "projects/my-project/datasets/security_exports"
}
