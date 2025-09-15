resource "google_folder" "folder_nc1" {
  parent              = "organizations/123456789"
  display_name        = "nc1"
  deletion_protection = false
}

resource "google_scc_folder_custom_module" "nc1" {
  folder           = google_folder.folder_nc1.folder_id
  display_name     = "nc1"
  enablement_state = "DISABLED"

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
      resource_types = ["cloudkms.googleapis.com/CryptoKey"]
    }
    severity       = "LOW"
    description    = "Description of the custom module"
    recommendation = "Steps to resolve violation"
  }
}

resource "google_folder" "folder_nc2" {
  parent              = "organizations/123456789"
  display_name        = "nc2"
  deletion_protection = false
}

resource "google_scc_folder_custom_module" "nc2" {
  folder           = google_folder.folder_nc2.folder_id
  display_name     = "nc2"
  enablement_state = "DISABLED"

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
      resource_types = ["cloudkms.googleapis.com/CryptoKey"]
    }
    severity       = "LOW"
    description    = "Description of the custom module"
    recommendation = "Steps to resolve violation"
  }
}
