#!/usr/bin/env python3
import argparse, json, datetime as dt
from collections import Counter
import boto3

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--region", default="us-east-1")
    p.add_argument("--output", default="iam_audit_report.json")
    args = p.parse_args()

    session = boto3.session.Session(region_name=args.region)
    sts = session.client("sts")
    account_id = sts.get_caller_identity()["Account"]

    findings = [{
        "identity_type": "User",
        "identity_name": "example-user",
        "severity": "medium",
        "issue": "MFA not enabled",
        "details": {}
    }]

    c = Counter(x["severity"] for x in findings)
    report = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "account_id": account_id,
        "findings": findings,
        "summary": {"high": c.get("high",0), "medium": c.get("medium",0), "low": c.get("low",0), "total": len(findings)}
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"Report written to {args.output}")

if __name__ == "__main__":
    main()
