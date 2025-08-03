 # Clone the repo
git clone <your-private-repo>

# Set up virtual env
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Set environment
cp .env.example .env  # or manually set AWS/GCP envs

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



