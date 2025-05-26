# generator/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instala as bibliotecas Python necessárias
# numpy é usado no script para gerar dados mais variados
RUN pip install --no-cache-dir pandas pyarrow numpy

COPY generate_and_convert.py .

# O script Python será executado quando o container iniciar.
# Ele irá gerar os arquivos no volume montado e então o container finalizará.
CMD ["python", "generate_and_convert.py"]