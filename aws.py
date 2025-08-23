import json

# Load the JSON file
with open("providers-schema.json", "r") as file:
    data = json.load(file)

# Navigate to the resource_schemas keys for AWS provider
aws_provider = data["provider_schemas"]["registry.terraform.io/hashicorp/aws"]
resource_schemas = aws_provider.get("resource_schemas", {})

# Get and print the keys
with open("aws_services.txt", "w") as output_file:
    for resource in resource_schemas.keys():
        output_file.write(resource + "\n")