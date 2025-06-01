
resource "azurerm_container_app_custom_domain" "this" {
  name                                     = trimsuffix(trimprefix(azurerm_dns_txt_record.this.fqdn, "asuid."), ".")
  container_app_id                         = var.containerapp.id
  certificate_binding_type                 = "SniEnabled"
  container_app_environment_certificate_id = var.containerapp_environment_certificate.id
}
