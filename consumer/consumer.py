from kafka import KafkaConsumer
import json
from db.db import get_connection

consumer = KafkaConsumer(
    'sales',
    bootstrap_servers='localhost:9093',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

conn = get_connection()
cur = conn.cursor()

for message in consumer:
    data = message.value
    print(f"Received: {data}")

    try:
        cur.execute(
            "INSERT INTO sales (product, price) VALUES (%s, %s)",
            (data['product'], data['price'])
        )
        conn.commit()
        print("Inserted into DB ✅")

    except Exception as e:
        print("Error:", e)
        conn.rollback()