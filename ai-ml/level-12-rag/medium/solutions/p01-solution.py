"""Level 12 Rag — Medium P01 Solution"""

import numpy as np

def solve():
    # Simulate a vector database
    class VectorDB:
        def __init__(self):
            self.embeddings = []
            self.metadata = []
        def add(self, embedding, metadata):
            self.embeddings.append(embedding)
            self.metadata.append(metadata)
        def search(self, query_embedding, top_k=3):
            similarities = []
            for emb in self.embeddings:
                sim = np.dot(query_embedding, emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(emb))
                similarities.append(sim)
            top_idx = np.argsort(similarities)[-top_k:][::-1]
            return [(self.metadata[i], similarities[i]) for i in top_idx]
    db = VectorDB()
    np.random.seed(42)
    for i in range(10):
        db.add(np.random.randn(384), f"doc_{i}")
    query = np.random.randn(384)
    results = db.search(query)
    print("Search results:")
    for meta, score in results:
        print(f"  {meta}: {score:.4f}")
    return results

if __name__ == "__main__":
    solve()