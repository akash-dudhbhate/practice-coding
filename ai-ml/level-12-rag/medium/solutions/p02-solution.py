"""Level 12 — RAG Systems — Medium P02 Solution"""

def rerank(query, retrieved_docs):
    query_words = set(query.lower().split())
    reranked = []
    for doc, score in retrieved_docs:
        doc_words = set(doc.lower().split())
        bonus = 0.1 * len(doc_words & query_words)
        reranked.append((doc, score + bonus))
    reranked.sort(key=lambda x: x[1], reverse=True)
    return reranked

if __name__ == "__main__":
    docs = [("Old doc about AI", 0.6), ("Recent ML advances", 0.5),
            ("Ancient history", 0.4)]
    for d, s in rerank("machine learning advances", docs):
        print(f"({s:.2f}) {d}")
