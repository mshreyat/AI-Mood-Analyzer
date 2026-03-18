# 🧠 AI Mood Analyzer & Screen Time Tracker

An intelligent wellness dashboard that correlates daily emotional states with digital habits using Natural Language Processing (NLP).

## 🌟 Overview
This project is a full-stack data science application designed to help users visualize the relationship between their mental well-being and screen usage. By leveraging **VADER Sentiment Analysis** and **Transformer models**, the app categorizes user journals into emotional insights and tracks them over time.

## 🚀 Key Features
- **Sentiment Analysis:** Real-time NLP processing of text entries to detect Positive, Negative, or Neutral moods.
- **Digital Habit Tracking:** Log daily screen time to monitor digital consumption.
- **Interactive Analytics:** Dynamic data visualization using Plotly/Matplotlib to show mood distribution and trends.
- **Persistent Storage:** Local data persistence using optimized CSV handling via Pandas.
- **Hybrid NLP Engine:** Custom logic to handle modern slang (e.g., "fire", "lit") and idiomatic expressions.

## 🛠️ Tech Stack
- **Language:** Python 3.9+
- **Frontend:** Streamlit (Web Framework)
- **AI/NLP:** VADER, Hugging Face Transformers (RoBERTa)
- **Data Science:** Pandas, NumPy
- **Visualization:** Plotly Express, Matplotlib

## 📂 Project Structure
```text
ai-mood-analyzer/
├── app.py           # Main application entry point & UI logic
├── sentiment.py     # NLP Engine (Sentiment & Emotion classification)
├── storage.py       # Data Persistence Layer (CSV CRUD operations)
├── requirements.txt # Project dependencies
└── data.csv         # Local database for user entries

---

## ⚙️ Installation

```bash
git clone https://github.com/mshreyat/AI-Mood-Analyzer
cd mood-analyzer
pip install -r requirements.txt
````

## ▶️ Run the App

```bash
streamlit run app.py
```

## 📸 Screenshots

(Add screenshots here)

## 🔮 Future Improvements

* Use deep learning (BERT)
* Add real screen time tracking API
* Deploy online

## 👩‍💻 Author

Shreya Malwade







