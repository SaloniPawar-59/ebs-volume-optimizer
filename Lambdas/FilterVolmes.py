import boto3
import json
from datetime import datetime, date

def convert_datetime(obj):
    if isinstance(obj, (datetime, date)):
        return str(obj)
    elif isinstance(obj, dict):
        return {k: convert_datetime(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_datetime(item) for 
