from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9093',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = ["Laptop", "Phone", "Tablet", "Headphones"]

while True:
    data = {
        "product": random.choice(products),
        "price": random.randint(100, 2000)
    }

    print(data)
    producer.send("sales", data)
    time.sleep(1)