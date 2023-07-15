variable "tenant_id" {
  description = "Deployment Azure Tenant ID"
  type        = string
  sensitive   = true
}

variable "subscription_id" {
  description = "Deployment Azure Subscription ID"
  type        = string
  sensitive   = true
}

variable "environment" {
  description = "Deployment Environment Name"
  type        = string
  default     = "prod"
}

variable "location" {
  description = "Deployment Environment Location"
  type        = string
  default     = "eastus"
}

variable "smtp_username" {
  description = "Username for the STMP server login"
  type        = string
}

variable "smtp_password" {
  description = "Password for the SMTP server login"
  type        = string
}

locals {
  application                  = "mailtome"
  workspace_root               = "/workspaces/template-python"
  app_dockerfile_relative_path = "./app/Dockerfile"
  app_checksum                 = sha1(join("", [for f in fileset(path.module, "../../app/*") : filesha1(f)]))
  tags = {
    application = local.application
    environment = var.environment
  }
}
