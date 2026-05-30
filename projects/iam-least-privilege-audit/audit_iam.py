#!/usr/bin/env python3
"""
AWS IAM Least-Privilege Audit

This script performs read-only IAM checks and generates a JSON report with
findings that can support remediation tracking.

Checks included:
- Users without MFA
- Access keys older than the configured threshold
- Inline and attached policies with wildcard actions/resources
- High-risk IAM, KMS, S3, EC2, Lambda, and Organizations permissions
"""

import argparse
import datetime as dt
import fnmatch
import json
from collections import Counter
from typing import Any, Dict, Iterable, List

import boto3
from botocore.exceptions import ClientError

HIGH_RISK_ACTION_PATTERNS = [
    "iam:*",
    "kms:*",
    "s3:*",
    "ec2:*",
    "lambda:*",
    "organizations:*",
    "cloudtrail:StopLogging",
    "cloudtrail:DeleteTrail",
    "config:DeleteConfigurationRecorder",
    "guardduty:DeleteDetector",
]


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def as_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def action_matches(pattern: str, action: str) -> bool:
    return fnmatch.fnmatch(action.lower(), pattern.lower())


def add_finding(findings: List[Dict[str, Any]], identity_type: str, identity_name: str, severity: str, issue: str, details: Dict[str, Any]) -> None:
    findings.append(
        {
            "identity_type": identity_type,
            "identity_name": identity_name,
            "severity": severity,
            "issue": issue,
            "details": details,
        }
    )


def evaluate_policy_document(findings: List[Dict[str, Any]], identity_type: str, identity_name: str, policy_name: str, document: Dict[str, Any]) -> None:
    for statement in as_list(document.get("Statement")):
        if statement.get("Effect") != "Allow":
            continue

        actions = as_list(statement.get("Action"))
        not_actions = as_list(statement.get("NotAction"))
        resources = as_list(statement.get("Resource"))

        if "*" in actions:
            add_finding(
                findings,
                identity_type,
                identity_name,
                "high",
                "Wildcard action detected",
                {"policy_name": policy_name, "action": "*", "resource": resources},
            )

        if "*" in resources:
            add_finding(
                findings,
                identity_type,
                identity_name,
                "medium",
                "Wildcard resource detected",
                {"policy_name": policy_name, "actions": actions, "resource": "*"},
            )

        if not_actions:
            add_finding(
                findings,
                identity_type,
                identity_name,
                "high",
                "NotAction used in allow statement",
                {"policy_name": policy_name, "not_actions": not_actions, "resource": resources},
            )

        for action in actions:
            for risky_pattern in HIGH_RISK_ACTION_PATTERNS:
                if action_matches(risky_pattern, action):
                    add_finding(
                        findings,
                        identity_type,
                        identity_name,
                        "high",
                        "High-risk permission detected",
                        {"policy_name": policy_name, "action": action, "matched_pattern": risky_pattern, "resource": resources},
                    )


def get_attached_policy_document(iam, policy_arn: str) -> Dict[str, Any]:
    policy = iam.get_policy(PolicyArn=policy_arn)["Policy"]
    version = iam.get_policy_version(PolicyArn=policy_arn, VersionId=policy["DefaultVersionId"])
    return version["PolicyVersion"]["Document"]


def audit_user(iam, user: Dict[str, Any], findings: List[Dict[str, Any]], key_age_days: int) -> None:
    user_name = user["UserName"]

    mfa_devices = iam.list_mfa_devices(UserName=user_name).get("MFADevices", [])
    if not mfa_devices:
        add_finding(findings, "User", user_name, "medium", "MFA not enabled", {})

    for key in iam.list_access_keys(UserName=user_name).get("AccessKeyMetadata", []):
        age = (utc_now() - key["CreateDate"]).days
        if age >= key_age_days:
            add_finding(
                findings,
                "User",
                user_name,
                "medium",
                "Access key exceeds age threshold",
                {"access_key_id": key["AccessKeyId"], "age_days": age, "threshold_days": key_age_days, "status": key["Status"]},
            )

    for policy_name in iam.list_user_policies(UserName=user_name).get("PolicyNames", []):
        document = iam.get_user_policy(UserName=user_name, PolicyName=policy_name)["PolicyDocument"]
        evaluate_policy_document(findings, "User", user_name, policy_name, document)

    for policy in iam.list_attached_user_policies(UserName=user_name).get("AttachedPolicies", []):
        document = get_attached_policy_document(iam, policy["PolicyArn"])
        evaluate_policy_document(findings, "User", user_name, policy["PolicyName"], document)


def audit_role(iam, role: Dict[str, Any], findings: List[Dict[str, Any]]) -> None:
    role_name = role["RoleName"]

    for policy_name in iam.list_role_policies(RoleName=role_name).get("PolicyNames", []):
        document = iam.get_role_policy(RoleName=role_name, PolicyName=policy_name)["PolicyDocument"]
        evaluate_policy_document(findings, "Role", role_name, policy_name, document)

    for policy in iam.list_attached_role_policies(RoleName=role_name).get("AttachedPolicies", []):
        document = get_attached_policy_document(iam, policy["PolicyArn"])
        evaluate_policy_document(findings, "Role", role_name, policy["PolicyName"], document)


def paginate(client_method, result_key: str, **kwargs) -> Iterable[Dict[str, Any]]:
    marker = None
    while True:
        request = dict(kwargs)
        if marker:
            request["Marker"] = marker
        response = client_method(**request)
        for item in response.get(result_key, []):
            yield item
        if not response.get("IsTruncated"):
            break
        marker = response.get("Marker")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit AWS IAM for least-privilege risks.")
    parser.add_argument("--region", default="us-east-1")
    parser.add_argument("--output", default="iam_audit_report.json")
    parser.add_argument("--key-age-days", type=int, default=90)
    args = parser.parse_args()

    session = boto3.session.Session(region_name=args.region)
    sts = session.client("sts")
    iam = session.client("iam")
    account_id = sts.get_caller_identity()["Account"]

    findings: List[Dict[str, Any]] = []

    try:
        for user in paginate(iam.list_users, "Users"):
            audit_user(iam, user, findings, args.key_age_days)

        for role in paginate(iam.list_roles, "Roles"):
            audit_role(iam, role, findings)

    except ClientError as error:
        add_finding(
            findings,
            "Account",
            account_id,
            "high",
            "Audit execution error",
            {"error": str(error)},
        )

    counts = Counter(finding["severity"] for finding in findings)
    report = {
        "generated_at": utc_now().isoformat(),
        "account_id": account_id,
        "region": args.region,
        "summary": {
            "high": counts.get("high", 0),
            "medium": counts.get("medium", 0),
            "low": counts.get("low", 0),
            "total": len(findings),
        },
        "findings": findings,
    }

    with open(args.output, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, default=str)

    print(f"Report written to {args.output}")
    print(json.dumps(report["summary"], indent=2))


if __name__ == "__main__":
    main()
