## 🛡️ Policy Deployment Engine: `scc_organization_scc_big_query_export`

This section provides a concise policy evaluation for the `scc_organization_scc_big_query_export` resource in GCP.

Reference: [Terraform Registry – scc_organization_scc_big_query_export](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_organization_scc_big_query_export)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `organization` | The organization where the BigQuery export configuration is created. Format: organizations/[organization_id]. | true | false | Defines the scope of the export but does not directly impact the security of exported data. | organizations/123456789 | organizations/000000000 |
| `big_query_export_id` | Unique identifier for the BigQuery export within the organization. | true | true | A valid, unique export ID ensures the correct identification of exports and avoids conflicts or overwriting of sensitive data. | scc_export_prod_australia-southeast1 -c | default |
| `description` | Optional description of the export (max 1024 characters). | false | false | Used for documentation and clarity only; does not affect security of the configuration. | Export of HIGH/CRITICAL findings to security dataset. |  |
| `dataset` | The BigQuery dataset where findings are exported. Format: projects/[projectId]/datasets/[datasetId]. Dataset names must contain only letters, numbers, or underscores. | false | true | Exports should be written to secure and approved datasets. Using unapproved or default datasets can expose sensitive findings. | projects/my-project/datasets/security_exports | projects/my-project/datasets/tmp_dataset |
| `filter` | Expression defining which findings are exported. Can include conditions (e.g., severity) combined with logical operators (AND, OR). | false | true | Filters ensure that only relevant findings are exported. Missing or overly broad filters can either miss critical issues or overwhelm the dataset with noise. | severity="HIGH" OR severity="CRITICAL" |  |
