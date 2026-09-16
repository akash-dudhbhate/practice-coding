"""
LEVEL 16 — Real RAG (Embeddings + Vector DB)
HARD P01 — Full RAG Answer
========================================

CONCEPT:
  Full RAG = retrieve → stuff chunks into a prompt → generate.
  The prompt is just a string: context lines + the question, shaped
  exactly like what you'd send to an LLM.

  We have no LLM here, so a template "answer" that cites the
  retrieved context stands in for the generation step — the
  pipeline shape is what matters.

PROBLEM:
  Write `rag_answer(query, store, vec, k=2)` that:
    1. Embeds the query with vec, retrieves top-k chunks from store
    2. Builds a prompt string: context lines + the question
    3. Returns an answer STRING that includes the retrieved context
       (e.g. f"Based on the docs: {top_chunk}")

TRY THIS INPUT:
  ```python
  store = VectorStore(); store.add(DOCS)
  print(rag_answer("which language is used for data science?",
                   store, store.vec))
  ```

EXPECTED OUTPUT:
  ```
  ... 'Python is a popular programming language widely used ...' ...
  ```

HINT:
  hits = store.query(vec.transform([query]), k)
  context = "\\n".join(store.texts[i] for i, _ in hits)
  prompt = f"Context:\\n{context}\\n\\nQuestion: {query}\\nAnswer:"

CHECK: python3 check.py hard/p01
"""

DOCS = [
    "The Eiffel Tower is a wrought-iron lattice tower located in Paris, France.",
    "Python is a popular programming language widely used for data science.",
    "Machine learning models learn patterns from large training datasets.",
    "The Great Wall of China stretches over thirteen thousand miles.",
    "Neural networks are computing systems inspired by biological neurons.",
    "Cooking pasta requires boiling salted water and about ten minutes.",
]

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# store = VectorStore(); store.add(DOCS)
# print(rag_answer("how long should I boil dinner in salted water?",
#                  store, store.vec))
