## 🛡️ Policy Deployment Engine: `scc_folder_notification_config`

This section provides a concise policy evaluation for the `scc_folder_notification_config` resource in GCP.

Reference: [Terraform Registry – scc_folder_notification_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_folder_notification_config)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `pubsub_topic` | The Pub/Sub topic to send notifications to. Format: projects/[project_id]/topics/[topic]. | true | true | Notifications are delivered to the specified Pub/Sub topic. Using an unapproved or insecure topic may expose findings to unauthorized subscribers. | None | None |
| `streaming_config` | Configuration for triggering streaming-based notifications. | true | true | The streaming filter defines which findings trigger notifications. Incorrect filters may miss critical issues or create excessive noise. | None | None |
| `organization` | The numerical ID of the parent organization where this notification config is defined. | true | true | Restricting configs to approved organizations ensures notifications aren’t misrouted to unauthorized orgs. | None | None |
| `folder` | Numerical ID of the parent folder where this notification config is defined. | true | false | The folder scope determines where notifications apply but does not affect the security of the configuration itself. | None | None |
| `config_id` | Unique identifier for the notification config within the organization. | true | false | The config ID ensures uniqueness but does not directly impact security. | None | None |
| `description` | Optional description of the notification config (max 1024 characters). | false | false | Descriptions are for documentation purposes only and do not affect security. | None | None |

### streaming_config Block
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `filter` | Filter expression applied across asset or finding events. Must include valid conditions such as severity levels to ensure important findings are captured. | true | true | A proper filter ensures that only relevant and high-severity findings are streamed. Missing or overly broad filters may reduce the effectiveness of alerts. | None | None |
