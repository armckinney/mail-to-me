# acme registration (let's encrypt account)
resource "acme_registration" "this" {
  email_address   = var.organization_email
  account_key_pem = tls_private_key.this.private_key_pem
}

# request the certificate from let's encrypt
resource "acme_certificate" "this" {
  common_name = "www.${var.application}.${var.dns_zone.name}"
  subject_alternative_names = [
    "${var.application}.${var.dns_zone.name}"
  ]
  account_key_pem          = acme_registration.this.account_key_pem
  certificate_p12_password = random_password.this.result

  pre_check_delay = 60

  dns_challenge {
    provider = "azure"
    config = {
      AZURE_ZONE_NAME      = var.dns_zone.name
      AZURE_RESOURCE_GROUP = var.dns_zone.resource_group_name
    }
  }
}

