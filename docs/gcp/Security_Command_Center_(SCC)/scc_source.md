## 🛡️ Policy Deployment Engine: `scc_source`

This section provides a concise policy evaluation for the `scc_source` resource in GCP.

Reference: [Terraform Registry – scc_source](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_source)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `display_name` | The source’s display name. Must be unique within the parent organization and follow naming rules. | true | false | The display name is used for identification and readability. It does not directly affect security but should be unique to avoid confusion. | None | None |
| `organization` | The organization in which the source exists. Format: organizations/[organization_id]. | true | true | Ensures the source is created in the correct organization. Misconfigured organization values can result in findings being logged under the wrong scope. | None | None |
| `description` | Optional description of the source (max 1024 characters). | false | false | Provides human-readable context for admins. This field does not impact security. | None | None |
