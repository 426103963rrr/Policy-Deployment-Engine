package terraform.gcp.security.scc.mute_config.type

import data.terraform.gcp.helpers
import data.terraform.gcp.security.scc.mute_config.vars

conditions := [
  [
    {
      "situation_description": "Type in mute_config should be one of the accepted values.",
      "remedies": [
        "Type in mute_config should be one of MUTE_CONFIG_TYPE_UNSPECIFIED, STATIC, or DYNAMIC"
      ]
    },
    {
      "condition": "Check if the type is in a specific state",
      "attribute_path": ["type"],
      "values": [
        "MUTE_CONFIG_TYPE_UNSPECIFIED",
        "STATIC",
        "DYNAMIC"
      ],
      "policy_type": "whitelist"
    }
  ]
]

summary := helpers.get_multi_summary(conditions, vars.variables)

message := summary.message
details := summary.details
