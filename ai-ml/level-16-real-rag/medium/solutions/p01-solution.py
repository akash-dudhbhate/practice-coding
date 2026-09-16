"""Level 16 — Real RAG — Medium P01 Solution"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


class VectorStore:
    """Mini vector DB: .add(texts) embeds + stores, .query(q_vec, k)
    returns [(idx, score), ...] sorted by cosine similarity desc."""

    def __init__(self):
        self.vec = TfidfVectorizer()
        self.texts = []
        self.matrix = None          # L2-normalized dense doc vectors

    def add(self, texts):
        texts = list(texts)
        if self.matrix is None:
            X = self.vec.fit_transform(texts)     # fit on first add
        else:
            X = self.vec.transform(texts)         # fixed space after
        X = X.toarray() if hasattr(X, "toarray") else np.asarray(X, dtype=float)
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


if __name__ == "__main__":
    store = VectorStore()
    store.add(["machine learning models learn", "pasta needs boiling water",
               "neural networks mimic neurons"])
    q = store.vec.transform(["neural networks brain neurons"])
    print(store.query(q, k=2))
