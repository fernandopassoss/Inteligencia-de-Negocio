import requests
import json
import time
from kafka import KafkaProducer

TOKEN_BRAPI = "h5BphdNjnWU21ZAnJSjpDF" 
TICKERS = "ITUB4,BBDC4" 
KAFKA_BOOTSTRAP_SERVERS = 'kafka:9092' 
KAFKA_TOPIC = 'acoes_topic'

try:
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        api_version=(3, 8, 0),
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        key_serializer=lambda k: k.encode('utf-8')
    )
except Exception as e:
    print(f" Erro ao conectar com o Kafka: {e}")
    exit()


def buscar_dados_de_acoes(tickers_list, token):
    url = f"https://brapi.dev/api/quote/{tickers_list}"
    headers={"Authorization": f"Bearer {token}"},
    print(f"Buscando dados para: {tickers_list}...")
    try:
        response = requests.get(url)
        # Lança uma exceção se a resposta da API for um erro (ex: 401 Unauthorized, 404, 500)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao buscar dados na brapi: {e}")
        return None

if __name__ == '__main__':
    print(f"✅ Iniciando produtor Kafka. Enviando dados para o tópico '{KAFKA_TOPIC}'...")
    while True: 
        # Chama a função para buscar os dados das ações definidas em TICKERS
        dados = buscar_dados_de_acoes(TICKERS, TOKEN_BRAPI)
        
        # A API retorna uma chave 'results' que contém uma lista com os dados de cada ação
        if dados and 'results' in dados:
            # 👉 CORREÇÃO: Itera sobre cada resultado (cada ação) na lista
            for dados_da_acao in dados['results']:
        
                key = dados_da_acao['symbol']
                
                # Envia a mensagem para o tópico do Kafka
                producer.send(KAFKA_TOPIC, key=key, value=dados_da_acao)
                print(f"  - Dados de '{key}' enviados com sucesso!")
            
            # Limpa o buffer para garantir o envio de todas as mensagens do loop
            producer.flush() 
        
        # Espera 30 segundos antes da próxima busca para não sobrecarregar a API
        print("\nAguardando 30 segundos para a próxima busca...")
        time.sleep(60)