from kafka import KafkaConsumer
import json

# Initialize KafkaConsumer

consumer = KafkaConsumer(
    'temperature_sensor_topic', 
    api_version=(3, 8, 0),
    bootstrap_servers='kafka:9092', # Change this if your Kafka broker is running elsewhere
    auto_offset_reset='earliest', # Start reading at the beginning of the topic if no offset is fo
    enable_auto_commit=True,

    group_id='temperature_sensor_topic_group', # Consumer group ID
    value_deserializer=lambda x: json. loads(x.decode('utf-8'))
)

if __name__ == '__main__':
    for message in consumer:
        print(f"Received: {message. value}")