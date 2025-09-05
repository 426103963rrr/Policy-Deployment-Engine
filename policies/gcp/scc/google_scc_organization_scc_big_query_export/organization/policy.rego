package terraform.gcp.security.scc.google_scc_organization_scc_big_query_export.organization
import data.terraform.gcp.helpers
import data.terraform.gcp.security.scc.google_scc_organization_scc_big_query_export.vars

# only this org is approved
approved_orgs := [
  "organizations/123456789"
]

conditions := [
  [
    {
      "situation_description": "Organization ID must be organizations/123456789.",
      "remedies": [
        "Set organization to organizations/123456789"
      ]
    },
    {
      "condition": "Organization must equal the approved org ID.",
      "attribute_path": ["organization"],
      "values": approved_orgs,
      "policy_type": "whitelist"
    }
  ]
]

message := helpers.get_multi_summary(conditions, vars.variables).message
details := helpers.get_multi_summary(conditions, vars.variables).details
