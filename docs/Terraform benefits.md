Terraform lets us use the same workflow to manage multiple providers and handle cross-cloud dependencies.
This simplifies management and orchestration for large-scale infrastructures.

All AWS components are available at terraform registry with examples and explanations.

## Summary
* [Benefits for using terraform]()
* [Useful Links]()


# Benefits for using terraform

#### Automated infrastructure management
Terraform can create configuration file templates to define, provision, and configure ECS resources in a repeatable and predictable manner,
reducing deployment and management errors resulting from human intervention.
In addition, Terraform can deploy the same template multiple times to create the same development, test, and production environment.

#### Infrastructure as code
With Terraform, we can use code to manage and maintain our resources. 
It allows you to store the infrastructure status, so that you can track the changes in different components of the system and share these configurations with others.

#### Reduced development costs
We can reduce costs by creating on-demand development and deployment environments. In addition, we can evaluate such environments before making system changes.

#### Reduced time to provision
Traditional click-ops methods of deployment used by organizations can take days or even weeks, in addition to being error-prone. With Terraform, full deployment can take just minutes.

# Terraform State 
Terraform stores state information about our managed infrastructure and configuration. This state is used to map real world resources to our configuration and then use it to determine which changes to make to your infrastructure.

This state file is extremely important, it maps various resource metadata to actual resource IDs so that Terraform knows what it is managing. This file must be saved and distributed to anyone who might run Terraform.


## Useful Links

* [Terraform aws module](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
* [Terraform Language](https://developer.hashicorp.com/terraform/language)
