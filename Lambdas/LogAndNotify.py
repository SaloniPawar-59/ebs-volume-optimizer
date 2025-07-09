import boto3
from datetime import datetime
def lambda_handler(event, context):
    sns = boto3.client('sns')
    dynamodb = boto3.client('dynamodb')
    
    topic_arn = 'arn:aws:sns:ap-south-1:853542655362:EBSVolumeConvertedTopic'
    table_name = 'EBSVolumeConversionLog'
    
    modified_volumes = event.get('ModifiedVolumes', [])
    timestamp = datetime.utcnow().isoformat()
    
    if not modified_volumes:
        print("No volumes to log or notify.")
        return {"message": "No volumes processed"}

    for vol_id in modified_volumes:
        print(f"Logging to DynamoDB: {vol_id}")
        # DynamoDB Logging
        dynamodb.put_item(
            TableName=table_name,
            Item={
                'VolumeId': {'S': vol_id},
                'Timestamp': {'S': timestamp}
            }
        )

        print(f"Sending SNS for: {vol_id}")
        # SNS Notification
        sns.publish(
            TopicArn=topic_arn,
            Subject='EBS Volume Converted',
            Message=f'Volume {vol_id} has been converted to gp3 at {timestamp}'
        )

    return {"message": "Logged and notified", "volumes": modified_volumes}


