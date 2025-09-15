resource "google_scc_mute_config" "nc" {
  mute_config_id = "nc"
  parent         = "organizations/123456789"
  filter         = "category: \"OS_VULNERABILITY\""
  type           = "INVALID_TYPE"
}
