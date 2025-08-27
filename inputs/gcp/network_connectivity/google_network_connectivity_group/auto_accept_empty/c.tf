resource "google_network_connectivity_hub" "c_hub"  {
 name        = "network-connectivity-hub1"
 description = "A sample hub"
 project = "PDE-Project"
}

resource "google_network_connectivity_group" "c"  {
 hub         = google_network_connectivity_hub.c_hub.id
 name        = "default"
 project = "PDE-Project"
 description = "c"
 auto_accept {
    auto_accept_projects = []
  }
}