
import streamlit as st
import os
import sqlite3
import pandas as pd
from datetime import datetime
from ocr import extract_text
from ml_classifier import classify_document
from summarizer import generate_summary
from semantic_search import semantic_search

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Smart AI Document Vault",
    layout="wide"
)

# ==========================================
# TITLE
# ==========================================

st.title("📂 Smart AI Document Vault")

st.caption(
    "OCR + Machine Learning + NLP Powered Document Management System"
)

# ==========================================
# SIDEBAR
# ==========================================

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Upload",
        "Search",
        "Documents"
    ]
)

# ==========================================
# CREATE FOLDERS
# ==========================================

os.makedirs("uploads", exist_ok=True)

# ==========================================
# DASHBOARD PAGE
# ==========================================

if page == "Dashboard":

    st.subheader("📊 Dashboard")

    conn = sqlite3.connect(
        "database/documents.db"
    )

    cursor = conn.cursor()

    # Total
    cursor.execute(
        "SELECT COUNT(*) FROM documents"
    )
    total_docs = cursor.fetchone()[0]

    # Academic
    cursor.execute("""
    SELECT COUNT(*)
    FROM documents
    WHERE category='Academic'
    """)
    academic_docs = cursor.fetchone()[0]

    # Professional
    cursor.execute("""
    SELECT COUNT(*)
    FROM documents
    WHERE category='Professional'
    """)
    professional_docs = cursor.fetchone()[0]

    # Achievement
    cursor.execute("""
    SELECT COUNT(*)
    FROM documents
    WHERE category='Achievement'
    """)
    achievement_docs = cursor.fetchone()[0]

    # Other
    cursor.execute("""
    SELECT COUNT(*)
    FROM documents
    WHERE category='Other'
    """)
    other_docs = cursor.fetchone()[0]

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Total", total_docs)

    with col2:
        st.metric("Academic", academic_docs)

    with col3:
        st.metric("Professional", professional_docs)

    with col4:
        st.metric("Achievement", achievement_docs)

    with col5:
        st.metric("Other", other_docs)

    st.subheader("📄 Recent Documents")

    recent_df = pd.read_sql_query(
        """
        SELECT
            filename,
            category,
            upload_date
        FROM documents
        ORDER BY id DESC
        LIMIT 5
        """,
        conn
    )

    st.dataframe(
        recent_df,
        width="stretch"
    )

    conn.close()

# ==========================================
# UPLOAD PAGE
# ==========================================

elif page == "Upload":

    st.subheader("📤 Upload Document")

    uploaded_file = st.file_uploader(
        "Upload Document",
        type=["pdf", "jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        file_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(
                uploaded_file.getbuffer()
            )

        try:
            extracted_text = extract_text(
                file_path
            )

        except Exception as e:

            st.error(
                f"OCR Error: {e}"
            )

            extracted_text = ""

        category = classify_document(
            extracted_text
        )

        if len(extracted_text.strip()) > 50:

            summary = generate_summary(
                extracted_text
            )

        else:

            summary = (
                "Not enough text available "
                "for summarization."
            )

        conn = sqlite3.connect(
            "database/documents.db"
        )

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO documents
        (
            filename,
            category,
            upload_date,
            filepath,
            extracted_text,
            summary
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            uploaded_file.name,
            category,
            str(datetime.now()),
            file_path,
            extracted_text,
            summary
        ))

        conn.commit()
        conn.close()

        st.success(
            "✅ Document Uploaded and Saved!"
        )

        st.subheader(
            "📄 Extracted Text"
        )

        st.text_area(
            "OCR Output",
            extracted_text,
            height=250
        )

        if category == "Academic":
            st.success(
                f"📚 {category}"
            )

        elif category == "Professional":
            st.info(
                f"💼 {category}"
            )

        elif category == "Achievement":
            st.warning(
                f"🏆 {category}"
            )

        else:
            st.error(
                f"📄 {category}"
            )

        st.subheader(
            "📝 AI Summary"
        )

        st.text_area(
            "Document Summary",
            summary,
            height=200
        )

# ==========================================
# SEARCH PAGE
# ==========================================

elif page == "Search":

    st.subheader(
        "🧠 AI Semantic Search"
    )

    semantic_query = st.text_input(
        "Ask in natural language"
    )

    if semantic_query:

        conn = sqlite3.connect(
            "database/documents.db"
        )

        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            filename,
            extracted_text
        FROM documents
        """)

        records = cursor.fetchall()

        conn.close()

        documents = []

        for row in records:

            filename = row[0]

            text = (
                row[1]
                if row[1]
                else ""
            )

            documents.append(
                filename + " " + text
            )

        results = semantic_search(
            semantic_query,
            documents
        )

        st.write(
            "### Search Results"
        )

        found = False

        for doc, score in results:

            if score > 0:

                found = True

                st.write(
                    f"📄 {doc[:100]}..."
                )

                st.write(
                    f"Similarity Score: {round(score,3)}"
                )

                st.write("---")

        if not found:

            st.warning(
                "No relevant documents found."
            )

# ==========================================
# DOCUMENTS PAGE
# ==========================================

elif page == "Documents":

    st.subheader(
        "📄 Uploaded Documents"
    )

    search_query = st.text_input(
        "Search by filename or category"
    )

    conn = sqlite3.connect(
        "database/documents.db"
    )

    if search_query:

        query = f"""
        SELECT
            id,
            filename,
            category,
            upload_date
        FROM documents
        WHERE filename LIKE '%{search_query}%'
           OR category LIKE '%{search_query}%'
        """

    else:

        query = """
        SELECT
            id,
            filename,
            category,
            upload_date
        FROM documents
        ORDER BY id DESC
        """

    df = pd.read_sql_query(
        query,
        conn
    )

    st.dataframe(
        df,
        width="stretch"
    )

    conn.close()