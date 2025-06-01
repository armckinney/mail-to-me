resource "azurerm_dns_cname_record" "this" {
  name                = var.application
  zone_name           = var.dns_zone.name
  resource_group_name = var.dns_zone.resource_group_name
  ttl                 = 3600
  record              = var.containerapp.latest_revision_fqdn
  tags                = var.tags
}

resource "azurerm_dns_txt_record" "this" {
  name                = "asuid.${var.application}"
  zone_name           = var.dns_zone.name
  resource_group_name = var.dns_zone.resource_group_name
  ttl                 = 3600
  tags                = var.tags
  record {
    value = var.containerapp.custom_domain_verification_id
  }
}
