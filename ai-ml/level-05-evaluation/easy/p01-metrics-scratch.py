"""
LEVEL 05 — Model Evaluation
EASY P01 — Metrics From Scratch
========================================

CONCEPT:
  Accuracy  = (TP+TN)/total     — overall correctness
  Precision = TP/(TP+FP)        — of predicted YES, how many right?
  Recall    = TP/(TP+FN)        — of actual YES, how many caught?
  F1        = 2·P·R/(P+R)       — harmonic mean of precision/recall

PROBLEM:
  Write `compute_metrics(y_true, y_pred)` that returns a dict:
    {"accuracy": x, "precision": x, "recall": x, "f1": x}
  Pure Python — no sklearn.metrics.

TRY THIS INPUT:
  ```python
  y_true = [0,0,1,1,1,0,1,0,1,1]
  y_pred = [0,1,1,1,0,0,1,0,1,1]
  m = compute_metrics(y_true, y_pred)
  print(m)
  ```

EXPECTED OUTPUT:
  ```
  {'accuracy': 0.8, 'precision': 0.833..., 'recall': 0.833..., 'f1': 0.833...}
  ```
  (TP=5, FP=1, TN=3, FN=1)

HINT:
  TP = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==1)
  Guard division by zero (return 0.0).

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# m = compute_metrics([0,0,1,1,1,0,1,0,1,1], [0,1,1,1,0,0,1,0,1,1])
# print(m)
