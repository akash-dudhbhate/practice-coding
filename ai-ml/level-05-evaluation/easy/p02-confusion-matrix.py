"""
LEVEL 05 — Model Evaluation
EASY P02 — Confusion Matrix
========================================

CONCEPT:
  Confusion matrix = the 4 outcomes of binary prediction:
    TP (hit)  |  FN (miss)
    FP (false alarm) |  TN (correct reject)

  Everything else (accuracy, precision, recall) derives from these.

PROBLEM:
  Write `confusion(y_true, y_pred)` that returns
  {"TP": x, "FP": x, "TN": x, "FN": x}

TRY THIS INPUT:
  ```python
  c = confusion([0,0,1,1,1,0,1,0,1,1], [0,1,1,1,0,0,1,0,1,1])
  print(c)
  ```

EXPECTED OUTPUT:
  ```
  {'TP': 5, 'FP': 1, 'TN': 3, 'FN': 1}
  ```

HINT:
  Loop over pairs; count each of the 4 cases.

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(confusion([0,0,1,1,1,0,1,0,1,1], [0,1,1,1,0,0,1,0,1,1]))
