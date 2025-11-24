# AWS-Network-Security-Analyzer
Automated AWS VPC Flow Log analyzer using Lambda + SNS alerts.

## Project Structure
## Overview
This project analyzes VPC Flow Logs in AWS using a Lambda function. Alerts are sent via SNS when suspicious traffic patterns are detected.

## Project Structure
- lambda/
  - flowlog_analyzer.py
- docs/
  - flowlogs_screenshot.png
  - architecture_diagram.png
- README.md
- requirements.txt
- LICENSE

## Setup Instructions
1. Create an S3 bucket to store flow logs.
2. Enable VPC Flow Logs in AWS for your VPCs.
3. Deploy the Lambda function (`flowlog_analyzer.py`) using your preferred method (Console, CLI, or CloudFormation).
4. Configure an SNS topic for notifications.
5. Update the Lambda environment variables as needed.

## Dependencies
- boto3 (already available in AWS Lambda)
- Add any additional packages to `requirements.txt` if used

## Security
- Do NOT put AWS credentials in the code.  
- Use IAM roles and environment variables for access.

## Docs
- Architecture diagram and screenshots are in `docs/` folder.

