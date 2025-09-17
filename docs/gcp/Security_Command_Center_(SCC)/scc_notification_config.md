## 🛡️ Policy Deployment Engine: `scc_notification_config`

This section provides a concise policy evaluation for the `scc_notification_config` resource in GCP.

Reference: [Terraform Registry – scc_notification_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_notification_config)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `pubsub_topic` | The Pub/Sub topic to send notifications to. Format: projects/[project_id]/topics/[topic]. | true | true | Notifications may contain sensitive findings. Using an insecure or unauthorized topic risks exposing data to unintended subscribers. | projects/security-core/topics/scc-findings | projects/test/topics/public-topic |
| `streaming_config` | Configuration for triggering streaming-based notifications. | true | true | Defines which findings trigger notifications. Weak or missing filters may allow irrelevant data or exclude critical issues. | { "filter": "severity=\"HIGH\" OR severity=\"CRITICAL\"" } | { "filter": "" } |
| `organization` | The organization in which the Notification Config is defined. | true | true | Ensuring the config is tied to the correct organization scope is critical for security. Misconfigured organizations may leak findings or fail to capture events. | organizations/123456789012 | organizations/000000000000 |
| `config_id` | Unique identifier for the notification config within the organization. | true | false | Ensures uniqueness but does not directly affect security posture. | None | None |
| `description` | Optional description of the notification config (max 1024 characters). | false | false | Descriptions are informational only and do not affect security. | None | None |

### streaming_config Block
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `filter` | Filter expression for selecting findings. Supports operators (=, >, <, :, etc.) and logical combinations (AND, OR, NOT). | true | true | Proper filtering ensures only relevant high-severity findings are sent. Overly broad or empty filters can reduce the effectiveness of alerting. | severity="HIGH" OR severity="CRITICAL" | severity="LOW" |
