resource "google_scc_notification_config" "c" {
  config_id   = "scc_notif_config_org_good -c"
  description = "Notification config with approved org"


  organization = "organizations/123456789012"

  pubsub_topic = "projects/security-core/topics/scc-findings"

  streaming_config {
    filter = "severity=\"HIGH\" OR severity=\"CRITICAL\""
  }
}
