"""Level 12 Rag — Easy P02 Solution"""

def solve():
    documents = [
        "Machine learning is a subset of AI.",
        "Deep learning uses neural networks.",
        "Data science combines statistics and programming."
    ]
    query = "What is machine learning?"
    # Simple retrieval (in reality, use embeddings + vector DB)
    def retrieve(query, docs, top_k=2):
        # Dummy similarity — in reality, use embeddings
        scores = [0.9, 0.3, 0.2]  # First doc is most similar
        ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
        return ranked[:top_k]
    results = retrieve(query, documents)
    print(f"Query: {query}")
    print("Retrieved documents:")
    for doc, score in results:
        print(f"  ({score:.2f}) {doc}")
    return results

if __name__ == "__main__":
    solve()