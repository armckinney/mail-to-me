application     = "mailtome"
environment     = "prod"
container_image = "ghcr.io/armckinney/mail-to-me:app-latest"
dns_zone = {
  name        = "armckinney.dev"
  application = "armckinney"
  environment = "prod"
}
