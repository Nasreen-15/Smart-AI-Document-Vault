import sqlite3

conn = sqlite3.connect("database/documents.db")

cursor = conn.cursor()

cursor.execute("""
ALTER TABLE documents
ADD COLUMN summary TEXT
""")

conn.commit()
conn.close()

print("Summary column added successfully")