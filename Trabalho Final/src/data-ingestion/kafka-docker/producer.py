import requests
import json
from kafka import KafkaProducer
import time


BRAPI_TOKEN = "h5BphdNjnWU21ZAnJSjpDF"
TICKER = "PETR4"
KAFKA_TOPIC = 'mercado_financeiro'


producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def buscar_dados_brapi(ticker, token):
    url = f"https://brapi.dev/api/quote/{ticker}?token={token}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para respostas com erro
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados da brapi: {e}")
        return None
    
if __name__ == '__main__':
    while True:
        dados_acao = buscar_dados_brapi(TICKER, BRAPI_TOKEN)

        if dados_acao and 'results' in dados_acao:
            for resultado in dados_acao['results']:
                print(f"Enviando dados para o Kafka: {resultado}")
                producer.send(KAFKA_TOPIC, resultado)
                producer.flush()
        else:
            print("Não foi possível obter os dados da ação.")

        time.sleep(5)