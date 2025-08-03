import os
from dotenv import load_dotenv
from app.s3_client import download_s3_file_stream

# Load environment variables
load_dotenv()

bucket = os.getenv("TEST_S3_BUCKET")
key = os.getenv("TEST_S3_KEY")
local_path = "downloaded_sample.csv"

try:
    print(f"Downloading from S3: s3://{bucket}/{key}")
    s3_stream = download_s3_file_stream(bucket, key)

    with open(local_path, "wb") as f:
        for chunk in iter(lambda: s3_stream.read(4096), b""):
            f.write(chunk)

    print(f"✅ File saved as: {local_path}")
except Exception as e:
    print(f"❌ Error: {e}")
