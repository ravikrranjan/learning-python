from datetime import datetime
import boto3
import random
# # Create  cloudWatch client
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')

# Genearte random value
value = float(random.randint(10, 100))

print(value)

# put custom metric
response = cloudwatch.put_metric_data(
    MetricData=[
        {
            'MetricName': 'Zax',
            'Dimensions': [
                {
                    'Name': 'VERIFY_APP',
                    'Value': 'Dihuli'
                },
                {
                    'Name': 'APP_VERSION',
                    'Value': '0.1'
                },
            ],
            'Timestamp': datetime.now(),
            'Unit': 'None',
            'Value': value
        },
    ],
    Namespace='ZAXApp'
)
print(response)
