resource "google_folder" "folder_c" {
<<<<<<< HEAD
  parent              = "organizations/123456789"
  display_name        = "c"
=======
  parent       = "organizations/123456789"
  display_name = "c"
>>>>>>> dev
  deletion_protection = false
}

resource "google_scc_folder_custom_module" "c" {
<<<<<<< HEAD
  folder          = google_folder.folder_c.folder_id
  display_name    = "c"
=======
  folder = google_folder.folder_c.folder_id
  display_name = "c"
>>>>>>> dev
  enablement_state = "ENABLED"

  custom_config {
    predicate {
      expression   = "resource.rotationPeriod > duration(\"2592000s\")"
      title        = "Purpose of the expression"
      description  = "description of the expression"
      location     = "location of the expression"
    }
    custom_output {
      properties {
        name = "duration"
        value_expression {
          expression   = "resource.rotationPeriod"
          title        = "Purpose of the expression"
          description  = "description of the expression"
          location     = "location of the expression"
        }
      }
    }
    resource_selector {
      resource_types = [
        "cloudkms.googleapis.com/CryptoKey",
      ]
    }
    severity       = "LOW"
    description    = "Description of the custom module"
    recommendation = "Steps to resolve violation"
  }
}
