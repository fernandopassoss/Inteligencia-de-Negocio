from kafka import KafkaConsumer
import json

# Initialize KafkaConsumer

consumer = KafkaConsumer(
    'temperature_sensor_topic', 
    bootstrap_servers='kafka:9092', 
    auto_offset_reset='earliest',
    enable_auto_commit=True,

    group_id='temperature_sensor_topic_group', # Consumer group ID
    value_deserializer=lambda x: json. loads(x.decode('utf-8'))
)

if __name__ == '__main__':
    for message in consumer:
        print(f"Received: {message. value}")