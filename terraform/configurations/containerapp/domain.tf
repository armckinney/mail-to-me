module "containerapp_environment_certificate" {
  source = "../../modules/containerapp_environment_certificate"
  count  = var.dns_zone != null ? 1 : 0

  containerapp_environment = azurerm_container_app_environment.this

  application = var.application
  environment = var.environment

  dns_zone           = data.azurerm_dns_zone.this
  organization       = local.organization
  organization_email = local.letsencrypt_email
  time_rotating_days = 59
  tags               = local.tags
}

module "containerapp_custom_domain" {
  source = "../../modules/containerapp_custom_domain"
  count  = var.dns_zone != null ? 1 : 0

  application                          = var.application
  containerapp                         = azurerm_container_app.this
  dns_zone                             = data.azurerm_dns_zone.this
  containerapp_environment_certificate = module.containerapp_environment_certificate[0].containerapp_environment_certificate
  tags                                 = local.tags
}
