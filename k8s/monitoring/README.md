# Monitoring

MegaMart uses lightweight Prometheus and Grafana for Kubernetes monitoring.

## Components

- Prometheus: 3.14.0
- Grafana: 12.3.1
- Namespace: monitoring
- Prometheus service: ClusterIP
- Grafana service: ClusterIP

## Resource-conscious configuration

Prometheus persistence is disabled to avoid additional EBS storage costs.
Grafana persistence is disabled for the same reason.
No AWS Load Balancer is created for monitoring.

## Verification

kubectl get pods -n monitoring

kubectl get svc -n monitoring

Prometheus readiness can be checked with:

kubectl run prometheus-test --image=curlimages/curl:8.10.1 --restart=Never --rm -i -- curl -s http://prometheus-server.monitoring.svc.cluster.local/-/ready
