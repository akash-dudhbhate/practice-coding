"""Level 12 — RAG Systems — Easy P02 Solution"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def retrieve(query, docs, top_k=2):
    vec = TfidfVectorizer()
    doc_vecs = vec.fit_transform(docs)
    query_vec = vec.transform([query])
    scores = cosine_similarity(query_vec, doc_vecs).flatten()
    top_idx = np.argsort(scores)[::-1][:top_k]
    return [(docs[i], scores[i]) for i in top_idx]

if __name__ == "__main__":
    docs = ["ML is a subset of AI", "Deep learning uses neural nets",
            "Cooking requires recipes", "NLP processes text"]
    r = retrieve("What is machine learning?", docs, 2)
    for doc, score in r:
        print(f"({score:.2f}) {doc}")
