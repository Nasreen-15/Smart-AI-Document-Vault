import sqlite3

def get_answer(question):

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

    if not result:
        return "No documents found."

    document_text = result[0]

    question_words = question.lower().split()

    lines = document_text.split("\n")

    matches = []

    for line in lines:

        for word in question_words:

            if word in line.lower():
                matches.append(line)

    if matches:
        return "\n".join(matches[:5])

    return "No relevant answer found."