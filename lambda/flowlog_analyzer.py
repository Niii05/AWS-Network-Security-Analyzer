import os
import time
import boto3

# ---------------------------
# Environment variables only
# ---------------------------
LOG_GROUP = os.environ.get('LOG_GROUP')  # No default value
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')  # No default
REJECT_THRESHOLD = int(os.environ.get('REJECT_THRESHOLD', '5'))  # Optional default

# Validate required environment variables
if not LOG_GROUP:
    raise ValueError("Environment variable LOG_GROUP is required.")
if not SNS_TOPIC_ARN:
    raise ValueError("Environment variable SNS_TOPIC_ARN is required.")

# ---------------------------
# AWS clients
# ---------------------------
logs_client = boto3.client('logs')
sns_client = boto3.client('sns')

# ---------------------------
# Function to count ACCEPT/REJECT
# ---------------------------
def count_accept_reject_from_streams(log_group, lookback_seconds=3600):
    now = int(time.time())
    start_time = (now - lookback_seconds) * 1000  # convert to milliseconds
    accept = 0
    reject = 0

    paginator = logs_client.get_paginator('describe_log_streams')
    for page in paginator.paginate(logGroupName=log_group, orderBy='LastEventTime', descending=True):
        for stream in page.get('logStreams', []):
            stream_name = stream['logStreamName']
            events = logs_client.filter_log_events(
                logGroupName=log_group,
                logStreamNames=[stream_name],
                startTime=start_time,
                limit=100
            ).get('events', [])
            for e in events:
                msg = e.get('message', '')
                if 'REJECT' in msg:
                    reject += 1
                elif 'ACCEPT' in msg:
                    accept += 1
    return accept, reject

# ---------------------------
# Lambda handler
# ---------------------------
def lambda_handler(event, context):
    try:
        accept_count, reject_count = count_accept_reject_from_streams(LOG_GROUP)
        summary = f"Flow Log Summary (last 1h): ACCEPT={accept_count}, REJECT={reject_count}"
        print(summary)

        # Send alert if SNS_TOPIC_ARN is set
        if SNS_TOPIC_ARN and reject_count > REJECT_THRESHOLD:
            sns_client.publish(
                TopicArn=SNS_TOPIC_ARN,
                Message=f"ALERT: High REJECT events detected.\n{summary}"
            )

        return {
            'statusCode': 200,
            'body': summary
        }
    except Exception as e:
        print("Error in FlowLogAnalyzer:", str(e))
        raise

