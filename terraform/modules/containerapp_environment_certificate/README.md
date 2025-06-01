<!-- BEGIN_TF_DOCS -->
## Requirements

No requirements.

## Providers

| Name | Version |
|------|---------|
| <a name="provider_acme"></a> [acme](#provider\_acme) | 2.32.0 |
| <a name="provider_azurerm"></a> [azurerm](#provider\_azurerm) | 4.31.0 |
| <a name="provider_random"></a> [random](#provider\_random) | 3.7.2 |
| <a name="provider_time"></a> [time](#provider\_time) | 0.13.1 |
| <a name="provider_tls"></a> [tls](#provider\_tls) | 4.1.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [acme_certificate.this](https://registry.terraform.io/providers/vancluever/acme/latest/docs/resources/certificate) | resource |
| [acme_registration.this](https://registry.terraform.io/providers/vancluever/acme/latest/docs/resources/registration) | resource |
| [azurerm_container_app_environment_certificate.this](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_app_environment_certificate) | resource |
| [random_password.this](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/password) | resource |
| [time_rotating.this](https://registry.terraform.io/providers/hashicorp/time/latest/docs/resources/rotating) | resource |
| [tls_private_key.this](https://registry.terraform.io/providers/hashicorp/tls/latest/docs/resources/private_key) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_application"></a> [application](#input\_application) | Name of the application to deploy | `string` | n/a | yes |
| <a name="input_containerapp_environment"></a> [containerapp\_environment](#input\_containerapp\_environment) | Azure Container App Environment to place the certificate in | <pre>object({<br>    id = string<br>  })</pre> | n/a | yes |
| <a name="input_dns_zone"></a> [dns\_zone](#input\_dns\_zone) | Name of the DNS zone | <pre>object({<br>    name                = string<br>    resource_group_name = string<br>  })</pre> | n/a | yes |
| <a name="input_environment"></a> [environment](#input\_environment) | Deployment Environment Name | `string` | n/a | yes |
| <a name="input_organization"></a> [organization](#input\_organization) | Organization name for the application | `string` | n/a | yes |
| <a name="input_organization_email"></a> [organization\_email](#input\_organization\_email) | Email address for certificate register notifications | `string` | n/a | yes |
| <a name="input_tags"></a> [tags](#input\_tags) | Tags to apply to resources | `map(string)` | `{}` | no |
| <a name="input_time_rotating_days"></a> [time\_rotating\_days](#input\_time\_rotating\_days) | Number of days to rotate the certificate | `number` | `60` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_containerapp_environment_certificate"></a> [containerapp\_environment\_certificate](#output\_containerapp\_environment\_certificate) | n/a |
<!-- END_TF_DOCS -->