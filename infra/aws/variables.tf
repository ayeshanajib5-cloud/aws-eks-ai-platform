variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "aws-eks-ai-platform"
}

variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
  default     = "ai-platform-eks"
}