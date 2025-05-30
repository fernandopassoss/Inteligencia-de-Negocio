import os
import time
import csv
import psycopg2
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

time.sleep(10) 

if not client.bucket_exists(bucket):
    client.make_bucket(bucket)

# Conecta ao banco
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
)

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS clientes (id SERIAL PRIMARY KEY, nome TEXT UNIQUE, email TEXT);")
cur.execute("INSERT INTO clientes (nome, email) VALUES ('João', 'joao@exemplo.com') ON CONFLICT (nome) DO NOTHING;") 
conn.commit()

cur.execute("SELECT id, nome, email FROM clientes;") 
rows = cur.fetchall()

file_path = "/tmp/clientes.csv"
with open(file_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "nome", "email"]) 
    writer.writerows(rows)

client.fput_object(bucket, "db/clientes.csv", file_path)
print("Arquivo enviado para raw/db/clientes.csv")

cur.close()
conn.close()