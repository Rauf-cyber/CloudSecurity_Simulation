# IAM Least-Privilege Audit (AWS)

A practical cloud-security project that audits AWS IAM users/roles for risky permissions and generates a remediation report.

## Why this project matters

Many breaches start with over-permissioned identities. This project demonstrates:

- Detection of wildcard permissions (`Action: *`, `Resource: *`)
- Detection of high-risk admin actions (`iam:*`, `kms:*`, `s3:*`, `ec2:*`)
- Detection of old access keys and users without MFA
- Export of findings into JSON for evidence and tracking
