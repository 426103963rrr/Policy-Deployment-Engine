resource "google_scc_source_iam_binding" "nc_s1_owner_only" {
  organization = "1234"
  source       = "2001"
  role         = "nc1"
  members      = ["group:secops@deakin.edu.au"]
}

resource "google_scc_source_iam_binding" "nc_s2_public_only" {
  organization = "1234"
  source       = "2002"
  role         = "nc2"
  members      = ["allAuthenticatedUsers"]
}


