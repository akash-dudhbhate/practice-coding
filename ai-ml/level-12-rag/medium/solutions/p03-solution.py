"""Level 12 — RAG Systems — Medium P03 Solution"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def hybrid_search(query, docs, top_k):
    vec = TfidfVectorizer()
    doc_vecs = vec.fit_transform(docs)
    query_vec = vec.transform([query])
    semantic = cosine_similarity(query_vec, doc_vecs).flatten()

    query_words = set(query.lower().split())
    keyword = np.array([len(query_words & set(d.lower().split())) / len(query_words)
                        for d in docs])

    combined = 0.5 * keyword + 0.5 * semantic
    top_idx = np.argsort(combined)[::-1][:top_k]
    return [(docs[i], combined[i]) for i in top_idx]

if __name__ == "__main__":
    docs = ["Python is a programming language", "ML models learn patterns",
            "Cooking is an art", "AI and machine learning"]
    r = hybrid_search("machine learning", docs, 2)
    for d, s in r:
        print(f"({s:.4f}) {d}")
