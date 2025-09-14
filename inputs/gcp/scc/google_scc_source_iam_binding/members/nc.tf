resource "google_scc_source_iam_binding" "scc_iam_binding_nc" {
  organization = "1234"
  source       = "5678"
  role         = "roles/securitycenter.findingsViewer"

  members = [
    "allUsers -nc",
    "user:external@gmail.comm -nc",
  ]
}
