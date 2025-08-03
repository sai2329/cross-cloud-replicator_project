from google.cloud import storage
import os
from io import BytesIO

from app.utils import retry_on_network_errors

# Get bucket name from environment variable
GCS_BUCKET_NAME = os.getenv("GCS_TARGET_BUCKET")
if not GCS_BUCKET_NAME:
    raise ValueError("Missing environment variable: GCS_TARGET_BUCKET")

# Connect to GCS
gcs_client = storage.Client()
gcs_bucket = gcs_client.bucket(GCS_BUCKET_NAME)

def file_exists_in_gcs(blob_name: str) -> bool:
    """Check if a blob already exists in the target GCS bucket."""
    blob = gcs_bucket.blob(blob_name)
    return blob.exists()

@retry_on_network_errors
def upload_stream_to_gcs(blob_name: str, stream_data):
    """
    Upload a file-like stream to GCS under the given blob name.
    Converts non-seekable stream to BytesIO buffer.
    """
    # Read entire stream into a seekable buffer
    buffer = BytesIO(stream_data.read())
    buffer.seek(0)

    blob = gcs_bucket.blob(blob_name)
    blob.upload_from_file(buffer)
    return True
