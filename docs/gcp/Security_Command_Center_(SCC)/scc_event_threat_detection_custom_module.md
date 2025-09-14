## 🛡️ Policy Deployment Engine: `scc_event_threat_detection_custom_module`

This section provides a concise policy evaluation for the `scc_event_threat_detection_custom_module` resource in GCP.

Reference: [Terraform Registry – scc_event_threat_detection_custom_module](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_event_threat_detection_custom_module)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `display_name` | A human-readable display name for the custom module. | false | false | Display names are for usability only and do not impact security. | enablement_state -c |  |
| `type` | The immutable type of Event Threat Detection module. Determines what kind of threat the module detects. | true | true | Using a valid detection type (e.g., CONFIGURABLE_BAD_IP) ensures the module functions correctly. Invalid types prevent proper detection. | CONFIGURABLE_BAD_IP | INVALID_TYPE |
| `organization` | The numerical ID of the parent organization where the module is deployed. | true | false | This ID determines scope but does not directly affect detection or security posture. | 123456789 | 000000000 |
| `config` | Configuration details for the custom module. Includes metadata such as severity, description, recommendation, and the IPs to detect. | true | true | The configuration defines the detection logic. Incorrect or empty values will result in incomplete or ineffective threat detection. | { "metadata": { "severity": "LOW", "description": "Flagged by Forcepoint as malicious", "recommendation": "Contact the owner of the relevant project." }, "ips": ["192.0.2.1", "192.0.2.0/24"] } | {} |
| `enablement_state` | Specifies whether the custom module is enabled or disabled. Must be ENABLED for detection to occur. | true | true | If disabled, the module will not detect threats, creating monitoring gaps. | ENABLED | DISABLED |
