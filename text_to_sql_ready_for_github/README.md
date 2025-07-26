# 🧠 Text to SQL

A Natural Language Processing tool that converts human language queries into SQL queries using Python, SQLite, and a custom parser.

## 🚀 Features

- Multilingual input support (English, French, etc.)
- Built-in GUI interface
- Stopword filtering and thesaurus matching
- Custom SQLite DB (`school.db`) and schema
- Web interface with Flask

## 📂 Structure

- `ln2sql/` — Core NLP and SQL generation logic
- `static/`, `templates/` — Web frontend assets
- `tests/` — Unit testing suite
- `app.py` — Entry point for web interface

## ⚙️ Installation

```bash
pip install -r requirements.txt
python app.py
```

## 🧪 Test

```bash
python -m unittest discover tests
```

## 📷 Preview

![Preview](static/images/result1.png)

## 📄 License

MIT License
