## 🛡️ Policy Deployment Engine: `scc_folder_custom_module`

This section provides a concise policy evaluation for the `scc_folder_custom_module` resource in GCP.

Reference: [Terraform Registry – scc_folder_custom_module](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_folder_custom_module)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `display_name` | The display name of the Security Health Analytics custom module. This display name becomes the finding category for all findings returned by the module. | true | false | The display name improves readability and categorization but does not directly affect security. | None | None |
| `enablement_state` | The enablement state of the custom module. Possible values are: ENABLED, DISABLED. | true | true | If the module is disabled, findings will not be generated, resulting in blind spots in threat detection. | ENABLED | DISABLED |
| `custom_config` | The user-specified configuration for the custom module, defining conditions, outputs, and selectors. | true | true | The custom configuration dictates what misconfigurations are detected. Weak or empty configs reduce coverage. | None | None |
| `folder` | Numerical ID of the parent folder where the custom module is deployed. | true | false | Specifies scope of the module but does not directly influence detection logic. | None | None |

### custom_config Block
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `predicate` | CEL expression to evaluate resources and generate findings when true. | true | true | The predicate determines detection logic. Without it, the module will not detect violations. | None | None |
| `custom_output` | Custom output properties to add additional context to findings. | false | false | Custom output enhances visibility but does not directly affect security posture. | None | None |
| `resource_selector` | The resource types that the custom module evaluates. | true | true | Ensures findings are scoped to the correct resource types. Misconfigured selectors may miss critical resources. | None | None |
| `severity` | The severity assigned to findings from this module. Valid values: CRITICAL, HIGH, MEDIUM, LOW. | true | true | Severity impacts prioritization of findings in incident response workflows. | None | None |
| `description` | Text describing the vulnerability or misconfiguration detected by the custom module. | false | false | The description helps analysts understand the issue but does not affect detection logic. | None | None |
| `recommendation` | Steps recommended for resolving the detected misconfiguration or vulnerability. | true | true | Recommendations are critical for guiding remediation after detection. | None | None |
