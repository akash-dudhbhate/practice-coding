"""
LEVEL 12 — RAG Systems
EASY P02 — Simple Retrieval
========================================

CONCEPT:
  RAG (Retrieval-Augmented Generation) = search + generate.
  Step 1: embed all docs → Step 2: embed query → Step 3: find
  most similar docs → Step 4: feed to LLM for answering.

  Here we implement step 3: given a query, find the most
  relevant documents from a small corpus.

PROBLEM:
  Write `retrieve(query, docs, top_k)` that:
    1. Vectorizes query + docs with TfidfVectorizer
    2. Computes cosine similarity of query to each doc
    3. Returns top_k docs sorted by similarity

TRY THIS INPUT:
  ```python
  docs = ["ML is a subset of AI", "Deep learning uses neural nets",
          "Cooking requires recipes", "NLP processes text"]
  r = retrieve("What is machine learning?", docs, top_k=2)
  for doc, score in r:
      print(f"({score:.2f}) {doc}")
  ```

EXPECTED OUTPUT:
  ```
  (0.32) ML is a subset of AI
  (0.32) Deep learning uses neural nets
  ```
  (both docs tie — TF-IDF sees them as equally similar to the query)

HINT:
  docs_matrix = vectorizer.fit_transform(docs)
  query_vec = vectorizer.transform([query])
  scores = cosine_similarity(query_vec, docs_matrix).flatten()

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# docs = ["ML is a subset of AI", "Deep learning uses neural nets"]
# r = retrieve("What is ML?", docs, 2)
# print(r)
