package terraform.gcp.security.scc.google_scc_source_iam_binding.allowed_role

import data.terraform.gcp.helpers
import data.terraform.gcp.security.scc.google_scc_source_iam_binding.vars

conditions := [
  [
    {
      "situation_description": "Binding must use an approved test role.",
      "remedies": ["Use role: c"]
    },
    {
      "condition": "Role must be from the approved test list.",
      "attribute_path": "role",    
      "values": ["c"],
      "policy_type": "whitelist"
    }
  ]
]

summary := helpers.get_multi_summary(conditions, vars.variables)

message := summary.message
details := summary.details
