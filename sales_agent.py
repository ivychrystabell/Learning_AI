import pandas as pd
import matplotlib.pyplot as plt
import io
import streamlit as st
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# --- Load .env file ---
load_dotenv()

def load_sales_data(path: str) -> pd.DataFrame:
    """Membaca file CSV data penjualan."""
    df = pd.read_csv(path)
    # Pastikan kolom tanggal dalam format datetime
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
    return df


def create_sales_agent(df: pd.DataFrame):
    """Membuat Pandas DataFrame Agent dengan model Groq."""
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        st.error("❌ GROQ_API_KEY belum ditemukan di file .env")
        st.stop()

    llm = ChatGroq(
        api_key=groq_api_key,
        model="llama-3.3-70b-versatile",
        temperature=0.2,
    )

    return create_pandas_dataframe_agent(
        llm,
        df,
        verbose=False,
        allow_dangerous_code=True
    )


def generate_chart(df: pd.DataFrame, query: str):
    """Membuat grafik otomatis berdasarkan isi pertanyaan."""
    query_lower = query.lower()
    fig, ax = plt.subplots(figsize=(8, 4))

    # Grafik berdasarkan kategori
    if "category" in query_lower:
        df_grouped = df.groupby("Category")["Sales_Amount"].sum().sort_values(ascending=False).head(10)
        df_grouped.plot(kind="bar", ax=ax)
        ax.set_title("Total Sales by Category")
        ax.set_ylabel("Sales Amount")
        return fig

    # Grafik berdasarkan region
    elif "region" in query_lower:
        df_grouped = df.groupby("Region")["Sales_Amount"].sum().sort_values(ascending=False)
        df_grouped.plot(kind="barh", ax=ax)
        ax.set_title("Sales by Region")
        return fig

    # Grafik tren waktu
    elif "trend" in query_lower or "month" in query_lower or "date" in query_lower or "time" in query_lower:
        df_grouped = df.groupby(df["Date"].dt.to_period("M"))["Sales_Amount"].sum()
        df_grouped.index = df_grouped.index.astype(str)
        df_grouped.plot(kind="line", ax=ax, marker="o")
        ax.set_title("Monthly Sales Trend")
        ax.set_xlabel("Month")
        ax.set_ylabel("Total Sales")
        return fig

    # Grafik berdasarkan customer segment
    elif "segment" in query_lower:
        df_grouped = df.groupby("Customer_Segment")["Sales_Amount"].sum().sort_values(ascending=False)
        df_grouped.plot(kind="bar", ax=ax, color="orange")
        ax.set_title("Sales by Customer Segment")
        return fig

    else:
        return None
