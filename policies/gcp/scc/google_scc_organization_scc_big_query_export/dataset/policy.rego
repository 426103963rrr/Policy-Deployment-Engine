package terraform.gcp.security.scc.google_scc_organization_scc_big_query_export.dataset

import data.terraform.gcp.helpers
import data.terraform.gcp.security.scc.google_scc_organization_scc_big_query_export.vars

approved_datasets := [
  "projects/my-project/datasets/security_exports"
]

conditions := [
  [
    {
      "situation_description": "Do not use placeholder dataset values.",
      "remedies": ["Replace placeholder datasets like default/test/tmp with a valid dataset name."]
    },
    {
      "condition": "Block weak or placeholder dataset names.",
      "attribute_path": ["dataset"],
      "values": [null, "" , "default", "test", "tmp"],
      "policy_type": "blacklist"
    }
  ],
  [
    {
      "situation_description": "Dataset must be from the approved allowlist.",
      "remedies": ["Use one of the approved datasets (e.g., projects/my-project/datasets/security_exports)."]
    },
    {
      "condition": "Dataset must match approved list.",
      "attribute_path": ["dataset"],
      "values": approved_datasets,
      "policy_type": "whitelist"
    }
  ]
]

message := helpers.get_multi_summary(conditions, vars.variables).message
details := helpers.get_multi_summary(conditions, vars.variables).details
