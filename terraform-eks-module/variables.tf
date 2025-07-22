# I will keep things flexible, variables so i can easily change stuff later, things may break, and need fixing, technically i call it a build it as i fly it approach

variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "eu-central-1"
}

variable "cluster_name" {
  description = "Name for your EKS cluster"
  type        = string
  default     = "my-cloud-app-cluster"
}

variable "cluster_version" {
  description = "Kubernetes version for EKS cluster"
  type        = string
  default     = "1.27"
}

variable "node_instance_types" {
  description = "EC2 instance types for EKS nodes"
  type        = list(string)
  default     = ["t3.medium"]
}

variable "desired_capacity" {
  description = "Desired number of worker nodes"
  type        = number
  default     = 3
}

variable "max_capacity" {
  description = "Max number of worker nodes"
  type        = number
  default     = 3
}

variable "min_capacity" {
  description = "Min number of worker nodes"
  type        = number
  default     = 2
}

variable "aws_auth_users" {
  description = "IAM users to map to Kubernetes RBAC system:masters group"
  type = list(object({
    userarn  = string
    username = string
    groups   = list(string)
  }))
  default = [
    {
      userarn  = "arn:aws:iam::194722436853:user/Ak_DevOps" # my aws accnt arn
      username = "Ak_DevOps"
      groups   = ["system:masters"]
    }
  ]
}
