# import logging
# logging.basicConfig(level=logging.INFO)

from kafka import KafkaProducer
from faker import Faker
import time
import json
import random

# Initialize Faker and KafkaProducer

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='kafka: 9092',
    api_version=(3, 8, 0),
    value_serializer=lambda v: json.dumps(v).encode('utf-8'), # Serializar a mensagem para JSON
    key_serializer=lambda k: k.encode('utf-8') # Serializar a mensagem para JSON

)

def generate_temperature_data():
    return {
    'sensor_id': str(random. randint(1, 50)), # Unique ID for the sensor
    'temperature': round(random.uniform(-10.0, 40.0), 2), # Random temperature between -10℃ an
    'timestamp': fake.date_time().isoformat() # Timestamp of the reading
    }

if __name__ == '__main__':
    topic = 'temperature_sensor_topic'

while True: 
    data = generate_temperature_data()
    key = data['sensor_id' ] # Use the 'sensor_id' as the key
    producer.send(topic, key=key, value=data) # Send both key and value
    time. sleep(1) # Send a message every second

