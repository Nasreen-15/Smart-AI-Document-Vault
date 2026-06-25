import sqlite3

conn = sqlite3.connect(
    "database/documents.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT extracted_text
FROM documents
ORDER BY id DESC
LIMIT 1
""")

result = cursor.fetchone()

conn.close()

print(result[0][:2000])