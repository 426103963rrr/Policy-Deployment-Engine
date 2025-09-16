resource "google_scc_source_iam_binding" "scc_iam_binding_nc" {
  organization = "nc"
  source       = "5678"
  role         = "roles/securitycenter.findingsViewer"

  members = [
    "allAuthenticatedUsers",
    "allUsers"
  ]
}
