# AWS EKS AI Platform – Enterprise DevOps & AI Infrastructure

## Project Overview

AWS EKS AI Platform is a production-grade cloud-native DevOps project designed to demonstrate enterprise infrastructure engineering, Kubernetes orchestration, Infrastructure as Code (IaC), GitOps deployment automation, CI/CD pipelines, monitoring, and scalable AI workload deployment.

The platform deploys containerized FastAPI AI services on Amazon EKS using Terraform, GitHub Actions, ArgoCD, Helm, Prometheus, and Grafana.

---

## Key Features

- AWS EKS Kubernetes Cluster
- Terraform Infrastructure as Code
- Modular Infrastructure Design
- Dockerized FastAPI Application
- Kubernetes Deployments and Services
- Horizontal Pod Autoscaling (HPA)
- Health Checks and Rolling Updates
- Helm Package Management
- GitHub Actions CI/CD
- Amazon ECR Container Registry
- ArgoCD GitOps Deployment
- Prometheus Monitoring
- Grafana Dashboards
- AWS IAM Security Configuration
- Load Balancer Exposure
- Production Repository Structure

---

## Technology Stack

### Cloud
- AWS

### Infrastructure as Code
- Terraform

### Containerization
- Docker
- Amazon ECR

### Orchestration
- Kubernetes (Amazon EKS)

### GitOps
- ArgoCD

### CI/CD
- GitHub Actions

### Monitoring
- Prometheus
- Grafana

### Backend
- FastAPI
- Python

---

## Architecture

```text
GitHub Repository
        │
        ▼
GitHub Actions CI/CD
        │
        ▼
Docker Image Build
        │
        ▼
Amazon ECR
        │
        ▼
ArgoCD GitOps
        │
        ▼
Amazon EKS Cluster
        │
        ▼
FastAPI AI Service
        │
        ▼
AWS Load Balancer
        │
        ▼
Prometheus & Grafana
        │
        ▼
Cloud Monitoring & Logging
```

---

## Repository Structure

```text
aws-eks-ai-platform/
│
├── api/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── infra/
│   └── aws/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       └── providers.tf
│
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   └── hpa.yaml
│
├── helm/
│   └── ai-platform/
│
├── argocd/
│   └── application.yaml
│
├── .github/
│   └── workflows/
│       ├── ci-cd.yml
│       └── terraform.yml
│
└── README.md
```

---

## Infrastructure Components

### Networking

- Custom VPC
- Public Subnets
- Private Subnets
- NAT Gateway
- Security Groups

### Kubernetes

- Amazon EKS Cluster
- Managed Node Group
- Kubernetes Deployment
- Kubernetes Service
- Horizontal Pod Autoscaler
- Load Balancer

### Container Registry

- Amazon Elastic Container Registry (ECR)

### Monitoring

- Prometheus
- Grafana

### GitOps

- ArgoCD Application Management

---

## Deployment Workflow

### Infrastructure Deployment

```bash
terraform init
terraform validate
terraform plan
terraform apply
```

### Docker Build

```bash
docker build -t ai-platform-api .
```

### Push Image to ECR

```bash
docker tag ai-platform-api:latest <ECR-URI>:latest
docker push <ECR-URI>:latest
```

### Kubernetes Deployment

```bash
kubectl apply -f k8s/
```

### Helm Deployment

```bash
helm upgrade --install ai-platform ./helm/ai-platform
```

### ArgoCD Deployment

```bash
kubectl apply -f argocd/application.yaml
```

---

## CI/CD Workflow

1. Developer pushes code to GitHub.
2. GitHub Actions pipeline starts automatically.
3. Docker image is built.
4. Docker image is pushed to Amazon ECR.
5. ArgoCD detects repository changes.
6. ArgoCD synchronizes Kubernetes resources.
7. Updated application is deployed to Amazon EKS.

---

## Monitoring Workflow

Prometheus collects:

- Cluster Metrics
- Node Metrics
- Pod Metrics
- Service Metrics

Grafana visualizes:

- CPU Utilization
- Memory Utilization
- Pod Health
- Cluster Status
- Application Metrics

---

## Screenshots

Add screenshots for:

- AWS EKS Cluster
- Amazon ECR Repository
- Running Kubernetes Pods
- FastAPI Swagger UI
- GitHub Actions Pipeline
- ArgoCD Dashboard
- Prometheus Monitoring
- Grafana Dashboard
- Terraform Apply Output

---

## Learning Outcomes

This project demonstrates:

- Kubernetes Administration
- Infrastructure as Code
- GitOps Workflows
- CI/CD Automation
- Cloud Infrastructure Engineering
- Container Orchestration
- Cloud Monitoring
- Production Deployment Practices
- Enterprise DevOps Engineering

---

## Author

**Ayesha Najib**

AWS | Kubernetes | Terraform | DevOps | Cloud Engineering | AI Infrastructure