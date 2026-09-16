"""Level 16 — Real RAG — Hard P03 Solution"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def _bm25_scores(query, docs, k1=1.5, b=0.75):
    """BM25-ish keyword score per doc."""
    toks = [d.lower().split() for d in docs]
    n = len(docs)
    dl = np.array([len(t) for t in toks], dtype=float)
    avgdl = dl.mean() if n else 1.0
    scores = np.zeros(n)
    for term in set(query.lower().split()):
        df = sum(1 for t in toks if term in t)
        if df == 0:
            continue
        idf = np.log((n - df + 0.5) / (df + 0.5) + 1.0)
        for i in range(n):
            f = toks[i].count(term)
            if f:
                scores[i] += idf * f * (k1 + 1) / \
                    (f + k1 * (1 - b + b * dl[i] / avgdl))
    return scores


def _maxnorm(a):
    m = a.max()
    return a / m if m > 0 else a


def hybrid(store, vec, query, docs, k=3, alpha=0.5):
    """Fuse dense (cosine via the store) with BM25-ish keyword scores.

    Returns [(idx, fused_score), ...] for top-k, sorted desc —
    same shape as store.query. Assumes the store holds `docs`
    in the same order.
    """
    n = len(docs)
    # dense scores for ALL docs
    dense = np.zeros(n)
    for i, s in store.query(vec.transform([query]), k=n):
        dense[i] = s
    # keyword scores
    kw = _bm25_scores(query, docs)
    fused = alpha * _maxnorm(dense) + (1 - alpha) * _maxnorm(kw)
    idx = np.argsort(-fused)[:k]
    return [(int(i), float(fused[i])) for i in idx]


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
        nn = np.linalg.norm(q)
        if nn:
            q = q / nn
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
    print(hybrid(store, store.vec, "great wall thousand miles", DOCS, k=2))
    print(hybrid(store, store.vec, "eiffel tower paris", DOCS, k=2))
