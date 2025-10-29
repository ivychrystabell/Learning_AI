import streamlit as st
import pandas as pd
import plotly.express as px
from sales_agent import load_sales_data, create_sales_agent, generate_chart

# --- Konfigurasi halaman
st.set_page_config(page_title="Sales Data Analyst", page_icon="📈", layout="wide")

st.title("📊 Sales Data Analyst (Groq + Pandas Agent)")
st.markdown("Gunakan asisten ini untuk menganalisis data penjualanmu secara interaktif 💬")

uploaded_file = st.file_uploader("📂 Upload file CSV data penjualan", type=["csv"])

if uploaded_file:
    # --- Load data
    df = pd.read_csv(uploaded_file)
    df["Date"] = pd.to_datetime(df["Date"])

    st.subheader("📄 Preview Data")
    st.dataframe(df.head(), use_container_width=True)

    # --- Statistik ringkas
    st.subheader("📈 Ringkasan Data")

    total_sales = df["Sales_Amount"].sum()
    total_orders = len(df)
    top_product = df.groupby("Product")["Sales_Amount"].sum().idxmax()
    top_region = df.groupby("Region")["Sales_Amount"].sum().idxmax()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Sales", f"€{total_sales:,.2f}")
    col2.metric("Total Orders", f"{total_orders}")
    col3.metric("Top Product", top_product)
    col4.metric("Top Region", top_region)

    # --- Sidebar Filter
    st.sidebar.header("🧭 Filter Data")
    selected_region = st.sidebar.multiselect("Pilih Region", df["Region"].unique())
    selected_category = st.sidebar.multiselect("Pilih Kategori", df["Category"].unique())

    filtered_df = df.copy()
    if selected_region:
        filtered_df = filtered_df[filtered_df["Region"].isin(selected_region)]
    if selected_category:
        filtered_df = filtered_df[filtered_df["Category"].isin(selected_category)]

    # --- Visualisasi dasar
    st.subheader("📊 Visualisasi Data")

    tab1, tab2 = st.tabs(["Tren Penjualan per Bulan", "Kontribusi Produk"])

    with tab1:
        df["Date"] = pd.to_datetime(df["Date"])
        monthly_sales = (
            filtered_df.groupby(filtered_df["Date"].dt.to_period("M"))["Sales_Amount"]
            .sum()
            .reset_index()
        )
        monthly_sales["Date"] = monthly_sales["Date"].astype(str)

        fig1 = px.line(
            monthly_sales,
            x="Date",
            y="Sales_Amount",
            title="Total Sales per Month",
            markers=True,
        )
        st.plotly_chart(fig1, use_container_width=True)

    with tab2:
        fig2 = px.bar(
            filtered_df.groupby("Product")["Sales_Amount"].sum().reset_index(),
            x="Product",
            y="Sales_Amount",
            title="Sales per Product",
            color="Product",
        )
        st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    # --- Bagian interaktif LLM
    st.subheader("💬 Tanya Asisten Data")
    st.markdown("Contoh: *'Produk mana yang paling banyak terjual di region South?'*")

    question = st.text_input("Pertanyaan:")
    analyze_btn = st.button("🔍 Cari jawaban")

    if analyze_btn:
        if question.strip():
            # Buat agent dari data
            agent = create_sales_agent(df)
            with st.spinner("Sedang menganalisis..."):
                try:
                    result = agent.run(question)
                    st.success("✅ Jawaban Asisten:")
                    st.write(result)

                    # Grafik otomatis jika cocok
                    fig = generate_chart(df, question)
                    if fig:
                        st.pyplot(fig)
                except Exception as e:
                    st.error(f"Terjadi error: {e}")
        else:
            st.warning("Silakan isi pertanyaan terlebih dahulu.")
else:
    st.info("⬆️ Upload data penjualan dalam format CSV untuk memulai analisis.")