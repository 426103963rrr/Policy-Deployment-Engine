resource "google_scc_notification_config" "nc" {
  config_id   = "scc_notif_config_stream_bad"
  description = "Invalid config with weak/empty streaming filter"

  organization = "organizations/123456789012"

  pubsub_topic = "projects/security-core/topics/scc-findings"


  streaming_config {
    filter = ""
  }
}
