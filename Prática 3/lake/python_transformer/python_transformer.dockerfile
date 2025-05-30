FROM python:3.11-slim
WORKDIR /app
COPY python_transformer.py .
RUN pip install minio pandas
CMD ["python", "python_transformer.py"]