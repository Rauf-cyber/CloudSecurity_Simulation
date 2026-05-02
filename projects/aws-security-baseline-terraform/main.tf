terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "security_logs" {
  bucket = "${var.project_name}-security-logs-${data.aws_caller_identity.current.account_id}"
}

resource "aws_guardduty_detector" "main" {
  enable = true
}

data "aws_caller_identity" "current" {}
