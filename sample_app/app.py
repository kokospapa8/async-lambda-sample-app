import boto3
import os
import requests

def lambda_handler(event, context):
    image_url = event['image_url']
    S3_BUCKET_PARAM = os.environ['S3_BUCKET_PARAM']

    # download

    image = requests.get(image_url).content


    ssm_client = boto3.client('ssm', region_name="ap-northeast-2")
    response = ssm_client.get_parameter(
        Name=S3_BUCKET_PARAM,
        WithDecryption=True
    )
    bucket_name = response['Parameter']['Value']

    s3_client = boto3.client('s3', region_name="ap-northeast-2")
    response = s3_client.put_object(
        Bucket=bucket_name,
        Key="image.png",
        Body=image
    )

    return response
