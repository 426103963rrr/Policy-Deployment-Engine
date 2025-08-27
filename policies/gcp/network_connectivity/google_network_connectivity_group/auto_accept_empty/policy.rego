package terraform.gcp.security.network_connectivity.google_network_connectivity_group.auto_accept_empty

import data.terraform.gcp.helpers
import data.terraform.gcp.security.network_connectivity.google_network_connectivity_group.vars

conditions := [
    [
        {
            "situation_description": "Auto-accept projects must always be empty",
            "remedies": ["Remove all entries from auto_accept_projects"]
        },
        {
            "condition": "auto_accept_projects is empty",
            "attribute_path": ["auto_accept", 0, "auto_accept_projects"],
            "values": [[]], 
            "policy_type": "whitelist"
        }
    ]
]

message := helpers.get_multi_summary(conditions, vars.variables).message

details := helpers.get_multi_summary(conditions, vars.variables).details
