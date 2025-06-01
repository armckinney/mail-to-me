application     = "mailtome"
environment     = "prod"
container_image = "docker.io/armck/mail-to-me:app-latest"
dns_zone = {
  name        = "armckinney.dev"
  application = "armckinney"
  environment = "prod"
}
