import streamlit as st
import requests
import pandas as pd
import time

# ------------------ CONFIG ------------------
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Real-Time Dashboard", layout="wide")

# ------------------ SIDEBAR ------------------
st.sidebar.title("Settings")

refresh_rate = st.sidebar.slider(
    "Refresh Rate (seconds)", 
    min_value=1, 
    max_value=10, 
    value=2
)

product_filter = st.sidebar.selectbox(
    "Filter by Product",
    ["All", "Laptop", "Phone", "Tablet", "Headphones"]
)

# ------------------ TITLE ------------------
st.title("Real-Time Sales Dashboard")

# ------------------ AUTO REFRESH ------------------
placeholder = st.empty()

while True:
    try:
        # -------- FETCH SALES DATA --------
        sales_response = requests.get(f"{API_URL}/sales")
        total_response = requests.get(f"{API_URL}/sales/total")

        if sales_response.status_code != 200:
            st.error("Failed to fetch sales data")
            break

        data = sales_response.json()

        # -------- DATAFRAME --------
        df = pd.DataFrame(data)

        # -------- COLUMN FIX --------
        # Handle different backend naming
        if "product" not in df.columns:
            if "product_name" in df.columns:
                df["product"] = df["product_name"]

        if "price" not in df.columns:
            if "amount" in df.columns:
                df["price"] = df["amount"]

        # -------- FILTER --------
        if "product" in df.columns and product_filter != "All":
            df = df[df["product"] == product_filter]

        # -------- DISPLAY --------
        with placeholder.container():

            col1, col2 = st.columns([3, 1])

            with col1:
                st.subheader("Recent Sales")
                st.dataframe(df.tail(10), use_container_width=True)

            with col2:
                st.subheader("Metrics")

                # Total Sales
                if total_response.status_code == 200:
                    total_sales = total_response.json().get("total_sales", 0)
                else:
                    total_sales = 0

                st.metric("Total Revenue", total_sales)

                # Average Price
                if "price" in df.columns and not df.empty:
                    avg_price = round(df["price"].mean(), 2)
                else:
                    avg_price = 0

                st.metric("Average Price", avg_price)

                # Total Records
                st.metric("Total Records", len(df))

    except Exception as e:
        st.error(f"Error: {e}")

    time.sleep(refresh_rate)