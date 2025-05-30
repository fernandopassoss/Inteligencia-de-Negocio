FROM python:3.11-slim
COPY consome_api_correios.py .
WORKDIR /app
RUN pip install minio requests
CMD ["python", "consome_api_correios.py"]