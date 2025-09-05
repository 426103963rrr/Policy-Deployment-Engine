resource "google_scc_source_iam_binding" "nc_s1_owner_only" {
  organization = "1234"
  source       = "2001"
  role         = "roles/owner"
  members      = ["group:secops@deakin.edu.au"]
}

resource "google_scc_source_iam_binding" "nc_s2_public_only" {
  organization = "1234"
  source       = "2002"
  role         = "roles/securitycenter.findingsViewer"
  members      = ["allAuthenticatedUsers"]
}


