
# add certificate to the container app environment
resource "azurerm_container_app_environment_certificate" "this" {
  name                         = "cert-${var.application}-${var.environment}"
  container_app_environment_id = var.containerapp_environment.id
  certificate_blob_base64      = acme_certificate.this.certificate_p12
  certificate_password         = acme_certificate.this.certificate_p12_password
  tags                         = var.tags
}
