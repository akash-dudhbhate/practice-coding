"""
LEVEL 12 — RAG Systems
HARD P01 — Simple RAG Pipeline
========================================

CONCEPT:
  RAG pipeline = retrieve → generate. No LLM needed for this exercise
  — we simulate the "generate" step with a simple template.

  retrieve: find most similar doc
  generate: "Based on: {doc} Answer: {query} is related to {doc}."

PROBLEM:
  Write `rag(query, docs)` that:
    1. Retrieves the most similar doc (use TF-IDF + cosine)
    2. Generates a template answer referencing it
    3. Returns (retrieved_doc, generated_answer)

TRY THIS INPUT:
  ```python
  docs = ["ML is a subset of AI", "Deep learning uses neural nets"]
  doc, answer = rag("What is ML?", docs)
  print(f"Retrieved: {doc}")
  print(f"Answer: {answer}")
  ```

EXPECTED OUTPUT:
  ```
  Retrieved: ML is a subset of AI
  Answer: Based on: ML is a subset of AI
  What is ML? is related to ML is a subset of AI.
  ```

HINT:
  Use your retrieve function from easy/p02 — or just find argmax
  of cosine similarity.

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# doc, ans = rag("What is ML?", ["ML is a subset of AI", "Deep learning is cool"])
# print(doc, ans)
