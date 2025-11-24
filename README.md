🚀 AWS Network Security Analyzer

Serverless AWS solution that analyzes VPC Flow Logs and triggers real-time security alerts using Lambda & SNS.


🔥 Overview

This project monitors AWS VPC network traffic using VPC Flow Logs.
A Lambda function analyzes logs for suspicious activity (denies, unusual ports, repeated failures) and sends alerts via SNS.

Designed for cloud security, network monitoring, and AWS automation.


🏗️ Architecture

VPC Flow Logs → CloudWatch

Lambda Analyzer (Python) processes flow logs

SNS Email Alerts for high-risk traffic

IAM roles for secure, permission-limited access

(Screenshots + architecture diagram included in /docs)


📂 Project Structure
AWS-Network-Security-Analyzer/
│
├── lambda/
│   └── flowlog_analyzer.py
├── docs/
│   ├── architecture_diagram.png
│   ├── flowlogs_screenshot.png
│   └── sns_alert_screenshot.png
├── README.md
├── requirements.txt
└── LICENSE


⚙️ Setup

Enable VPC Flow Logs (send to CloudWatch).

Create SNS Topic → Email Subscription.

Create Lambda Function → Add IAM Role → Add environment variables.

Upload flowlog_analyzer.py.

Test with sample traffic (ACCEPT/REJECT events).


🔐 Security Best Practices

No credentials in code

IAM least-privilege

Environment variables for configuration

Logging + monitoring enabled


🧩 Use Cases

Detect suspicious inbound/outbound activity

Monitor rejected traffic

Automate cloud security notifications

Improve AWS network visibility


⭐ Keywords (SEO)

AWS • VPC • Flow Logs • Cloud Security • Network Monitoring • Lambda • SNS • CloudWatch • Python • Security Automation