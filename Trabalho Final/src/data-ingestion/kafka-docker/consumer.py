from kafka import KafkaConsumer
import json


KAFKA_TOPIC = 'mercado_financeiro'
KAFKA_BROKER = 'kafka:9092'

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',  # pega desde o início do tópico
    group_id='grupo_consumidor_financeiro',  # necessário pra Kafka controlar o offset
    enable_auto_commit=True
)

if __name__ == '__main__':
    for message in consumer:
        print(f"Received: {message.value}")