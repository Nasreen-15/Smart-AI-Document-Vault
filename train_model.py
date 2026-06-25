import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

import pickle

# Load training data
df = pd.read_csv("training_data.csv")

# Create ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# Train model
model.fit(
    df["text"],
    df["category"]
)

# Save model
with open("document_classifier.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model Trained Successfully")