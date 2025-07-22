# Cloud Native Monitoring App:: Python + EKS + ArgoCD

## 🚀 what is it about?

Simple Python Flask monitoring app:
- Containerized with Docker.
- Pushed to AWS ECR.
- Deployed to EKS via Terraform.
- Managed with ArgoCD for GitOps.
- Exposed via AWS LoadBalancer.

## ⚙️ How To Use

1. **Devlop Application**
    <any similar or any application of your choice>

2. **Build & Push Image**
   ```bash
   docker build -t my-monitoring-app .
   # Tag and push to ECR

3. **Provision your choice of infra**
    ```terraform init
        terraform plan
    `   terraform apply

4. **Deploy APp**
    ```kubectl apply -f deployment.yaml
       kubectl apply -f service.yaml


5. **Configure GitOps with ArgoCD**
    Install official setup: https://argo-cd.readthedocs.io/en/stable/getting_started/#1-install-argo-cd

    Log iin to ArgoCD UI with admin and password fromm your k8s argo namespace.

    Connect this repo.

    Sync & manage deployments.

    **🧹 Clean Code**
    Cluster state in EKS.
    Infra tracked in Terraform. 
    ```terraform destroy -auto-approve
    
