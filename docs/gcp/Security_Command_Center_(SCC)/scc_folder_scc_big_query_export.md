## 🛡️ Policy Deployment Engine: `scc_folder_scc_big_query_export`

This section provides a concise policy evaluation for the `scc_folder_scc_big_query_export` resource in GCP.

Reference: [Terraform Registry – scc_folder_scc_big_query_export](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_folder_scc_big_query_export)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `description` | The description of the export (max 1024 characters). | false | false | The description is for documentation purposes only and does not affect security. | None | None |
| `dataset` | The BigQuery dataset to write findings' updates to. Format: projects/[projectId]/datasets/[datasetId]. | true | true | Exports must target approved, secure datasets. Using temporary or default datasets risks accidental exposure. | None | None |
| `filter` | Expression that defines which findings are exported. Should include severity conditions to prioritize critical issues. | true | true | Without a proper filter, important findings may be missed or too much irrelevant data may be exported, weakening security analysis. | None | None |
| `folder` | Numerical ID of the parent folder where the BigQuery export is defined. | true | false | Determines scope of the export but does not directly affect security posture. | None | None |
| `big_query_export_id` | A unique identifier for the BigQuery export within the folder. | true | true | Unique, descriptive export IDs help ensure correct configuration and prevent overwriting exports. | None | None |
