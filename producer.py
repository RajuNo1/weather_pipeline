from kafka import KafkaProducer
import json
import time
from fetch_weather import fetch_weather_data

producer = KafkaProducer(bootstrap_servers='kafka:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    data = fetch_weather_data("Bangalore", "YOUR_API_KEY")
    producer.send("weather_data", value=data)
    print("Produced:", data)
    time.sleep(300)
