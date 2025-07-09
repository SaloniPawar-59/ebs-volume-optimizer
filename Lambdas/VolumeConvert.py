import boto3
import json
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    modified_volumes = []
    for vol in event['Volumes']:
        vol_id = vol['VolumeId']
        ec2.modify_volume(VolumeId=vol_id, VolumeType='gp3')
        modified_volumes.append(vol_id)
    return {'ModifiedVolumes': modified_volumes}
