"""Level 12 Rag — Medium P02 Solution"""

import numpy as np

def solve():
    def rerank(results, query_embedding, boost_recent=True):
        reranked = []
        for doc, score in results:
            # Boost score if document is recent (simulated)
            if boost_recent and 'recent' in doc.lower():
                score *= 1.2
            reranked.append((doc, score))
        return sorted(reranked, key=lambda x: x[1], reverse=True)
    results = [
        ("Old document about ML", 0.8),
        ("Recent ML advances", 0.7),
        ("Ancient AI history", 0.6),
    ]
    reranked = rerank(results, None)
    print("Reranked results:")
    for doc, score in reranked:
        print(f"  ({score:.2f}) {doc}")
    return reranked

if __name__ == "__main__":
    solve()