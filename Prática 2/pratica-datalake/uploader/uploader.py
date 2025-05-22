import os
import time
from minio import Minio
from minio.error import S3Error

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
file_path = "/app/data/example.txt"
object_name = os.path.basename(file_path)

time.sleep(5)

if not client.bucket_exists(bucket):
    client.make_bucket(bucket) # Cria o bucket se nao existir
    print(f"Bucket '{bucket}' criado.")
else:
    print(f"Bucket '{bucket}' ja existe.")


try: # Envia o arquivo
    client.fput_object(bucket, object_name, file_path)
    print(f"Arquivo '{object_name}' enviado para '{bucket}/'.")
except S3Error as err:
    print("Erro no upload:", err)   