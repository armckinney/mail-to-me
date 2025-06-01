variable "application" {
  description = "Name of the application to deploy"
  type        = string
}

variable "environment" {
  description = "Deployment Environment Name"
  type        = string
}

variable "containerapp_environment" {
  description = "Azure Container App Environment to place the certificate in"
  type = object({
    id = string
  })
}

variable "organization" {
  description = "Organization name for the application"
  type        = string
}

variable "organization_email" {
  description = "Email address for certificate register notifications"
  type        = string
}

variable "dns_zone" {
  description = "Name of the DNS zone"
  type = object({
    name                = string
    resource_group_name = string
  })
}

variable "time_rotating_days" {
  description = "Number of days to rotate the certificate"
  type        = number
  default     = 60

}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default     = {}
}
