<h1> Cloud Security Portfolio – AWS, Terraform, IAM Auditing, and Container Security </h1>

<h2>Overview</h2>
This repository now contains multiple hands-on cloud security projects that demonstrate practical skills across infrastructure-as-code, identity hardening, logging/monitoring, and DevSecOps automation.
<br />

## 🚀 Projects Included

### 1) AWS CloudFormation & S3 Management (Existing Project)
A project focused on deploying and managing AWS infrastructure with CloudFormation, including stack create/update/delete lifecycle and EC2 web deployment.

- **Skills:** CloudFormation, S3, EC2, VPC, IaC
- **Path:** repository root documentation + screenshots

### 2) IAM Least-Privilege Audit (Python + Boto3)
Automated IAM assessment script that detects wildcard permissions, high-risk action namespaces, missing MFA, and old access keys.

- **Skills:** IAM policy analysis, Python automation, security reporting
- **Path:** `projects/iam-least-privilege-audit/`
- **Main file:** `projects/iam-least-privilege-audit/audit_iam.py`

### 3) AWS Security Baseline (Terraform)
Terraform baseline to provision core cloud detection controls and secure logging storage.

- **Includes:** encrypted S3 log bucket, CloudTrail, GuardDuty, AWS Config recorder
- **Skills:** Terraform, governance controls, audit-readiness
- **Path:** `projects/aws-security-baseline-terraform/`

### 4) Container Security CI Pipeline (GitHub Actions + Trivy)
DevSecOps pipeline that builds a container image, scans for vulnerabilities, and fails CI on high/critical findings.

- **Skills:** container scanning, CI/CD policy enforcement, SARIF upload
- **Path:** `projects/container-security-ci/`
- **Workflow:** `.github/workflows/container-security.yml`

## 💡 Why this looks technically strong on GitHub

- Shows **breadth** (CloudFormation, Terraform, Python, CI security)
- Shows **security depth** (IAM least privilege, vulnerability gates, monitoring controls)
- Shows **real engineering workflow** (automation + evidence/report artifacts)

## 📌 Next upgrade ideas

- Add architecture diagrams for each project
- Add Terraform `tfsec` / `checkov` pipeline
- Add a Security Hub + EventBridge alerting mini-project
- Add a Kubernetes security mini-lab (EKS + OPA/Gatekeeper)
