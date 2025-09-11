## 🛡️ Policy Deployment Engine: `vertex_ai_rag_engine_config`

This section provides a concise policy evaluation for the `vertex_ai_rag_engine_config` resource in GCP.

Reference: [Terraform Registry – vertex_ai_rag_engine_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vertex_ai_rag_engine_config)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `rag_managed_db_config` | Required. The config of the RagManagedDb used by RagEngine. Structure is [documented below](#nested_rag_managed_db_config). | true | false | None | None | None |
| `region` | The region of the RagEngineConfig. eg us-central1 | false | false | None | None | None |
| `project` | If it is not provided, the provider project is used. | false | false | None | None | None |

### rag_managed_db_config Block
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `scaled` | Scaled tier offers production grade performance along with autoscaling functionality. It is suitable for customers with large amounts of data or performance sensitive workloads. | false | false | None | None | None |
| `basic` | Basic tier is a cost-effective and low compute tier suitable for the following cases: Experimenting with RagManagedDb, Small data size, Latency insensitive workload, Only using RAG Engine with external vector DBs. NOTE: This is the default tier if not explicitly chosen. | false | false | None | None | None |
| `unprovisioned` | Disables the RAG Engine service and deletes all your data held within this service. This will halt the billing of the service. NOTE: Once deleted the data cannot be recovered. To start using RAG Engine again, you will need to update the tier by calling the UpdateRagEngineConfig API. | false | false | None | None | None |
