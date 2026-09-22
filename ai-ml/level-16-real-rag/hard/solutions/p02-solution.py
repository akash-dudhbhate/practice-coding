"""Level 16 — Real RAG — Hard P02 Solution"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def eval_rag(queries, expected_keywords, store, vec, k=3):
    """Hit-rate: fraction of queries where ANY expected keyword appears
    in the top-k retrieved texts. Returns a float in [0, 1]."""
    if not queries:
        return 0.0
    hits = 0
    for q, keywords in zip(queries, expected_keywords):
        results = store.query(vec.transform([q]), k)
        got = " ".join(store.texts[i] for i, _ in results).lower()
        if any(kw.lower() in got for kw in keywords):
            hits += 1
    return hits / len(queries)


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
    queries = ["language for data science", "tower in paris",
               "boiling salted water"]
    expected = [["python"], ["eiffel", "paris"], ["pasta"]]
    print(eval_rag(queries, expected, store, store.vec))
