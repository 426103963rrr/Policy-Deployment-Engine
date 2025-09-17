## 🛡️ Policy Deployment Engine: `scc_project_notification_config`

This section provides a concise policy evaluation for the `scc_project_notification_config` resource in GCP.

Reference: [Terraform Registry – scc_project_notification_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_project_notification_config)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `pubsub_topic` | The Pub/Sub topic to send notifications to. Format: projects/[project_id]/topics/[topic]. | true | true | Notifications may contain sensitive findings. Sending to insecure or unauthorized topics risks exposing security data to unintended recipients. | None | None |
| `streaming_config` | Configuration for triggering streaming-based notifications. Determines which findings are sent. | true | true | Defines which findings trigger notifications. Weak, missing, or overly broad filters can either exclude critical findings or generate noise. | None | None |
| `config_id` | Unique identifier for the notification config within the project. | true | false | Ensures uniqueness and prevents conflicts, but does not directly impact security posture. | None | None |
| `description` | Optional description of the notification config (max 1024 characters). | false | false | Descriptions are informational only and do not affect security or functionality. | None | None |
| `project` | The project in which the notification config is defined. If not provided, the provider project is used. | true | false | Specifies scope but does not directly impact security posture. | None | None |

### streaming_config Block
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `filter` | Expression to filter findings for notification. Supports logical operators and comparison operators. | true | true | A proper filter ensures only relevant and high-severity findings are sent. Poor filters can miss important issues or overwhelm teams with unnecessary alerts. | None | None |
