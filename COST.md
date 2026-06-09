# AWS EKS AI Platform – Cost Analysis

## Project Overview

This project deploys a production-grade AWS EKS AI Platform using Terraform, Kubernetes, Helm, ArgoCD, GitHub Actions, Prometheus, Grafana, Amazon ECR, and AWS Load Balancers.

The objective is to demonstrate enterprise-level DevOps engineering, Infrastructure as Code (IaC), GitOps deployment automation, CI/CD pipelines, cloud-native monitoring, and scalable application deployment on AWS.

---

# AWS Resources Used

| Service | Purpose |
|----------|----------|
| Amazon EKS | Kubernetes Cluster |
| EC2 Managed Node Group | Worker Nodes |
| Amazon ECR | Docker Image Registry |
| Elastic Load Balancer | Public Application Access |
| VPC | Network Isolation |
| Public & Private Subnets | Networking |
| NAT Gateway | Internet Access for Private Resources |
| Security Groups | Access Control |
| IAM Roles | Authentication & Authorization |
| CloudWatch | Logging & Monitoring |
| Prometheus | Metrics Collection |
| Grafana | Monitoring Dashboards |

---

# Infrastructure Components

## Networking

- Amazon VPC
- Public Subnets
- Private Subnets
- Internet Gateway
- NAT Gateway
- Route Tables
- Security Groups

## Kubernetes

- Amazon EKS Cluster
- Managed Node Groups
- Kubernetes Deployments
- Kubernetes Services
- Horizontal Pod Autoscaler (HPA)
- AWS Load Balancer

## Monitoring

- Prometheus
- Grafana
- CloudWatch

## DevOps

- GitHub Actions
- ArgoCD
- Helm
- Terraform

---

# Estimated Monthly Cost

## Amazon EKS Control Plane

| Resource | Estimated Cost |
|-----------|-----------|
| Amazon EKS Cluster | ~$73/month |

---

## EC2 Worker Nodes

Assuming:

- 2 × t3.medium instances

| Resource | Estimated Cost |
|-----------|-----------|
| EC2 Worker Nodes | ~$60/month |

---

## AWS Load Balancer

| Resource | Estimated Cost |
|-----------|-----------|
| Elastic Load Balancer | ~$18/month |

---

## NAT Gateway

| Resource | Estimated Cost |
|-----------|-----------|
| NAT Gateway | ~$32/month |

---

## Amazon ECR

| Resource | Estimated Cost |
|-----------|-----------|
| Container Registry Storage | ~$1–5/month |

---

## CloudWatch

| Resource | Estimated Cost |
|-----------|-----------|
| Logs & Monitoring | ~$5–10/month |

---

# Estimated Total Monthly Cost

| Component | Approximate Cost |
|------------|----------------|
| Amazon EKS | $73 |
| EC2 Worker Nodes | $60 |
| Load Balancer | $18 |
| NAT Gateway | $32 |
| CloudWatch | $10 |
| ECR | $5 |
| **Total** | **~$150–200/month** |

---

# Cost Optimization Strategies

The following strategies can significantly reduce infrastructure costs:

### Kubernetes

- Use smaller EC2 instance types for development.
- Reduce node group size when idle.
- Enable cluster autoscaling.

### Networking

- Remove unused Load Balancers.
- Remove NAT Gateway when the cluster is not in use.

### Container Registry

- Delete unused Docker images.
- Configure image lifecycle policies.

### Monitoring

- Configure CloudWatch log retention.
- Reduce Prometheus retention period.

### Development Environment

- Destroy infrastructure after testing.
- Use Terraform to recreate resources when required.

---

# Cost Breakdown

```text
Amazon EKS Cluster         ~$73/month
EC2 Worker Nodes           ~$60/month
Load Balancer              ~$18/month
NAT Gateway                ~$32/month
CloudWatch                 ~$10/month
Amazon ECR                 ~$5/month
----------------------------------------
Estimated Total       ~$150–200/month
```

---

# Actual Project Cost

This project was developed as a portfolio and learning project.

Resources were provisioned only when required and were removed after testing to minimize AWS charges.

The actual cost depends on:

- Region
- Number of Nodes
- Application Traffic
- Monitoring Retention
- Storage Consumption
- Load Balancer Usage

---
# Destroying Infrastructure

To prevent unnecessary AWS charges, destroy all provisioned infrastructure when the project is not in use.

## Step 1: Navigate to Terraform Directory

```powershell
cd infra/aws
```

## Step 2: Review Planned Destruction

```powershell
terraform plan -destroy
```

This command shows which AWS resources will be removed.

## Step 3: Destroy Infrastructure

```powershell
terraform destroy
```

Type:

```text
yes
```

when prompted.

---

## Optional: Auto Approve

```powershell
terraform destroy -auto-approve
```

---

## Resources Removed

Terraform will remove:

- Amazon EKS Cluster
- Managed Node Groups
- EC2 Worker Nodes
- VPC
- Public Subnets
- Private Subnets
- NAT Gateway
- Route Tables
- Internet Gateway
- Security Groups
- IAM Resources (managed by Terraform)
- EKS Networking Components

---

## Verify Cleanup

Check that no clusters remain:

```powershell
aws eks list-clusters --region us-east-1
```

Check running EC2 instances:

```powershell
aws ec2 describe-instances --region us-east-1
```

Check load balancers:

```powershell
aws elbv2 describe-load-balancers --region us-east-1
```

---

## Important Note

Amazon ECR repositories, CloudWatch log groups, and manually created resources may not always be deleted automatically depending on the Terraform configuration.

Always verify resource cleanup in the AWS Console to avoid unexpected charges.
Important: Do NOT actually run terraform destroy now unless you're finished with the project and no longer need the EKS cluster, Grafana, ArgoCD, or Load Balancer. It will delete the infrastructure.

# Conclusion

The AWS EKS AI Platform demonstrates a complete production-grade cloud-native DevOps environment using Kubernetes, Terraform, GitOps, CI/CD, monitoring, and scalable application deployment on AWS.

The project showcases enterprise infrastructure engineering practices while maintaining a cost-conscious architecture suitable for portfolio and learning purposes.