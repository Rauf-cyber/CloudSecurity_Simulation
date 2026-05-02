<h1 align="center">☁️🔐 Cloud Security Engineer Portfolio</h1>

## 🏷️ Cloud Security Focus Areas
- IAM Hardening
- Infrastructure as Code Security
- AWS Security Monitoring
- DevSecOps Pipeline Security
- Container Vulnerability Management

<p align="center">
  <img src="https://img.shields.io/badge/Focus-Cloud%20Security-0ea5e9?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/AWS-Security-orange?style=for-the-badge&logo=amazonaws"/>
  <img src="https://img.shields.io/badge/Terraform-IaC-7c3aed?style=for-the-badge&logo=terraform"/>
  <img src="https://img.shields.io/badge/Python-Automation-22c55e?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/DevSecOps-CI%2FCD-ef4444?style=for-the-badge&logo=githubactions"/>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=140&text=Cloud%20Security%20Portfolio&fontAlign=50&fontAlignY=42&fontSize=34&color=0:0ea5e9,100:111827&fontColor=ffffff" alt="Cloud Security Portfolio Banner"/>
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
  IAMTool --> Report[JSON Findings Report]


