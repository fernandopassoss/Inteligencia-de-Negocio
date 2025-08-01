import requests
import json
from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers='localhost:19090',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

try:
    headers = {
        "Authorization":"Bearer h5BphdNjnWU21ZAnJSjpDF"
    }

    response = requests.get('https://brapi.dev/api/quote/MGLU3',headers=headers)
    response.raise_for_status()  
    data = response.json()

    producer.send('brapi-topic', value=data)

    print("Dados da Magazine Luiza (MGLU3) enviados com sucesso para o tópico 'brapi-topic'!")
    print(data)

except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar a API da Brapi: {e}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    producer.flush()
    producer.close()