"""Level 12 Rag — Hard P02 Solution"""

def solve():
    def evaluate_rag(questions, expected_answers, retrieved_docs):
        metrics = {}
        for i, (q, expected, retrieved) in enumerate(zip(questions, expected_answers, retrieved_docs)):
            metrics[f'q{i}'] = {
                'retrieval_relevance': 0.8 if any(exp in r for r in retrieved) else 0.3,
                'answer_quality': 0.9 if expected in retrieved else 0.5,
            }
        avg_relevance = sum(m['retrieval_relevance'] for m in metrics.values()) / len(metrics)
        avg_quality = sum(m['answer_quality'] for m in metrics.values()) / len(metrics)
        print(f"Avg retrieval relevance: {avg_relevance:.2f}")
        print(f"Avg answer quality: {avg_quality:.2f}")
        return metrics
    questions = ["What is ML?", "What is DL?"]
    expected = ["machine learning", "deep learning"]
    retrieved = [["ML is machine learning", "Other doc"], ["DL is deep learning", "Other doc"]]
    return evaluate_rag(questions, expected, retrieved)

if __name__ == "__main__":
    solve()