# Lesson 20 — Hard P01: Simple RAG pipeline
# Knowledge base, retrieval function (TF-IDF), RAG prompt construction, mock LLM.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Knowledge base (list of documents)
knowledge_base = [
    "Python is a high-level programming language known for its readability and simplicity. It supports multiple paradigms including object-oriented and functional programming.",
    "Machine learning is a subset of AI that enables systems to learn from data. Common algorithms include linear regression, decision trees, and neural networks.",
    "REST APIs use HTTP methods (GET, POST, PUT, DELETE) to perform CRUD operations. They are stateless and return JSON or XML responses.",
    "Docker is a containerization platform that packages applications with their dependencies. Containers are lightweight and portable across environments.",
    "Git is a version control system that tracks changes in code. Key commands include commit, push, pull, branch, and merge.",
    "SQL databases store data in tables with rows and columns. Common operations include SELECT, INSERT, UPDATE, and DELETE with JOINs for related data.",
    "React is a JavaScript library for building user interfaces. It uses components, hooks, and a virtual DOM for efficient rendering.",
    "Neural networks are inspired by the human brain. They consist of layers of neurons with weights adjusted during training via backpropagation.",
]


def retrieve_documents(query, kb, top_k=3):
    """Retrieve top-k relevant documents using TF-IDF and cosine similarity."""
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(kb + [query])
    query_vec = tfidf_matrix[-1]
    doc_vecs = tfidf_matrix[:-1]
    similarities = cosine_similarity(query_vec, doc_vecs).flatten()
    top_indices = np.argsort(similarities)[::-1][:top_k]
    return [(kb[i], similarities[i]) for i in top_indices]


def construct_rag_prompt(query, retrieved_docs):
    """Construct a RAG prompt with retrieved context."""
    context = "\n\n".join([doc for doc, _ in retrieved_docs])
    prompt = f"""Answer the question based on the following context. If the context doesn't contain the answer, say "I don't have enough information."

Context:
{context}

Question: {query}

Answer:"""
    return prompt


def mock_llm_response(prompt):
    """Mock LLM that generates a response based on the prompt content."""
    if "Python" in prompt:
        return "Python is a high-level programming language known for readability and simplicity, supporting multiple paradigms."
    elif "machine learning" in prompt.lower() or "neural" in prompt.lower():
        return "Machine learning enables systems to learn from data using algorithms like neural networks and decision trees."
    elif "REST" in prompt or "API" in prompt:
        return "REST APIs use HTTP methods for CRUD operations and return JSON responses."
    elif "Docker" in prompt:
        return "Docker is a containerization platform that packages applications with dependencies for portability."
    elif "Git" in prompt:
        return "Git is a version control system for tracking code changes with commands like commit and push."
    elif "SQL" in prompt:
        return "SQL databases store data in tables, using operations like SELECT and JOIN."
    elif "React" in prompt:
        return "React is a JavaScript UI library using components and a virtual DOM."
    return "I don't have enough information to answer that question."


# Test with 5 questions
questions = [
    "What is Python?",
    "How do REST APIs work?",
    "What is Docker used for?",
    "How do neural networks work?",
    "What is Git?",
]

print("=== RAG Pipeline Test ===\n")
for q in questions:
    retrieved = retrieve_documents(q, knowledge_base, top_k=3)
    prompt = construct_rag_prompt(q, retrieved)
    answer = mock_llm_response(prompt)
    print(f"Question: {q}")
    print(f"Retrieved docs (top 3):")
    for doc, score in retrieved:
        print(f"  [{score:.3f}] {doc[:60]}...")
    print(f"Answer: {answer}")
    print()
