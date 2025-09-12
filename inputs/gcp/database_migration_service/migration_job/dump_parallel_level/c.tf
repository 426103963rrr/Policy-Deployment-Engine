resource "google_database_migration_service_migration_job" "c" {
    display_name          = "dbms_mj_compliant"
    location              = "australia-southeast2"
    migration_job_id  = "compliant-migration"
    project               = "gcp-project-id"
    type              = "CONTINUOUS"

    performance_config {
    dump_parallel_level = "MAX"
    }
     
    vpc_peering_connectivity {
    vpc = "dummy-vpc"
    }
    
    source      = "projects/proj-id/locations/australia-southeast2/connectionProfiles/source"
    destination = "projects/proj-id/locations/australia-southeast2/connectionProfiles/destination"
}