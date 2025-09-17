## 🛡️ Policy Deployment Engine: `scc_organization_custom_module`

This section provides a concise policy evaluation for the `scc_organization_custom_module` resource in GCP.

Reference: [Terraform Registry – scc_organization_custom_module](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_organization_custom_module)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `display_name` | The display name of the custom module. This becomes the finding category for all findings returned by this module. | true | false | The display name is cosmetic and helps identify findings but does not directly affect security posture. | None | None |
| `enablement_state` | The enablement state of the custom module. Possible values: ENABLED or DISABLED. | true | true | If disabled, the module will not detect findings, resulting in blind spots in monitoring. | ENABLED | DISABLED |
| `custom_config` | Custom configuration for the module, including predicate, resource selector, severity, description, and recommendation. | true | true | Defines the detection logic for the module. Misconfigurations can lead to missed or incorrect findings. | None | None |
| `organization` | The numerical ID of the parent organization. | true | false | Defines scope of the module but does not affect detection or security posture directly. | None | None |

### custom_config Block
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `predicate` | CEL expression that evaluates resource properties to produce findings. A finding is generated when the expression evaluates to true. | true | true | Defines the detection condition. If incorrect or missing, the module may fail to identify issues. | None | None |
| `resource_selector` | The resource types that this custom module evaluates. | true | true | Scoping the module to specific resource types ensures relevant findings. Incorrect values may miss or misclassify findings. | None | None |
| `severity` | Severity level assigned to findings. Valid values: CRITICAL, HIGH, MEDIUM, LOW. | true | true | Severity guides prioritization and response to findings. Incorrect values may result in improper triage. | None | None |
| `description` | Explanation of the vulnerability or misconfiguration detected by the module. | false | false | Helps analysts understand findings but does not affect detection logic. | None | None |
| `recommendation` | Suggested remediation steps for the detected misconfiguration. | true | true | Recommendations ensure findings can be acted upon effectively. Without them, remediation may be delayed or incorrect. | None | None |
