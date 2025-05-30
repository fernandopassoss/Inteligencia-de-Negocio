FROM python:3.11-slim
WORKDIR /app
COPY leitura_csv.py .
RUN pip install minio
CMD ["python", "leitura_csv.py"]