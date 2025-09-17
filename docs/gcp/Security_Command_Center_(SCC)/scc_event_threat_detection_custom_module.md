## 🛡️ Policy Deployment Engine: `scc_event_threat_detection_custom_module`

This section provides a concise policy evaluation for the `scc_event_threat_detection_custom_module` resource in GCP.

Reference: [Terraform Registry – scc_event_threat_detection_custom_module](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_event_threat_detection_custom_module)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `display_name` | A human-readable display name for the custom module. | false | false | Display names are for usability only and do not impact security. | None | None |
| `type` | The immutable type of Event Threat Detection module. Determines what kind of threat the module detects. | true | false | Using a valid detection type (e.g., CONFIGURABLE_BAD_IP) ensures the module functions correctly. Invalid types prevent proper detection. | CONFIGURABLE_BAD_IP | INVALID_TYPE |
| `organization` | The numerical ID of the parent organization where the module is deployed. | true | false | This ID determines scope but does not directly affect detection or security posture. | None | None |
| `config` | Configuration details for the custom module. Includes detection logic parameters such as suspicious login detection settings. | true | true | The configuration defines the detection logic. If suspiciousLoginDetector.enabled is not set to true, login anomalies may not be detected. | {"suspiciousLoginDetector":{"enabled":true,"threshold":5,"timeWindow":"10m"}} | {"suspiciousLoginDetector":{"enabled":false}} |
| `enablement_state` | Specifies whether the custom module is enabled or disabled. Must be ENABLED for detection to occur. | true | true | If disabled, the module will not detect threats, creating monitoring gaps. | ENABLED | DISABLED |
