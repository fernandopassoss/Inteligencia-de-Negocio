import os
import time
from minio import Minio

endpoint = os.getenv("MINIO_ENDPOINT", "localhost:9000")
access_key = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
secret_key = os.getenv("MINIO_SECRET_KEY", "minioadmin")

client = Minio(
    endpoint,
    access_key=access_key,
    secret_key=secret_key,
    secure=False 
)

bucket = "raw"

time.sleep(5) 

if not client.bucket_exists(bucket):
    client.make_bucket(bucket)


file_path = "/data/pessoas.csv"
client.fput_object(bucket, "csv/pessoas.csv", file_path)
print("Arquivo enviado para raw/csv/pessoas.csv")