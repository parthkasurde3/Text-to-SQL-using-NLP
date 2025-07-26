# 🧠 LN2SQL – Natural Language to SQL Converter

LN2SQL is an NLP-powered tool that converts everyday spoken or written language into structured SQL queries. It's designed to help users explore databases intuitively, without needing SQL expertise.

---

## 🎤 Sample Input Queries

Try out queries like:

- What is the **average age** of students?
- Show me the list of students whose **age is greater than 21**
- Display students whose **name starts with the letter "E"**
- List students whose age is **20**
- Find students whose name is **like "Mahi"**
- How many students are enrolled in **each class?**
- Show the **professor list**
- What is the **total number of students?**
- Which students have the **same first name** but are in **different classes?**
- What is the **total number of classes** taught by each professor?

---

## 🧠 How It Works

- Accepts user input in natural language
- Processes language structure and intent
- Uses a custom parser and thesaurus for matching
- Converts input to a valid SQL query
- Executes query on the sample database (`school.db`)

---

## 📂 Project Structure

```
ln2sql/                 → Core engine (parser, query builder)
static/, templates/     → Flask frontend assets
school.db               → Sample database
tests/                  → Unit tests
app.py                  → Entry point for the web app
```

---

## 🚀 Getting Started

### 🔧 Requirements
- Python 3.8+
- Flask
- SQLAlchemy (if extending)
- nltk

### 📦 Installation

```bash
git clone https://github.com/yourusername/text-to-sql.git
cd text-to-sql
pip install -r requirements.txt
python app.py
```

The app will launch locally on `http://127.0.0.1:5000/`

---

## ✅ Features

- 🔤 Multilingual stopword support (English, French, more)
- 💬 Fuzzy name matching (e.g., starts with, like)
- 🖼 Web-based interface
- 🧪 Unit tested modules

---

## 🧪 Running Tests

```bash
python -m unittest discover tests
```

---

## 📄 License

MIT License – use freely with attribution.

---

## 👏 Credits

This project is inspired by the idea of bridging the gap between non-technical users and databases. Built with ❤️ using Python and Flask.
