resource "google_scc_organization_scc_big_query_export" "nc" {
  organization        = "organizations/123456789"
  big_query_export_id = "nc1"
  filter              = ""  
}
resource "google_scc_organization_scc_big_query_export" "nc_no_sev" {
  organization        = "organizations/123456789"
  big_query_export_id = "nc2"
  filter              = "category:\"Firewall\""  
}