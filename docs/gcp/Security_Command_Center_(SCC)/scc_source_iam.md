## 🛡️ Policy Deployment Engine: `scc_source_iam`

This section provides a concise policy evaluation for the `scc_source_iam` resource in GCP.

Reference: [Terraform Registry – scc_source_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_source_iam)

---

## Argument Reference
| Argument | Description | Required | Security Impact | Rationale | Compliant | Non-Compliant |
|----------|-------------|----------|-----------------|-----------|-----------|---------------|
| `source` | The ID of the SCC source to which the IAM policy is attached. | true | true | Specifies the SCC source being secured. Incorrect or missing source values could result in IAM bindings not being applied to the intended findings source. | None | None |
| `member/members` | The identities being granted the role. Supported formats include user:{email}, group:{email}, serviceAccount:{email}, domain:{domain}, or project-level identifiers. Avoid allUsers and allAuthenticatedUsers as they grant broad access. | true | true | Defining correct members ensures least privilege. Using public principals exposes sensitive findings to unauthorized users. | ["group:secops@deakin.edu.au"] | ["allUsers"] |
| `role` | The role assigned to the members. Must be a valid Security Command Center role or a custom role in the format [projects|organizations]/{parent}/roles/{role-name}. | true | true | Roles determine access scope. Using non-SCC roles or overly permissive roles can create security risks. | roles/securitycenter.findingsViewer | roles/owner |
| `policy_data` | An IAM policy data source to define multiple bindings at once. | false | true | When used, policy_data ensures consistent IAM application. If misconfigured, it can unintentionally override other bindings. | None | None |
