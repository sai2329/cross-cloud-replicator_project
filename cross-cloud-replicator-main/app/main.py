from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import threading
import time
import webbrowser

from app.s3_client import download_s3_file_stream
from app.gcs_client import upload_stream_to_gcs, file_exists_in_gcs

# Load environment variables
load_dotenv()

app = FastAPI()

# Auto-open docs in default browser (in a thread, to not block FastAPI)
def open_browser():
    time.sleep(1)  # Delay to ensure server has started
    webbrowser.open("http://127.0.0.1:8000/docs")

# Start the browser opener in a background thread
threading.Thread(target=open_browser).start()

# Request schema
class ReplicationRequest(BaseModel):
    s3_bucket: str
    s3_key: str

# Root endpoint
@app.get("/")
async def root():
    return {"message": "FastAPI is running. Visit /docs for API documentation."}

# Replication endpoint
@app.post("/v1/replicate")
async def replicate_file(request_data: ReplicationRequest):
    try:
        s3_bucket = request_data.s3_bucket
        s3_key = request_data.s3_key
        target_blob_name = s3_key

        if file_exists_in_gcs(target_blob_name):
            return {"status": "skipped", "message": "File already exists in GCS."}

        s3_stream = download_s3_file_stream(s3_bucket, s3_key)
        upload_stream_to_gcs(target_blob_name, s3_stream)

        return {"status": "success", "message": "File replicated to GCS."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"S3/GCS Error: {str(e)}")
