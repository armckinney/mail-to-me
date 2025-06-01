locals {
  location                = "eastus"
  organization            = "armckinney"
  letsencrypt_email       = "armck.phantom@gmail.com"
  dns_zone_resource_group = join("-", ["rg", var.dns_zone.application, var.dns_zone.environment])
  tags = {
    application = var.application
    environment = var.environment
  }
}
