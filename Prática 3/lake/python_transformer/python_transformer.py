import os
import time
import io
import pandas as pd
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

bucket_raw = "raw"
bucket_custom = "custom"

time.sleep(10) 

if not client.bucket_exists(bucket_custom):
    client.make_bucket(bucket_custom)

objects = client.list_objects(bucket_raw, recursive=True)

for obj in objects:
    if obj.object_name.endswith(".csv") or obj.object_name.endswith(".json"): 
        print(f"Transformando: {obj.object_name}")
        response = client.get_object(bucket_raw, obj.object_name)
        
       
        if obj.object_name.endswith(".csv"):
            df = pd.read_csv(io.BytesIO(response.read())) 
        elif obj.object_name.endswith(".json"):
            df = pd.read_json(io.BytesIO(response.read()))
        
        df.columns = [col.upper() for col in df.columns]
        
        
        out_name = obj.object_name.replace(f"{bucket_raw}/", "").replace(".json", ".csv") 
        out_csv = df.to_csv(index=False).encode("utf-8")
        
        client.put_object(bucket_custom, out_name, io.BytesIO(out_csv), len(out_csv))
        print(f"Transformado e salvo: {out_name}")
    response.close() 
    response.release_conn()