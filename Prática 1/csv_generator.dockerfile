FROM python:3.9-slim
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir pandas numpy
CMD ["python", "generate_csv.py"]