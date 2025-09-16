resource "google_scc_organization_scc_big_query_export" "nc" {
  organization        = "nc1"
  big_query_export_id = "default-test-export"
  filter              = ""  
}
resource "google_scc_organization_scc_big_query_export" "nc_no_sev" {
  organization        = "nc2"
  big_query_export_id = "tmp-scc-export"
  filter              = "category:\"Firewall\""  
}