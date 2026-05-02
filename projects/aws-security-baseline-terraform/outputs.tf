output "security_log_bucket_name" {
  value = aws_s3_bucket.security_logs.bucket
}

output "guardduty_detector_id" {
  value = aws_guardduty_detector.main.id
}
