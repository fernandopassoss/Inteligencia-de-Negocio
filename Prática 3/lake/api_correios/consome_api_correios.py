import os
import time
import json
import requests
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

response = requests.get("https://viacep.com.br/ws/63708825/json/")
cep_data = response.json()

file_path = "/tmp/cep.json"

with open(file_path, "w") as f:
    json.dump(cep_data, f)

client.fput_object(bucket, "api_correios/cep.json", file_path)
print("Arquivo enviado para raw/api_correios/cep.json")