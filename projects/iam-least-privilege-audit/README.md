# IAM Least-Privilege Audit (AWS)

A practical cloud-security project that audits AWS IAM users and roles for risky permissions and generates a remediation-ready JSON report.

## Why this project matters

Over-permissioned cloud identities are one of the most common ways attackers expand access after getting an initial foothold. This project demonstrates how to identify identity risks that matter in real AWS environments.

## What the script checks

- IAM users without MFA enabled
- Access keys older than the configured threshold
- Inline and attached policies with wildcard actions such as `Action: *`
- Policies with wildcard resources such as `Resource: *`
- `NotAction` usage in allow statements
- High-risk permissions such as `iam:*`, `kms:*`, `s3:*`, `ec2:*`, `lambda:*`, and `organizations:*`
- Security-service tampering actions such as stopping CloudTrail, deleting GuardDuty detectors, or deleting AWS Config recorders

## How to run

```bash
pip install -r requirements.txt
python audit_iam.py --region us-east-1 --output iam_audit_report.json --key-age-days 90
```

## Required AWS permissions

The script is designed for read-only review activity. The execution role or user should have permissions such as:

- `iam:ListUsers`
- `iam:ListRoles`
- `iam:ListMFADevices`
- `iam:ListAccessKeys`
- `iam:ListUserPolicies`
- `iam:GetUserPolicy`
- `iam:ListAttachedUserPolicies`
- `iam:ListRolePolicies`
- `iam:GetRolePolicy`
- `iam:ListAttachedRolePolicies`
- `iam:GetPolicy`
- `iam:GetPolicyVersion`
- `sts:GetCallerIdentity`

## Example output

```json
{
  "summary": {
    "high": 2,
    "medium": 3,
    "low": 0,
    "total": 5
  }
}
```

## Remediation guidance

| Finding | Recommended action |
|---|---|
| Missing MFA | Require MFA for human users and prefer federated access where possible |
| Old access key | Rotate or remove unused keys and move workloads to role-based access |
| Wildcard action | Replace broad actions with specific required API actions |
| Wildcard resource | Scope permissions to specific ARNs where supported |
| High-risk permission | Restrict to admin/security engineering roles with approval and monitoring |
| Security service tampering | Restrict to break-glass/admin paths and alert on usage |

## Portfolio value

This project shows cloud security engineering skills across IAM review, automation, policy analysis, evidence generation, and practical remediation planning.
