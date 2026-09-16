"""Level 12 Rag — Easy P01 Solution"""

import numpy as np

def solve():
    # Simple embedding simulation (in reality, use sentence-transformers)
    def embed(text):
        np.random.seed(hash(text) % 2**32)
        return np.random.randn(384)
    doc1 = embed("machine learning is fun")
    doc2 = embed("deep learning is powerful")
    doc3 = embed("machine learning is great")
    # Cosine similarity
    def cosine_sim(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    sim1 = cosine_sim(doc1, doc3)  # Similar texts
    sim2 = cosine_sim(doc1, doc2)  # Different texts
    print(f"Similar docs similarity: {sim1:.4f}")
    print(f"Different docs similarity: {sim2:.4f}")
    return sim1, sim2

if __name__ == "__main__":
    solve()