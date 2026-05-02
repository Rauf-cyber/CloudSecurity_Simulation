<h1 align="center">☁️🔐 Cloud Security Engineer Portfolio</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Focus-Cloud%20Security-0ea5e9?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/AWS-Security-orange?style=for-the-badge&logo=amazonaws"/>
  <img src="https://img.shields.io/badge/Terraform-IaC-7c3aed?style=for-the-badge&logo=terraform"/>
  <img src="https://img.shields.io/badge/Python-Automation-22c55e?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/DevSecOps-CI%2FCD-ef4444?style=for-the-badge&logo=githubactions"/>
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/Rauf-cyber/CloudSecurity_Simulation?style=flat-square" />
  <img src="https://img.shields.io/github/repo-size/Rauf-cyber/CloudSecurity_Simulation?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Actively%20Improving-success?style=flat-square" />
</p>


<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=200&text=Cloud%20Security%20Engineer%20Portfolio&fontAlign=50&fontAlignY=40&color=0:0ea5e9,100:111827&fontColor=ffffff" alt="Cloud Security Portfolio Banner"/>
</p>

## 🧱 High-Level Security Architecture

```mermaid
flowchart LR
  Dev[Developer Commit] --> GH[GitHub Repository]
  GH --> GA[GitHub Actions CI]
  GA --> TV[Trivy Scan]
  TV -->|SARIF| GS[GitHub Security Tab]

  GH --> IAC[IaC Layer]
  IAC --> CFN[AWS CloudFormation]
  IAC --> TF[Terraform Security Baseline]

  TF --> S3[(Encrypted S3 Logs)]
  TF --> CT[CloudTrail]
  TF --> GD[GuardDuty]
  TF --> CFG[AWS Config]

  IAMTool[IAM Audit Script] --> IAM[AWS IAM]
  IAMTool --> Report[JSON Findings Report]<h1> Cloud Security Portfolio – AWS, Terraform, IAM Auditing, and Container Security </h1>

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


