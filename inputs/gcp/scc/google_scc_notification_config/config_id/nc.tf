resource "google_scc_notification_config" "nc" {
  # Bad: doesn’t follow naming convention (missing scc_ prefix, uses uppercase)
  config_id   = "NotifConfigBad"
  description = "Notification config with invalid ID"

  organization = "organizations/123456789012"
  pubsub_topic = "projects/security-core/topics/scc-findings"

  streaming_config {
    filter = "severity=\"HIGH\""
  }
}
