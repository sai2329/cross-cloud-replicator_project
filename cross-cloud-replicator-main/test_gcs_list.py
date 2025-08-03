from google.cloud import storage
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

bucket_name = os.getenv("GCS_TARGET_BUCKET")
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# ✅ Check if GCP credentials file exists
if not credentials_path or not os.path.isfile(credentials_path):
    print(f"❌ GCP credentials file not found at: {credentials_path}")
    exit(1)

# ✅ Try connecting to GCS and list files
try:
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    blobs = list(bucket.list_blobs())
    print(f"✅ Files in GCS bucket '{bucket_name}':")

    if not blobs:
        print("⚠️ No files found in the bucket.")
    else:
        for blob in blobs:
            print("-", blob.name)

except Exception as e:
    print(f"❌ GCS error: {e}")
