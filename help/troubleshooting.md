# MegaMart Troubleshooting Guide

## Pod is Pending

kubectl get pods -n megamart
kubectl describe pod <pod-name> -n megamart

Check node capacity:
kubectl describe nodes

## Pod is CrashLoopBackOff

kubectl logs <pod-name> -n megamart
kubectl logs <pod-name> -n megamart --previous

## Check application deployments

kubectl get deployments -n megamart
kubectl rollout status deployment/catalog-service -n megamart
kubectl rollout status deployment/order-service -n megamart

## Check HPA

kubectl get hpa -n megamart
kubectl top pods -n megamart
kubectl top nodes

## Check Cluster Autoscaler

kubectl get pods -n kube-system | grep autoscaler
kubectl logs -n kube-system deployment/cluster-autoscaler-aws-cluster-autoscaler

## Check Argo CD

kubectl get application megamart -n argocd
kubectl describe application megamart -n argocd

## Check monitoring

kubectl get pods -n monitoring
kubectl get svc -n monitoring

## Check recent Kubernetes events

kubectl get events -A --sort-by=.lastTimestamp
