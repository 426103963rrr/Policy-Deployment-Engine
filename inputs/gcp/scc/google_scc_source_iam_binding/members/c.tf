resource "google_scc_source_iam_binding" "scc_iam_binding_c" {
  organization = "c"
  source       = "5678"
  role         = "roles/securitycenter.findingsViewer"

  members = [
    "group:secops@deakin.edu.au"
  ]
}
