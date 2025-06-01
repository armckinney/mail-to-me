resource "azurerm_log_analytics_workspace" "this" {
  name                = join("-", ["log", var.application, var.environment])
  resource_group_name = azurerm_resource_group.this.name
  location            = azurerm_resource_group.this.location
  tags                = local.tags
}
