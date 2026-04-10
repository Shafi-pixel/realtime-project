🚀 Real-Time Sales Data Pipeline

📌 Overview

This project is a complete end-to-end real-time data pipeline built using modern data engineering tools.

It simulates live sales data ingestion using Kafka, processes it, stores it in PostgreSQL, and visualizes it using a Streamlit dashboard.

---

🏗️ Architecture

Kafka → Consumer → PostgreSQL → FastAPI → Streamlit Dashboard

---

🛠️ Tech Stack

- Kafka – Real-time data streaming
- FastAPI – Backend API
- PostgreSQL – Database
- Streamlit – Dashboard UI
- Docker – Containerization
- AWS EC2 – Deployment

---

✨ Features

- Real-time data pipeline
- REST API for data access
- Interactive dashboard with filters
- Auto-refresh dashboard
- Deployed on AWS EC2

---

📊 Dashboard Preview

Shows:

- Recent sales data
- Total revenue
- Average price
- Product-wise filtering

---

⚙️ Setup Instructions

1. Clone Repository

git clone https://github.com/YOUR_USERNAME/realtime-sales-pipeline.git
cd realtime-sales-pipeline

2. Install Dependencies

pip install -r requirements.txt

3. Run Docker Services

docker-compose up -d

4. Start Backend

uvicorn api.main:app --host 0.0.0.0 --port 8000

5. Run Dashboard

streamlit run dashboard.py --server.port 8501 --server.address 0.0.0.0

---

🌐 Access

- API: http://<your-ec2-ip>:8000/sales
- Dashboard: http://<your-ec2-ip>:8501

---

👨‍💻 Author

Shafi (Data Engineering Enthusiast)

---

⭐ If you like this project, give it a star!