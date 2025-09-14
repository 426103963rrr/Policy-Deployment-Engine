## 🛡️ Policy Deployment Engine: `scc_folder_notification_config`

This section provides a concise policy evaluation for the `scc_folder_notification_config` resource in GCP.

Reference: [Terraform Registry – scc_folder_notification_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_folder_notification_config)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `pubsub_topic` | The Pub/Sub topic to send notifications to. Format: projects/[project_id]/topics/[topic]. | true | true | Notifications are delivered to the specified Pub/Sub topic. Using an unapproved or insecure topic may expose findings to unauthorized subscribers. | projects/security-core/topics/scc-findings | projects/test/topics/public-topic |
| `streaming_config` | Configuration for triggering streaming-based notifications. | true | true | The streaming filter defines which findings trigger notifications. Incorrect filters may miss critical issues or create excessive noise. | { "filter": "severity=\"HIGH\" OR severity=\"CRITICAL\"" } | { "filter": "" } |
| `folder` | Numerical ID of the parent folder where this notification config is defined. | true | false | The folder scope determines where notifications apply but does not affect the security of the configuration itself. | folders/987654321 |  |
| `config_id` | Unique identifier for the notification config within the organization. | true | false | The config ID ensures uniqueness but does not directly impact security. | scc_notif_config_stream_good -c |  |
| `description` | Optional description of the notification config (max 1024 characters). | false | false | Descriptions are for documentation purposes only and do not affect security. | Valid config with proper streaming filter |  |

### streaming_config Block
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `filter` | Filter expression applied across asset or finding events. Must include valid conditions such as severity levels to ensure important findings are captured. | true | true | A proper filter ensures that only relevant and high-severity findings are streamed. Missing or overly broad filters may reduce the effectiveness of alerts. | severity="HIGH" OR severity="CRITICAL" | severity="LOW" |
