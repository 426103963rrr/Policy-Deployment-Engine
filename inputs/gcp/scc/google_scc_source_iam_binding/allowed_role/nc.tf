resource "google_scc_source_iam_binding" "nc" {
  organization = "1234"
  source       = "2001"
  role         = "nc"
  members      = ["allAuthenticatedUsers"]
}
