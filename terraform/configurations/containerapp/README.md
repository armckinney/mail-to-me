<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | 1.10.5 |
| <a name="requirement_acme"></a> [acme](#requirement\_acme) | 2.32.0 |
| <a name="requirement_azurerm"></a> [azurerm](#requirement\_azurerm) | 4.30.0 |
| <a name="requirement_random"></a> [random](#requirement\_random) | 3.7.2 |
| <a name="requirement_time"></a> [time](#requirement\_time) | 0.13.1 |
| <a name="requirement_tls"></a> [tls](#requirement\_tls) | 4.1.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_azurerm"></a> [azurerm](#provider\_azurerm) | 4.30.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_containerapp_custom_domain"></a> [containerapp\_custom\_domain](#module\_containerapp\_custom\_domain) | ../../modules/containerapp_custom_domain | n/a |
| <a name="module_containerapp_environment_certificate"></a> [containerapp\_environment\_certificate](#module\_containerapp\_environment\_certificate) | ../../modules/containerapp_environment_certificate | n/a |

## Resources

| Name | Type |
|------|------|
| [azurerm_container_app.this](https://registry.terraform.io/providers/hashicorp/azurerm/4.30.0/docs/resources/container_app) | resource |
| [azurerm_container_app_environment.this](https://registry.terraform.io/providers/hashicorp/azurerm/4.30.0/docs/resources/container_app_environment) | resource |
| [azurerm_log_analytics_workspace.this](https://registry.terraform.io/providers/hashicorp/azurerm/4.30.0/docs/resources/log_analytics_workspace) | resource |
| [azurerm_resource_group.this](https://registry.terraform.io/providers/hashicorp/azurerm/4.30.0/docs/resources/resource_group) | resource |
| [azurerm_dns_zone.this](https://registry.terraform.io/providers/hashicorp/azurerm/4.30.0/docs/data-sources/dns_zone) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_application"></a> [application](#input\_application) | Name of the application to deploy | `string` | n/a | yes |
| <a name="input_container_image"></a> [container\_image](#input\_container\_image) | Container image to deploy in the container app | `string` | `"docker.io/hello-world:latest"` | no |
| <a name="input_dns_zone"></a> [dns\_zone](#input\_dns\_zone) | DNS Zone object containing the name and resource group for the DNS zone | <pre>object({<br>    name        = string<br>    application = string<br>    environment = string<br>  })</pre> | `null` | no |
| <a name="input_environment"></a> [environment](#input\_environment) | Deployment Environment Name | `string` | n/a | yes |

## Outputs

No outputs.
<!-- END_TF_DOCS -->