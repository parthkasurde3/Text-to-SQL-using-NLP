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
- Parses the sentence using a custom NLP pipeline
- Maps user intent to SQL clauses
- Executes queries on a sample SQLite database (`school.db`)
- Displays results in a web-based interface

---

## 📁 Project Structure

```
text-to-sql/
├── app.py                         # Main Flask application
├── setup.py, setup.cfg           # Project setup files
├── Makefile, .travis.yml         # Build and CI configs
├── school.db                     # Sample SQLite database
├── user-system.sql               # SQL schema for database
├── output.json                   # Sample output storage
├── requirements.txt              # Project dependencies
├── README.md                     # Project documentation
│
├── ln2sql/                       # Core logic package
│   ├── __init__.py, main.py      # Entry and routing
│   ├── ln2sql.py                 # NLP to SQL engine
│   ├── parser.py, query.py       # Parsing and query logic
│   ├── column.py, table.py       # DB structure representation
│   ├── stopwordFilter.py         # Stopword processing
│   ├── constants.py, thesaurus.py# Utilities
│   ├── database.py               # DB interaction logic
│   ├── ln2sql_gui.py             # GUI app (optional)
│   ├── database_store/           # DB schema files
│   │   └── school.sql
│   ├── lang_store/               # Language mappings
│   ├── stopwords/                # Stopword lists
│   └── thesaurus_store/          # Thesaurus data files
│
├── static/                       # Web UI assets
│   ├── images/                   # Images for UI
│   └── style.css                 # CSS styles
│
├── templates/                    # HTML templates
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── predict.html
│   └── test.html
│
└── tests/                        # Unit tests
    ├── test_thesaurus.py
    ├── test_unit.py
    └── test_utils.py
```

---

## 🚀 Getting Started

### 📦 Installation

```bash
git clone https://github.com/yourusername/text-to-sql.git
cd text-to-sql
pip install -r requirements.txt
python app.py
```

Visit the app at `http://127.0.0.1:5000/`

---

## ✅ Features

- 🔤 Multilingual stopword support (English, French, more)
- 💬 Fuzzy name matching (e.g., LIKE, starts with)
- 🖼 Clean, responsive web interface
- 🧪 Unit tested backend logic
- 🧠 NLP-driven SQL generation without needing SQL skills

---

## 🧪 Run Tests

```bash
python -m unittest discover tests
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 👏 Credits

Built with ❤️ using Python, Flask, and SQL. Inspired by the need to make databases more accessible for everyone.
