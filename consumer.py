from kafka import KafkaConsumer
import json
from insert_to_db import insert_weather_to_db

consumer = KafkaConsumer("weather_data",
                         bootstrap_servers='kafka:9092',
                         auto_offset_reset='earliest',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    insert_weather_to_db(message.value)
    print("Consumed & inserted:", message.value)
