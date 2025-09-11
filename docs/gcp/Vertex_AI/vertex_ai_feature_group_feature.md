## 🛡️ Policy Deployment Engine: `vertex_ai_feature_group_feature`

This section provides a concise policy evaluation for the `vertex_ai_feature_group_feature` resource in GCP.

Reference: [Terraform Registry – vertex_ai_feature_group_feature](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vertex_ai_feature_group_feature)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `name` | The resource name of the Feature Group Feature. | true | false | None | None | None |
| `feature_group` | The name of the Feature Group. | true | false | None | None | None |
| `region` | The region for the resource. It should be the same as the feature group's region. | true | false | None | None | None |
| `labels` | The labels with user-defined metadata to organize your FeatureGroup. **Note**: This field is non-authoritative, and will only manage the labels present in your configuration. Please refer to the field `effective_labels` for all of the labels present on the resource. | false | false | None | None | None |
| `description` | The description of the FeatureGroup. | false | false | None | None | None |
| `version_column_name` | The name of the BigQuery Table/View column hosting data for this version. If no value is provided, will use featureId. | false | false | None | None | None |
| `project` | If it is not provided, the provider project is used. | false | false | None | None | None |
