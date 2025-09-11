## 🛡️ Policy Deployment Engine: `vertex_ai_dataset`

This section provides a concise policy evaluation for the `vertex_ai_dataset` resource in GCP.

Reference: [Terraform Registry – vertex_ai_dataset](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vertex_ai_dataset)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `display_name` | The user-defined name of the Dataset. The name can be up to 128 characters long and can be consist of any UTF-8 characters. | true | false | Display Name has no impact on the security of the resource or data contained. | None | None |
| `metadata_schema_uri` | Points to a YAML file stored on Google Cloud Storage describing additional information about the Dataset. The schema is defined as an OpenAPI 3.0.2 Schema Object. The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/metadata/. | true | false | None | None | None |
| `labels` | A set of key/value label pairs to assign to this Workflow. **Note**: This field is non-authoritative, and will only manage the labels present in your configuration. Please refer to the field `effective_labels` for all of the labels present on the resource. | false | false | None | None | None |
| `encryption_spec` | Customer-managed encryption key spec for a Dataset. If set, this Dataset and all sub-resources of this Dataset will be secured by this key. Structure is [documented below](#nested_encryption_spec). | false | true | Correct encryption standards on the VertexAI Dataset is critical to maintain confidentiality of the data. | None | None |
| `region` | The region of the dataset. eg us-central1 | false | false | None | None | None |
| `project` | If it is not provided, the provider project is used. | false | false | None | None | None |

### encryption_spec Block
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `kms_key_name` | Required. The Cloud KMS resource identifier of the customer managed encryption key used to protect a resource. Has the form: projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key. The key needs to be in the same region as where the resource is created. | false | true | The Encryption Key Name must be entered in the correct format to ensure encryption is matained on the dataset. | projects/my-project/locations/australia/keyRings/my-kr/cryptoKeys/my-key | projects/my-project/locations/us-east1/keyRings/my-kr/cryptoKeys/my-key |
