# Monitoring Setup

This project uses kube-prometheus-stack to deploy Prometheus, Grafana, Alertmanager, kube-state-metrics, and node-exporter on AWS EKS.

## Install Monitoring

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm upgrade --install monitoring prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  -f monitoring/prometheus-values.yaml