"""
LEVEL 12 — RAG Systems
HARD P02 — RAG Evaluation
========================================

CONCEPT:
  How good is your RAG? Evaluate on test questions:
    - Did it retrieve the right document?
    - Did the answer contain the right information?

  Metric: % of questions where the correct doc was in top-k.

PROBLEM:
  Write `evaluate_rag(questions, docs, answers)` that:
    1. For each question, retrieve the most similar doc
    2. Check if the retrieved doc matches the expected answer doc
    3. Returns accuracy = correct / total

TRY THIS INPUT:
  ```python
  questions = ["What is ML?", "What is deep learning?"]
  docs = ["ML is AI", "Deep learning uses neural nets"]
  answers = ["ML is AI", "Deep learning uses neural nets"]
  acc = evaluate_rag(questions, docs, answers)
  print(f"{acc:.2f}")   # 1.00 if both retrieved correctly
  ```

EXPECTED OUTPUT:
  ```
  1.00
  ```

HINT:
  For each question, find most similar doc via TF-IDF + cosine.
  Check if it equals the expected answer.

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# q = ["What is ML?", "What is DL?"]
# d = ["ML is AI", "DL uses nets"]
# a = ["ML is AI", "DL uses nets"]
# print(evaluate_rag(q, d, a))
