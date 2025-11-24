
# AWS-Network-Security-Analyzer

Automated AWS VPC Flow Log analyzer using Lambda + SNS alerts.

## Overview
This project analyzes VPC Flow Logs in AWS using a Lambda function. Alerts are sent via SNS when suspicious traffic patterns are detected. The goal is to monitor network traffic patterns and get automated notifications for unusual activities.

## Project Structure

- lambda/
  - flowlog_analyzer.py  # Main Lambda function code
- docs/
  - flowlogs_screenshot.png
  - architecture_diagram.png
- README.md
- requirements.txt
- LICENSE

## Setup Instructions

1. Create an S3 bucket to store flow logs.
2. Enable VPC Flow Logs in AWS for your VPCs.
3. Deploy the Lambda function (`flowlog_analyzer.py`) using the AWS Console, CLI, or CloudFormation.
4. Configure an SNS topic for notifications.
5. Update the Lambda environment variables as needed (e.g., bucket name, SNS topic ARN).

## Dependencies

- boto3 (already available in AWS Lambda)
- Add any additional Python packages to `requirements.txt` if needed.

## Security

- **Do NOT** put AWS credentials in the code.  
- Use IAM roles and environment variables for secure access.

## Docs

- Architecture diagram and screenshots are stored in the `docs/` folder.
