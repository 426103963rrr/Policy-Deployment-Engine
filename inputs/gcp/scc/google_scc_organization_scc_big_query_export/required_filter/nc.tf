resource "google_scc_organization_scc_big_query_export" "nc" {
  organization        = "organizations/123456789"
  big_query_export_id = "scc_export_bad_filter -nc"
  filter              = ""  
}
resource "google_scc_organization_scc_big_query_export" "nc_no_sev" {
  organization        = "organizations/123456789"
  big_query_export_id = "scc_export_bad_filter_no_severity -nc"
  filter              = "category:\"Firewall\""  
}