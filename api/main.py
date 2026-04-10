from fastapi import FastAPI
from db.db import get_connection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Kafka Streaming API Running"}

@app.get("/sales")
def get_sales():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM sales ORDER BY id DESC LIMIT 10")
    rows = cur.fetchall()

    return rows

@app.get("/sales/total")
def total_sales():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT SUM(price) FROM sales")
    total = cur.fetchone()

    return {"total_sales": total[0]}