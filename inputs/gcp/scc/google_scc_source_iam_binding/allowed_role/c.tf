resource "google_scc_source_iam_binding" "c" {
  organization = "1234"   
  source       = "5678"    
  role = "roles/securitycenter.findingsViewer -c"

  members = [
    "group:secops@deakin.edu.au",
  ]
}
