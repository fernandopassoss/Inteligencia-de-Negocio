import requests
import json
from kafka import KafkaProducer
import time

# --- Configurações ---
# Substitua pelo seu token da brapi
BRAPI_TOKEN = "h5BphdNjnWU21ZAnJSjpDF"
# O ticker da ação que você quer consultar
TICKER = "PETR4"
# Tópico do Kafka para onde os dados serão enviados
KAFKA_TOPIC = 'mercado_financeiro'

# --- Inicializa o produtor Kafka ---
producer = KafkaProducer(
    bootstrap_servers='kafka: 9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def buscar_dados_brapi(ticker, token):
    """
    Busca os dados de uma ação na API da brapi.
    """
    url = f"https://brapi.dev/api/quote/{ticker}?token={token}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para respostas com erro
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados da brapi: {e}")
        return None

# --- Loop para buscar e enviar dados ---
while True:
    dados_acao = buscar_dados_brapi(TICKER, BRAPI_TOKEN)

    if dados_acao and 'results' in dados_acao:
        for resultado in dados_acao['results']:
            print(f"Enviando dados para o Kafka: {resultado}")
            producer.send(KAFKA_TOPIC, resultado)
            producer.flush() # Garante que as mensagens sejam enviadas
    else:
        print("Não foi possível obter os dados da ação.")

    # Espera 60 segundos antes da próxima busca
    time.sleep(60)