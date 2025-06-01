variable "application" {
  description = "Name of the application to deploy"
  type        = string
}

variable "containerapp" {
  description = "Azure Container App Environment to place the certificate in"
  type = object({
    id                            = string
    latest_revision_fqdn          = string
    custom_domain_verification_id = string
  })
}

variable "dns_zone" {
  description = "Name of the DNS zone"
  type = object({
    name                = string
    resource_group_name = string
  })
}

variable "containerapp_environment_certificate" {
  description = "Azure Container App Environment Certificate to bind the custom domain to"
  type = object({
    id = string
  })
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default     = {}
}
