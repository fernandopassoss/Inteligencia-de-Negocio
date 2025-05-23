FROM python:3.11-slim

WORKDIR /app

RUN pip install minio

COPY upload.py .

CMD ["python", "upload.py"]