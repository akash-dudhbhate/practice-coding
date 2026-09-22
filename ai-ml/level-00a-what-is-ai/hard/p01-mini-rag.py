"""
LEVEL 00A — What is AI?
HARD P01 — Mini RAG (Search Then Answer)
=========================================

CONCEPT:
  RAG = Retrieval-Augmented Generation = "search first, then answer."
  Instead of memorizing everything, the AI looks up your documents
  and answers using what it found. Open-book exam for AI.

PROBLEM:
  Write `mini_rag(question, docs)`:
    1. For each doc, compute similarity(question, doc) using
       word-overlap (shared/total — you built this in medium/p03)
    2. Return the doc with the highest similarity score
    3. If no doc shares any words, return "I don't know"

TRY THIS INPUT:
  ```python
  docs = [
      "Python is a programming language",
      "Cats sleep 16 hours a day",
      "Machine learning needs data",
  ]
  print(mini_rag("what is python?", docs))
  print(mini_rag("how long do cats sleep?", docs))
  print(mini_rag("quantum physics explained", docs))
  ```

EXPECTED OUTPUT:
  ```
  Python is a programming language
  Cats sleep 16 hours a day
  I don't know
  ```

WHY THIS MATTERS:
  This IS RAG — just without the LLM doing the final answer.
  Level-12 adds the "generate a nice answer" step on top.

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement mini_rag(question, docs)


def mini_rag(question, docs):
    """Find the most similar doc to the question."""
    pass


# === TEST ===
# docs = [
#     "Python is a programming language",
#     "Cats sleep 16 hours a day",
#     "Machine learning needs data",
# ]
# print(mini_rag("what is python?", docs))
# print(mini_rag("how long do cats sleep?", docs))
# print(mini_rag("quantum physics explained", docs))
