# 🧠 Competitor Analyzer AI

This AI-powered tool helps you identify and rank the top 5 competitors based on your service description and keywords. It performs live Google searches, scrapes relevant websites, and applies NLP-based semantic similarity to return the most similar competitor companies.

---

## 🚀 Features

- 🔍 Accepts user description and keywords
- 🌐 Searches live competitor websites via Google (Serper API)
- 🧽 Scrapes company service data from websites
- 🧠 Uses `SentenceTransformer` for semantic embeddings
- 📊 Ranks competitors based on similarity
- 📥 Option to export top 5 results as CSV (Streamlit UI)

---

## 🧰 Tech Stack

- Python
- Streamlit (for interactive UI)
- `sentence-transformers` for embeddings
- `scikit-learn` for cosine similarity
- `requests` + `BeautifulSoup` for scraping
- Serper.dev for Google search API

---

## 📦 Installation

```bash
git clone https://github.com/your-username/competitor-analyzer-ai.git
cd competitor-analyzer-ai
pip install -r requirements.txt

