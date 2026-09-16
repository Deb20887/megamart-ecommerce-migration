# MegaMart Deployment Guide

## Prerequisites

- AWS CLI configured for the target AWS account
- kubectl installed
- Helm installed
- eksctl installed
- Git installed

## 1. Clone the repository

git clone https://github.com/Deb20887/megamart-ecommerce-migration.git
cd megamart-ecommerce-migration

## 2. Create the EKS cluster

eksctl create cluster -f eks-cluster.yaml

The cluster configuration uses the ap-south-1 region and the megamart-ng managed node group.

## 3. Configure kubectl

aws eks update-kubeconfig --region ap-south-1 --name megamart-eks

## 4. Deploy MegaMart Kubernetes resources

kubectl apply -k k8s/

## 5. Install Argo CD

kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

## 6. Deploy the Argo CD application

kubectl apply -f argocd/application.yaml

## 7. Verify GitOps

kubectl get application megamart -n argocd

Expected status:
Synced and Healthy

## 8. Verify MegaMart

kubectl get pods -n megamart
kubectl get svc -n megamart
kubectl get hpa -n megamart

## Important

Do not commit AWS credentials, GitHub tokens, passwords, kubeconfig files, or other secrets to this public repository.
