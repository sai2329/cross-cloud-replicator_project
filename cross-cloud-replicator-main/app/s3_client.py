import boto3
import os
from dotenv import load_dotenv
from app.utils import retry_on_network_errors
from botocore.exceptions import BotoCoreError

load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

@retry_on_network_errors
def download_s3_file_stream(bucket_name: str, object_key: str):
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        return response["Body"]  # StreamingBody
    except Exception as e:
        raise RuntimeError(f"S3 Error: {str(e)}")
