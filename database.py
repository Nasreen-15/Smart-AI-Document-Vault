import sqlite3
import os

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/documents.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS documents(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    category TEXT,
    upload_date TEXT,
    filepath TEXT,
    extracted_text TEXT,
    summary TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")

