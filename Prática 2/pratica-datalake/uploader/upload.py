import os
import time
from minio import Minio
from minio.error import S3Error

# Configurações do cliente MinIO (inalteradas)
endpoint = os.getenv("MINIO_ENDPOINT", "localhost:9000")
access_key = os.getenv("MINIO_ACCESS_KEY", "minioadmin")
secret_key = os.getenv("MINIO_SECRET_KEY", "minioadmin")

client = Minio(
    endpoint,
    access_key=access_key,
    secret_key=secret_key,
    secure=False  # Mantido como False, conforme o original, para conexões HTTP
)

# Nome do bucket (inalterado)
bucket_name = "raw" # (implícito pelo uso em todo o exercício)

# --- MODIFICAÇÃO PRINCIPAL AQUI ---
# Pega o caminho do arquivo e o nome do objeto das variáveis de ambiente.
# Se as variáveis não estiverem definidas, ele usa os valores originais
# para manter a compatibilidade com o upload do 'example.txt'.
file_to_upload_path = os.getenv("UPLOAD_FILE_PATH", "/app/data/example.txt")
object_name_in_bucket = os.getenv("UPLOAD_OBJECT_NAME", os.path.basename(file_to_upload_path))
# --- FIM DA MODIFICAÇÃO PRINCIPAL ---

# Aumentar o tempo de espera pode ser útil se o MinIO demorar para iniciar,
# mas a diretiva 'depends_on' com 'healthcheck' no docker-compose.yml é a forma mais robusta.
print(f"Aguardando um momento para garantir que os serviços estejam prontos (sleep)...")
time.sleep(10) # O original tinha 5 segundos, pode ser ajustado conforme necessário.

print(f"Verificando/Criando bucket: {bucket_name}")
if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)
    print(f"Bucket '{bucket_name}' criado.")
else:
    print(f"Bucket '{bucket_name}' ja existe.")

print(f"Tentando enviar o arquivo: '{file_to_upload_path}'")
print(f"Como objeto: '{object_name_in_bucket}' para o bucket '{bucket_name}'")

try:
    # Verifica se o arquivo de fato existe no caminho esperado DENTRO do container uploader
    if not os.path.exists(file_to_upload_path):
        print(f"ERRO: Arquivo '{file_to_upload_path}' não encontrado no container uploader.")
        print(f"Verifique os volumes no docker-compose.yml e o caminho de saída no script gerador.")
        # Considerar sair com erro se o arquivo não for encontrado
        # import sys
        # sys.exit(1)
    else:
        client.fput_object(bucket_name, object_name_in_bucket, file_to_upload_path) # Usa as novas variáveis
        print(f"Arquivo '{object_name_in_bucket}' enviado com sucesso para o bucket '{bucket_name}'.")
except S3Error as err:
    print(f"Erro S3 no upload: {err}")
except Exception as e:
    print(f"Ocorreu uma exceção geral durante o upload: {e}")