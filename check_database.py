import sqlite3

conn = sqlite3.connect("database/documents.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
    filename,
    category,
    summary
FROM documents
ORDER BY id DESC
LIMIT 3
""")

records = cursor.fetchall()

for row in records:
    print("\nFilename:", row[0])
    print("Category:", row[1])
    print("Summary:", row[2])

conn.close()