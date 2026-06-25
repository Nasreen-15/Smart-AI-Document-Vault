from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def semantic_search(query, documents):

    query_embedding = model.encode([query])

    doc_embeddings = model.encode(documents)

    similarities = cosine_similarity(
        query_embedding,
        doc_embeddings
    )[0]

    results = list(
        zip(documents, similarities)
    )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return results