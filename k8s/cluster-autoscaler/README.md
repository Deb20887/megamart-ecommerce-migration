# Cluster Autoscaler

MegaMart uses Kubernetes Cluster Autoscaler to adjust EKS worker nodes based on pending pods.

## Configuration

- Cluster: megamart-eks
- Region: ap-south-1
- Node group: megamart-ng
- Instance type: t3.small
- Minimum nodes: 1
- Maximum nodes: 2
- Kubernetes: 1.34
- Cluster Autoscaler: 1.34.2
- Helm chart: 9.53.0

## IAM

IAM policy: MegaMartClusterAutoscalerPolicy

The IAM policy is managed separately and is not stored in this public repository.

No AWS credentials, access keys, passwords, or tokens are stored in this repository.

## Verification

kubectl get pods -n kube-system | grep autoscaler

aws eks describe-nodegroup --cluster-name megamart-eks --nodegroup-name megamart-ng --region ap-south-1
