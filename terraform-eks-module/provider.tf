terraform {
  required_version = ">= 1.2.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.20" # Latest AWS provider version, no messing around
    }
  }
}

provider "aws" {
  region = "eu-central-1" # Change this to your AWS region, keep it tight
}
