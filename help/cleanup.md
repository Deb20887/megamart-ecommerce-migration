# MegaMart AWS Cleanup Guide

## Important

The GitHub repository is the permanent source of truth. AWS resources can be deleted after the demo without deleting the source code.

## 1. Delete the EKS cluster

eksctl delete cluster --name megamart-eks --region ap-south-1

This removes the EKS control plane and associated worker infrastructure managed by eksctl.

## 2. Delete the DynamoDB table

aws dynamodb delete-table --table-name MegaMartOrders --region ap-south-1

## 3. Delete ECR repositories if no longer required

aws ecr delete-repository --repository-name megamart-catalog --force --region ap-south-1
aws ecr delete-repository --repository-name megamart-order --force --region ap-south-1

## 4. Verify remaining resources

aws eks list-clusters --region ap-south-1
aws dynamodb list-tables --region ap-south-1
aws ecr describe-repositories --region ap-south-1

## Cost control

Deleting the EKS cluster removes the EKS worker infrastructure created for this project.
Delete the DynamoDB table and ECR repositories when they are no longer needed.
Always verify the AWS Console Billing and Cost Management page after cleanup.

## GitHub

The GitHub repository remains available after AWS cleanup and can be used to recreate the project.
