from kafka import KafkaConsumer
import json
import time  # não pode esquecer de importar isso!

KAFKA_TOPIC = 'mercado_financeiro'
KAFKA_BROKER = 'kafka:9092'

def criar_consumidor_kafka():
    while True:
        try:
            consumer = KafkaConsumer(
                KAFKA_TOPIC,
                bootstrap_servers=KAFKA_BROKER,
                value_deserializer=lambda v: json.loads(v.decode('utf-8')),
                auto_offset_reset='earliest',
                group_id='grupo_consumidor_financeiro',
                enable_auto_commit=True
            )
            print("conectado ao kafka")
            return consumer
        except Exception as e:
            print(f" erro ({e})")
            time.sleep(5)

consumer = criar_consumidor_kafka()

if __name__ == '__main__':
    for message in consumer:
        try:
            print("Mensagem recebida:")
            print(json.dumps(message.value, indent=2))
        except Exception as e:
            print(f"Erro ao processar mensagem: {e}")

        try:
            time.sleep(5)
        except Exception as e:
            print(f"Erro no delay: {e}")
