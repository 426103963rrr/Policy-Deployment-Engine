## 🛡️ Policy Deployment Engine: `vertex_ai_featurestore`

This section provides a concise policy evaluation for the `vertex_ai_featurestore` resource in GCP.

Reference: [Terraform Registry – vertex_ai_featurestore](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vertex_ai_featurestore)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `name` | The name of the Featurestore. This value may be up to 60 characters, and valid characters are [a-z0-9_]. The first character cannot be a number. | false | false | None | None | None |
| `labels` | A set of key/value label pairs to assign to this Featurestore. **Note**: This field is non-authoritative, and will only manage the labels present in your configuration. Please refer to the field `effective_labels` for all of the labels present on the resource. | false | false | None | None | None |
| `online_serving_config` | Config for online serving resources. Structure is [documented below](#nested_online_serving_config). | false | false | None | None | None |
| `online_storage_ttl_days` | , [Beta](https://terraform.io/docs/providers/google/guides/provider_versions.html)) TTL in days for feature values that will be stored in online serving storage. The Feature Store online storage periodically removes obsolete feature values older than onlineStorageTtlDays since the feature generation time. Note that onlineStorageTtlDays should be less than or equal to offlineStorageTtlDays for each EntityType under a featurestore. If not set, default to 4000 days | false | false | None | None | None |
| `encryption_spec` | If set, both of the online and offline data storage will be secured by this key. Structure is [documented below](#nested_encryption_spec). | false | false | None | None | None |
| `region` | The region of the dataset. eg us-central1 | false | false | None | None | None |
| `project` | If it is not provided, the provider project is used. | false | false | None | None | None |
| `force_destroy` |  | false | false | None | None | None |
| `scaling` |  | false | false | None | None | None |

### online_serving_config Block
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `fixed_node_count` | The number of nodes for each cluster. The number of nodes will not scale automatically but can be scaled manually by providing different values when updating. | false | false | None | None | None |
| `scaling` | Online serving scaling configuration. Only one of fixedNodeCount and scaling can be set. Setting one will reset the other. Structure is [documented below](#nested_online_serving_config_scaling). | false | false | None | None | None |

### encryption_spec Block
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `kms_key_name` | The Cloud KMS resource identifier of the customer managed encryption key used to protect a resource. Has the form: projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key. The key needs to be in the same region as where the compute resource is created. | true | false | None | None | None |

### scaling Block
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `min_node_count` | The minimum number of nodes to scale down to. Must be greater than or equal to 1. | true | false | None | None | None |
| `max_node_count` | The maximum number of nodes to scale up to. Must be greater than minNodeCount, and less than or equal to 10 times of 'minNodeCount'. | true | false | None | None | None |
