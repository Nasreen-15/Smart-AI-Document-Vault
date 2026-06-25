from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def semantic_search(query, documents):

    corpus = documents + [query]

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(corpus)

    similarities = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )[0]

    results = list(
        zip(documents, similarities)
    )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return results