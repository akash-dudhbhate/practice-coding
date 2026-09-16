"""Level 16 — Real RAG — Hard P01 Solution"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def rag_answer(query, store, vec, k=2):
    """Retrieve top-k chunks, build a prompt, return an answer string
    that cites the retrieved context (template stands in for an LLM)."""
    hits = store.query(vec.transform([query]), k)
    ctx = [store.texts[i] for i, _ in hits]
    prompt = ("Answer the question using only the context below.\n\n"
              "Context:\n" + "\n".join(f"- {t}" for t in ctx) +
              f"\n\nQuestion: {query}\nAnswer:")
    # "Generation" step — a real system sends `prompt` to an LLM.
    answer = (f"Based on the retrieved docs: {ctx[0]}"
              + (f" Also relevant: {ctx[1]}" if len(ctx) > 1 else ""))
    return answer


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
    print(rag_answer("which language is used for data science?",
                     store, store.vec))
