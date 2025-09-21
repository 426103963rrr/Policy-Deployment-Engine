resource "google_network_connectivity_hub" "nc_hub"  {
 name        = "network-connectivity-hub1"
 description = "A sample hub"
 project = "PDE-Project"
}

resource "google_network_connectivity_group" "nc"  {
 hub         = google_network_connectivity_hub.nc_hub.id
 name        = "default"
 project = "PDE-Project"
 description = "nc"
 auto_accept {
    auto_accept_projects = [
      "foo", 
      "bar", 
    ]
  }
}