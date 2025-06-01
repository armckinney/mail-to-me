# account private key
resource "tls_private_key" "this" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

resource "time_rotating" "this" {
  rotation_days = var.time_rotating_days
}

# password for certificate encryption
resource "random_password" "this" {
  length  = 32
  special = true

  keepers = {
    rotation = time_rotating.this.id
  }
}
