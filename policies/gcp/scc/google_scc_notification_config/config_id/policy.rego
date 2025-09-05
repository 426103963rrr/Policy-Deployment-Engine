package terraform.gcp.security.scc.google_scc_notification_config.config_id

import data.terraform.gcp.helpers
import data.terraform.gcp.security.scc.google_scc_notification_config.vars

conditions := [
  [
    {
      "situation_description": "Config ID must follow the naming convention.",
      "remedies": [
        "Ensure the config_id starts with 'scc_' and uses only lowercase letters, numbers, or underscores."
      ]
    },
    {
      "condition": "Config ID must match the allowlisted patterns.",
      "attribute_path": ["config_id"],
      "values": [
        "scc_notif_config_good",
        "scc_*"
      ],
      "policy_type": "whitelist"
    }
  ],
  [
    {
      "situation_description": "Config ID must not contain uppercase letters or invalid characters.",
      "remedies": [
        "Use lowercase letters, numbers, and underscores only."
      ]
    },
    {
      "condition": "Blacklist invalid IDs.",
      "attribute_path": ["config_id"],
      "values": [
        "NotifConfigBad",
        "INVALID*"
      ],
      "policy_type": "blacklist"
    }
  ]
]

message := helpers.get_multi_summary(conditions, vars.variables).message
details := helpers.get_multi_summary(conditions, vars.variables).details
