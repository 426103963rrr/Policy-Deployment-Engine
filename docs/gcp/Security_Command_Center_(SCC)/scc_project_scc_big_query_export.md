## 🛡️ Policy Deployment Engine: `scc_project_scc_big_query_export`

This section provides a concise policy evaluation for the `scc_project_scc_big_query_export` resource in GCP.

Reference: [Terraform Registry – scc_project_scc_big_query_export](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_project_scc_big_query_export)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `big_query_export_id` | Unique identifier for the BigQuery export within the project. | true | true | A valid, unique export ID ensures proper identification of exports and prevents overwriting existing sensitive data. | None | None |
| `description` | Optional description of the export (max 1024 characters). | false | false | Provides context for admins but does not impact security. | None | None |
| `dataset` | The BigQuery dataset where findings are exported. Format: projects/[projectId]/datasets/[datasetId]. Dataset names must contain only letters, numbers, or underscores. | false | true | Exports should be written to secure and approved datasets. Using temporary or default datasets may expose sensitive findings to unauthorized users. | None | None |
| `filter` | Expression defining which findings are exported. Can include conditions (e.g., severity) with logical operators (AND, OR). | false | true | A proper filter ensures only relevant findings are exported. Missing or weak filters may either miss critical issues or flood the dataset with irrelevant data. | None | None |
| `project` | The project where the export is defined. If not provided, the provider project is used. | true | false | Specifies the scope of the export but does not directly affect security posture. | None | None |
