package terraform.gcp.security.scc.google_scc_notification_config.streaming_config

import data.terraform.gcp.helpers
import data.terraform.gcp.security.scc.google_scc_notification_config.vars

conditions := [
  [
    {
      "situation_description": "Streaming config filter must not be empty or placeholder.",
      "remedies": [
        "Provide a valid findings filter.",
        "Do not use blank or placeholder strings."
      ]
    },
    {
      "condition": "Filter cannot be empty or placeholder.",
      "attribute_path": ["streaming_config", 0, "filter"],
      "values": ["", "default", "test", "tmp", "TODO"],
      "policy_type": "blacklist"
    }
  ],
  [
    {
      "situation_description": "Streaming config must reference HIGH or CRITICAL severity findings.",
      "remedies": [
        "Set the filter to an approved severity expression."
      ]
    },
    {
      "condition": "Filter must exactly match one of the approved severities.",
      "attribute_path": ["streaming_config", 0, "filter"],
      "values": [
        "severity=\"HIGH\"",
        "severity=\"CRITICAL\"",
        "severity:(HIGH OR CRITICAL)",
        "severity=\"HIGH\" OR severity=\"CRITICAL\""
      ],
      "policy_type": "whitelist"
    }
  ]
]

message := helpers.get_multi_summary(conditions, vars.variables).message
details := helpers.get_multi_summary(conditions, vars.variables).details
