# 📂 Smart AI Document Vault

An AI-powered Document Management System built using **Python**, **Streamlit**, **Machine Learning**, and **Natural Language Processing (NLP)**. The application automatically extracts text from documents, classifies them into categories, generates AI summaries, and enables semantic search using natural language.

## 🚀 Live Demo

🔗 https://smart-ai-document-vault-gz3zgmjdyfpbzocewannwk.streamlit.app/

## 📸 Screenshots

<img width="1300" height="649" alt="image" src="https://github.com/user-attachments/assets/53457c17-4f37-4998-bac0-776ee2ac622e" />


---

# ✨ Features

### 📄 OCR Text Extraction
- Extracts text from PDF and image documents.
- Supports PDF, JPG, JPEG and PNG files.

### 🤖 Machine Learning Document Classification
Automatically classifies uploaded documents into:
- 📚 Academic
- 💼 Professional
- 🏆 Achievement
- 📄 Other

### 📝 AI Document Summarization
Uses NLP to generate concise summaries of lengthy documents.

### 🔍 Semantic Search
Search documents using natural language instead of exact filenames.

Example:

> "Show my internship certificates"

> "Find my resume"

> "Academic documents"

### 📊 Interactive Dashboard
Displays:
- Total Documents
- Academic Documents
- Professional Documents
- Achievement Documents
- Other Documents

### 💾 SQLite Database
Stores:
- Filename
- Category
- Upload Date
- File Path
- OCR Text
- AI Summary

### 🌐 Web Interface
Built using Streamlit with:
- Dashboard
- Upload Page
- Search Page
- Documents Page

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Web Application |
| SQLite | Database |
| Scikit-learn | Machine Learning |
| Sentence Transformers | Semantic Search |
| Sumy | NLP Summarization |
| Pytesseract | OCR |
| Pandas | Data Processing |

---

# 📁 Project Structure

```
Smart-AI-Document-Vault
│
├── app.py
├── database.py
├── ml_classifier.py
├── ocr.py
├── summarizer.py
├── semantic_search.py
├── requirements.txt
├── README.md
│
├── database/
│   └── documents.db
│
└── uploads/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Nasreen-15/Smart-AI-Document-Vault.git
```

Move into the project folder

```bash
cd Smart-AI-Document-Vault
```

Install dependencies

```bash
pip install -r requirements.txt
```

Initialize the database

```bash
python database.py
```

Run the application

```bash
streamlit run app.py
```

---

# 🧠 AI Features

✅ OCR Text Extraction

✅ Machine Learning Document Classification

✅ NLP Text Summarization

✅ Semantic Search using Sentence Transformers

---

# Future Improvements

- User Authentication
- Cloud Database
- Chat with Documents (LLM)
- AI Question Answering
- Document Similarity Detection
- Multi-language OCR
- Cloud Storage Integration

---

# 👩‍💻 Author

**Nasreen Mursal**

GitHub:
https://github.com/Nasreen-15

---

# 📜 License

This project is licensed under the MIT License.
