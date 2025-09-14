package terraform.gcp.security.scc.google_scc_source_iam_binding.allowed_role

import data.terraform.gcp.helpers
import data.terraform.gcp.security.scc.google_scc_source_iam_binding.vars


conditions := [
  [
    {
      "situation_description": "Binding must use an approved SCC role.",
      "remedies": ["Use one of: roles/securitycenter.findingsViewer, roles/securitycenter.findingsEditor, roles/securitycenter.admin"]
    },
    {
      "condition": "Role must be from the approved SCC list.",
      "attribute_path": ["role"],
      "values": [
        "roles/securitycenter.findingsViewer",
        "roles/securitycenter.findingsEditor",
        "roles/securitycenter.admin"
      ],
      "policy_type": "whitelist"
    }
  ],
  [
    {
      "situation_description": "Public principals are not allowed.",
      "remedies": ["Remove allUsers/allAuthenticatedUsers; grant access to a least-privilege group instead"]
    },
    {
      "condition": "Members must not include public identities.",
      "attribute_path": ["members", 0],
      "values": ["allUsers", "allAuthenticatedUsers"],
      "policy_type": "blacklist"
    }
  ]
]

message := helpers.get_multi_summary(conditions, vars.variables).message
details := helpers.get_multi_summary(conditions, vars.variables).details
