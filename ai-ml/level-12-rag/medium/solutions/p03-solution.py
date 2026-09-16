"""Level 12 Rag — Medium P03 Solution"""

def solve():
    def hybrid_search(query, documents, alpha=0.5):
        # Keyword search (BM25-like)
        keyword_scores = [len(set(query.split()) & set(doc.split())) for doc in documents]
        # Semantic search (simulated)
        semantic_scores = [np.random.random() for _ in documents]
        # Combine
        combined = [alpha * k + (1 - alpha) * s for k, s in zip(keyword_scores, semantic_scores)]
        ranked = sorted(zip(documents, combined), key=lambda x: x[1], reverse=True)
        return ranked
    docs = ["Machine learning tutorial", "Deep learning guide", "Python programming"]
    results = hybrid_search("machine learning", docs)
    print("Hybrid search results:")
    for doc, score in results:
        print(f"  ({score:.2f}) {doc}")
    return results

if __name__ == "__main__":
    solve()