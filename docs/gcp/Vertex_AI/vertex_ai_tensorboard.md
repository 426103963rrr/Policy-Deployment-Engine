## 🛡️ Policy Deployment Engine: `vertex_ai_tensorboard`

This section provides a concise policy evaluation for the `vertex_ai_tensorboard` resource in GCP.

Reference: [Terraform Registry – vertex_ai_tensorboard](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vertex_ai_tensorboard)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `display_name` | User provided name of this Tensorboard. | true | false | None | None | None |
| `description` | Description of this Tensorboard. | false | false | None | None | None |
| `encryption_spec` | Customer-managed encryption key spec for a Tensorboard. If set, this Tensorboard and all sub-resources of this Tensorboard will be secured by this key. Structure is [documented below](#nested_encryption_spec). | false | false | None | None | None |
| `labels` | The labels with user-defined metadata to organize your Tensorboards. **Note**: This field is non-authoritative, and will only manage the labels present in your configuration. Please refer to the field `effective_labels` for all of the labels present on the resource. | false | false | None | None | None |
| `region` | The region of the tensorboard. eg us-central1 | false | false | None | None | None |
| `project` | If it is not provided, the provider project is used. | false | false | None | None | None |

### encryption_spec Block
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `kms_key_name` | The Cloud KMS resource identifier of the customer managed encryption key used to protect a resource. Has the form: projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key. The key needs to be in the same region as where the resource is created. | true | false | None | None | None |
