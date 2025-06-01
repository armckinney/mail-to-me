resource "azurerm_resource_group" "this" {
  name     = join("-", ["rg", var.application, var.environment])
  location = local.location
  tags     = local.tags
}
