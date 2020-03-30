
from datetime import datetime
import boto3
import random
# # Create  cloudWatch client
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

value = float(random.randint(1, 10))

# Put custom metrics
cloudwatch.put_metric_data(
    MetricData=[
        {
            'MetricName': 'PAGES_VISITED',
            'Dimensions': [
                {
                    'Name': 'UNIQUE_PAGES',
                    'Value': 'URLS'
                },
            ],
            'Unit': 'None',
            'Value': value
        },
    ],
    Namespace='SITE/TRAFFIC'
)

# crontab for every minute to call script
# * * * * * python3 / home/ec2-user/put_custom_metric.py >> cron.log 2 > &1
