## 🛡️ Policy Deployment Engine: `vertex_ai_feature_group`

This section provides a concise policy evaluation for the `vertex_ai_feature_group` resource in GCP.

Reference: [Terraform Registry – vertex_ai_feature_group](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vertex_ai_feature_group)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `name` | The resource name of the Feature Group. | false | false | None | None | None |
| `labels` | The labels with user-defined metadata to organize your FeatureGroup. **Note**: This field is non-authoritative, and will only manage the labels present in your configuration. Please refer to the field `effective_labels` for all of the labels present on the resource. | false | false | None | None | None |
| `description` | The description of the FeatureGroup. | false | false | None | None | None |
| `big_query` | Indicates that features for this group come from BigQuery Table/View. By default treats the source as a sparse time series source, which is required to have an entityId and a feature_timestamp column in the source. Structure is [documented below](#nested_big_query). | false | false | None | None | None |
| `region` | The region of feature group. eg us-central1 | false | false | None | None | None |
| `project` | If it is not provided, the provider project is used. | false | false | None | None | None |
| `big_query_source` |  | false | false | None | None | None |

### big_query Block
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `big_query_source` | The BigQuery source URI that points to either a BigQuery Table or View. Structure is [documented below](#nested_big_query_big_query_source). | true | false | None | None | None |
| `entity_id_columns` | Columns to construct entityId / row keys. If not provided defaults to entityId. | false | false | None | None | None |

### big_query_source Block
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `input_uri` | BigQuery URI to a table, up to 2000 characters long. For example: `bq://projectId.bqDatasetId.bqTableId.` | true | false | None | None | None |
