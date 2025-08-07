import requests
import json
from kafka import KafkaProducer
import time

BRAPI_TOKEN = "h5BphdNjnWU21ZAnJSjpDF"
TICKER = "PETR4"
KAFKA_TOPIC = 'mercado_financeiro'
KAFKA_BROKER = 'kafka:9092'  


def criar_produtor_kafka():
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers=KAFKA_BROKER,
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            print("✅ Conexão com Kafka estabelecida com sucesso.")
            return producer
        except Exception as e:
            print(f"⏳ Kafka não disponível ainda. Tentando novamente em 5 segundos... ({e})")
            time.sleep(5)

producer = criar_produtor_kafka()

def buscar_dados_brapi(ticker, token):
    url = f"https://brapi.dev/api/quote/{ticker}?token={token}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao buscar dados da brapi: {e}")
        return None


if __name__ == '__main__':
    while True:
        dados_acao = buscar_dados_brapi(TICKER, BRAPI_TOKEN)

        if dados_acao and 'results' in dados_acao:
            for resultado in dados_acao['results']:
                print(f"📤 Enviando dados para o Kafka: {resultado}")
                try:
                    future = producer.send(KAFKA_TOPIC, resultado)
                    future.get(timeout=10)
                    print("✅ Dados enviados com sucesso.\n")
                except Exception as e:
                    print(f"⚠️ Erro ao enviar para o Kafka: {e}")
        else:
            print("🚫 Não foi possível obter os dados da ação.")

        time.sleep(5)
