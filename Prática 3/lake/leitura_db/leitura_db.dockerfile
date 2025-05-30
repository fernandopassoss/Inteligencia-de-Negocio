FROM python:3.11-slim
WORKDIR /app
COPY leitura_db.py .
RUN pip install minio psycopg2-binary
CMD ["python", "leitura_db.py"]