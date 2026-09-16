# MegaMart GitOps

This directory documents the GitOps structure used by the MegaMart project.

## GitOps Flow

```text
Developer
   |
   v
GitHub Repository
   |
   v
Argo CD
   |
   v
Amazon EKS
   |
   +--> Catalog Service
   |
   +--> Order Service
   |
   +--> HPA
   |
   +--> Monitoring

megamart-ecommerce-migration $

