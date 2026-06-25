import pickle

with open(
    "document_classifier.pkl",
    "rb"
) as f:

    model = pickle.load(f)

def classify_document(text):

    prediction = model.predict([text])

    return prediction[0]