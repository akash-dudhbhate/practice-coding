"""Level 12 — RAG Systems — Hard P02 Solution"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def evaluate_rag(questions, docs, answers):
    vec = TfidfVectorizer()
    doc_vecs = vec.fit_transform(docs)
    correct = 0
    for q, expected in zip(questions, answers):
        q_vec = vec.transform([q])
        scores = cosine_similarity(q_vec, doc_vecs).flatten()
        best_idx = np.argmax(scores)
        if docs[best_idx] == expected:
            correct += 1
    return correct / len(questions)

if __name__ == "__main__":
    questions = ["What is ML?", "What is deep learning?"]
    docs = ["ML is AI", "Deep learning uses neural nets"]
    answers = ["ML is AI", "Deep learning uses neural nets"]
    print(f"{evaluate_rag(questions, docs, answers):.2f}")
