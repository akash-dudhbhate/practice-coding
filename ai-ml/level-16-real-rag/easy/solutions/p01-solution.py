"""Level 16 — Real RAG — Easy P01 Solution"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def embed(texts):
    """Fit TF-IDF on `texts`; return L2-normalized dense matrix."""
    vec = TfidfVectorizer()
    X = vec.fit_transform(texts).toarray()
    norms = np.linalg.norm(X, axis=1, keepdims=True)
    norms[norms == 0] = 1.0          # avoid divide-by-zero on empty rows
    return X / norms


if __name__ == "__main__":
    docs = ["machine learning models learn", "pasta needs boiling water",
            "neural networks mimic neurons"]
    M = embed(docs)
    print(M.shape)
    print(np.linalg.norm(M, axis=1))
