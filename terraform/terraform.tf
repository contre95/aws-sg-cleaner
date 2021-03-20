terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

locals {
  # Common tags to be assigned to all resources
  common_tags = {
    Project = "Lucas Contreras Challange"
    Owner   = "lucascontre95@gmail.com"
  }
}

variable "SG_COLLECTORS" {
  type = string
}

variable "AWS_ACCOUNT_NUMBER" {
  type = string
}

variable "SQS_URL" {
  type = string
}

variable "QUEUE_NAME" {
  type = string
}

variable "RULE_GROUPS_ID_DENYLIST" {
  type = string
}
