"""Level 16 — Real RAG — Medium P03 Solution"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def retrieve(store, query, vec, k=3):
    """Embed `query`, ask the store for top-k, return the texts."""
    q_vec = vec.transform([query])
    hits = store.query(q_vec, k)          # [(idx, score), ...]
    return [store.texts[i] for i, _ in hits]


# --- demo store (medium/p01) so this file runs standalone ---
class VectorStore:
    def __init__(self):
        self.vec = TfidfVectorizer()
        self.texts = []
        self.matrix = None

    def add(self, texts):
        texts = list(texts)
        X = self.vec.fit_transform(texts) if self.matrix is None \
            else self.vec.transform(texts)
        X = X.toarray()
        norms = np.linalg.norm(X, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        X = X / norms
        self.matrix = X if self.matrix is None else np.vstack([self.matrix, X])
        self.texts += texts
        return len(texts)

    def query(self, q_vec, k=3):
        q = q_vec.toarray() if hasattr(q_vec, "toarray") else q_vec
        q = np.asarray(q, dtype=float).ravel()
        n = np.linalg.norm(q)
        if n:
            q = q / n
        scores = self.matrix @ q
        idx = np.argsort(-scores)[:k]
        return [(int(i), float(scores[i])) for i in idx]


DOCS = [
    "The Eiffel Tower is a wrought-iron lattice tower located in Paris, France.",
    "Python is a popular programming language widely used for data science.",
    "Machine learning models learn patterns from large training datasets.",
    "The Great Wall of China stretches over thirteen thousand miles.",
    "Neural networks are computing systems inspired by biological neurons.",
    "Cooking pasta requires boiling salted water and about ten minutes.",
]

if __name__ == "__main__":
    store = VectorStore()
    store.add(DOCS)
    for t in retrieve(store, "which programming language for data science?",
                      store.vec, k=2):
        print("-", t)
