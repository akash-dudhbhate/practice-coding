"""Level 12 — RAG Systems — Hard P01 Solution"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rag(query, docs):
    vec = TfidfVectorizer()
    doc_vecs = vec.fit_transform(docs)
    query_vec = vec.transform([query])
    scores = cosine_similarity(query_vec, doc_vecs).flatten()
    best_idx = np.argmax(scores)
    retrieved = docs[best_idx]
    answer = f"Based on: {retrieved}\n{query} is related to {retrieved}."
    return retrieved, answer

if __name__ == "__main__":
    doc, ans = rag("What is ML?", ["ML is a subset of AI", "Deep learning uses neural nets"])
    print(f"Retrieved: {doc}")
    print(f"Answer: {ans}")
