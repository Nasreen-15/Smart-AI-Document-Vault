from semantic_search import semantic_search

documents = [

    "Bachelor of Engineering Marksheet",

    "Internship Certificate at TCS",

    "Resume with Python Skills"
]

query = "Show my internship documents"

results = semantic_search(
    query,
    documents
)

for doc, score in results:

    print(doc, round(score, 3))