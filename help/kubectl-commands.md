# MegaMart kubectl Command Reference

## 1. Check cluster nodes

kubectl get nodes
kubectl top nodes

## 2. Check MegaMart workloads

kubectl get pods -n megamart
kubectl get deployments -n megamart
kubectl get services -n megamart
kubectl get hpa -n megamart

## 3. Check application logs

kubectl logs deployment/catalog-service -n megamart
kubectl logs deployment/order-service -n megamart

## 4. Test Catalog Service

kubectl run catalog-test --image=curlimages/curl:8.10.1 --restart=Never --rm -i -- curl -s http://catalog-service.megamart.svc.cluster.local:8000/health

kubectl run catalog-test --image=curlimages/curl:8.10.1 --restart=Never --rm -i -- curl -s http://catalog-service.megamart.svc.cluster.local:8000/products

## 5. Test Order Service

kubectl run order-test --image=curlimages/curl:8.10.1 --restart=Never --rm -i -- curl -s http://order-service.megamart.svc.cluster.local:8001/health

## 6. Argo CD GitOps

kubectl get application megamart -n argocd
kubectl describe application megamart -n argocd

## 7. Cluster Autoscaler

kubectl get pods -n kube-system | grep autoscaler
kubectl logs -n kube-system deployment/cluster-autoscaler-aws-cluster-autoscaler

## 8. Monitoring

kubectl get pods -n monitoring
kubectl get svc -n monitoring

## 9. Troubleshooting

kubectl describe pod <pod-name> -n <namespace>
kubectl logs <pod-name> -n <namespace>
kubectl get events -n <namespace> --sort-by=.lastTimestamp
