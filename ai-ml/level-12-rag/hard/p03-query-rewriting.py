"""
LEVEL 12 — RAG Systems
HARD P03 — Query Rewriting
========================================

CONCEPT:
  User queries are often vague: "What is ML?" → the retrieval
  might miss. Rewrite queries to be more specific BEFORE searching.

  Simple rewrite: expand abbreviations, add context keywords.
  "ML" → "machine learning"; "DL" → "deep learning"; etc.

PROBLEM:
  Write `rewrite_query(query)` that:
    1. Expands common ML abbreviations (ML, DL, AI, NLP, CV, RL)
    2. Returns the rewritten query

TRY THIS INPUT:
  ```python
  print(rewrite_query("What is ML?"))
  print(rewrite_query("Tell me about NLP"))
  ```

EXPECTED OUTPUT:
  ```
  What is machine learning?
  Tell me about natural language processing
  ```

HINT:
  replacements = {"ML": "machine learning", "DL": "deep learning",
                  "NLP": "natural language processing", ...}
  Only replace whole words — use regex or split-and-join.

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(rewrite_query("What is ML?"))
