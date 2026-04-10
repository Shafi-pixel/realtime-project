# 🚀 Real-Time Sales Data Pipeline & Dashboard

A production-style **real-time data engineering project** that simulates streaming sales data, processes it through Kafka, stores it in PostgreSQL, and visualizes it on a live dashboard.

---

## ⚡ Tech Stack

- **Streaming:** Apache Kafka  
- **Backend:** FastAPI (Python)  
- **Database:** PostgreSQL  
- **Dashboard:** Streamlit  
- **Containerization:** Docker & Docker Compose  
- **Cloud:** AWS EC2  

---

## 🧠 Architecture

Producer → Kafka → Consumer → PostgreSQL → FastAPI → Streamlit Dashboard

---

## 🔥 Key Features

- ⚡ Real-time data ingestion using Kafka
- 🧩 Microservices architecture (Producer + Consumer + API)
- 🗄️ Persistent storage with PostgreSQL
- 📊 Live dashboard with auto-refresh
- 🐳 Fully containerized using Docker
- ☁️ Deployed on AWS EC2

---

## 📊 Live Dashboard

👉 http://13.49.78.44:8501  

---

## 🚀 Quick Start (Local Setup)

```bash
git clone https://github.com/Shafi-pixel/realtime-project.git
cd realtime-project
docker-compose up -d
Run dashboard:
Bash
python dashboard.py

📁 Project Structure

realtime-project/
│
├── producer.py        # Kafka Producer
├── consumer.py        # Kafka Consumer
├── api/               # FastAPI Backend
├── db/                # Database connection
├── dashboard.py       # Streamlit UI
├── docker-compose.yml
└── README.md
💡 Learnings
Built end-to-end data pipeline from scratch
Hands-on with Kafka streaming
Docker-based deployment workflow
Real-time system design basics
👨‍💻 Author
Shafi
Aspiring Data Engineer 🚀
