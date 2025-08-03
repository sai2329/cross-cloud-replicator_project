# cross-cloud-replicator
Assignment - Event-driven file replication from AWS S3 to GCS

please refer- Project Working Steps..pdf (use powershell or commad prompt all commonds show in a pdf refer it.

click on info and go to main in this branch have all code.

All project zip file download through this link --> https://drive.google.com/file/d/1XakNSLYmA2RUesWUIHVW18kTLzOEqiJu/view?usp=sharing


# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app.main:app --reload

How to Trigger Replication

curl -X POST http://127.0.0.1:8000/v1/replicate \
  -H "Content-Type: application/json" \
  -d '{"s3_bucket": "my-test-bucket-saideep-2025", "s3_key": "sample.csv"}'


 Sequence Diagram

Client --> FastAPI --> S3 Download (boto3)
                           ↓
                  Upload to GCS (google-cloud-storage)
                           ↓
                 Return Success/Failure
