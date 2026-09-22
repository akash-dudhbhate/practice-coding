"""Level 12 — RAG Systems — Medium P01 Solution"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def vector_store(docs, query, top_k):
    vec = TfidfVectorizer()
    doc_vecs = vec.fit_transform(docs)
    query_vec = vec.transform([query])
    scores = cosine_similarity(query_vec, doc_vecs).flatten()
    top_idx = np.argsort(scores)[::-1][:top_k]
    return [(docs[i], scores[i]) for i in top_idx]

if __name__ == "__main__":
    docs = ["ML is great", "Python is a language", "Deep learning is fun",
            "NLP handles text", "Cooking is an art"]
    r = vector_store(docs, "Tell me about AI", 3)
    for doc, score in r:
        print(f"({score:.4f}) {doc}")
