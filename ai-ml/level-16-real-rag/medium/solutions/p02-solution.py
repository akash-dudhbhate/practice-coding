"""Level 16 — Real RAG — Medium P02 Solution"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def chunk_text(text, size=100, overlap=20):
    """Overlapping chunks with metadata (same as easy/p03)."""
    step = max(1, size - overlap)
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        chunks.append({"id": len(chunks), "text": text[start:end],
                       "start": start, "end": end})
        if end >= len(text):
            break
        start += step
    return chunks


def ingest(store, raw_docs, size=100, overlap=20):
    """Chunk every raw doc and add the chunk texts to the store.

    The store embeds internally (store.add embeds via its vectorizer).
    Returns the total number of chunks added.
    """
    chunk_texts = []
    for doc in raw_docs:
        for c in chunk_text(doc, size=size, overlap=overlap):
            chunk_texts.append(c["text"])
    store.add(chunk_texts)
    return len(chunk_texts)


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


RAW_DOCS = [
    "Machine learning is a branch of artificial intelligence where models "
    "learn patterns from data instead of following explicit rules. "
    "Supervised learning trains on labeled examples, unsupervised learning "
    "finds hidden clusters, and reinforcement learning optimizes rewards.",

    "Paris is the capital of France and home to the Eiffel Tower, the "
    "Louvre museum, and countless cafes along the Seine. Visitors climb "
    "the tower at sunset for panoramic views, then stroll the "
    "Champs-Elysees toward the Arc de Triomphe.",

    "Great pasta starts with aggressively salted boiling water. Cook "
    "spaghetti until al dente, save a cup of starchy pasta water, then "
    "toss with the sauce so it clings to every strand. Finish with "
    "parmesan cheese and cracked black pepper.",
]

if __name__ == "__main__":
    store = VectorStore()
    n = ingest(store, RAW_DOCS)
    print(n, len(store.texts))
