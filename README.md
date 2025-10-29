# 📊 Sales Data Assistant (Final Project)

This project is a **Streamlit dashboard** that enables users to analyze and explore sales data interactively using **Groq API + LangChain Pandas DataFrame Agent**.  
It is designed as part of a **final project** to demonstrate how natural language can be used to interact with structured sales data.

---

## 🚀 Features

- 🧠 **Ask questions in natural language** (e.g., “Which region had the highest sales in 2024?”)  
- 📈 **Automatic visualizations** for common questions (sales by month, category, or region)  
- 🔍 **Interactive filters** in the sidebar for date, region, and category  
- 📂 **CSV upload support** — users can analyze their own sales data  
- 🤖 Powered by **Groq LLM + LangChain Pandas Agent**

---

## 🧩 Tech Stack

| Component | Description |
|------------|--------------|
| **Language** | Python 3.12 |
| **Framework** | Streamlit |
| **AI Model** | Groq (via LangChain integration) |
| **Libraries** | pandas, matplotlib, langchain, langchain_experimental, python-dotenv |

---

## ⚙️ Setup & Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ivychrystabell/Learning_AI.git
cd Learning_AI
```

### 2️⃣ Create a virtual environment
```bash
python -m venv myenv
source myenv/bin/activate      # macOS / Linux
myenv\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add your Groq API key  
Create a file named `.env` in the project folder and add:
```
GROQ_API_KEY=your_api_key_here
```

### 5️⃣ Run the app
```bash
streamlit run app.py
```

After running, open your browser at:  
👉 [http://localhost:8501](http://localhost:8501)

---

## ☁️ Deployment on Streamlit Cloud

1. Push your project to GitHub (include all files except `.env`).  
2. Go to [Streamlit Cloud](https://share.streamlit.io).  
3. Click **"New App" → Select your GitHub repo → Choose `app.py`**.  
4. Click **Deploy**.  
5. Your app will be live at a public URL (e.g. `https://your-app-name.streamlit.app/`).

---

## 🧾 Dataset

The project uses a **synthetic sales dataset (`sales.csv`)** generated for demonstration purposes.  
It contains **500 rows** of transactions from January to December 2024 with the following columns:

| Column | Description |
|---------|-------------|
| `Order_ID` | Unique transaction ID |
| `Date` | Transaction date |
| `Product` | Name of the sold product |
| `Category` | Product category |
| `Region` | Sales region (North, South, East, West) |
| `Sales_Amount` | Total sale amount (after discount) |
| `Quantity` | Number of units sold |
| `Unit_Price` | Price per unit |
| `Discount` | Discount applied |
| `Customer_Segment` | Segment (Consumer, Home Office, Corporate) |

---

## 💡 Example Questions

You can try these in the app:
- “What was the total sales in 2024?”
- “Which region had the highest total sales?”
- “Show average discount per category.”
- “How many products were sold in the South region?”
- “Plot sales trend by month.”

---

## 👩‍💻 Author

**Ivy Ivenna Chrystabell**  
FH Dortmund — Informatik Data Science Student  
📍 Based in Dortmund, Germany  

---

## 🧠 Acknowledgements

- [LangChain Documentation](https://python.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Groq API](https://groq.com/)
