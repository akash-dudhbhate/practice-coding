"""
LEVEL 06 — Advanced ML
HARD P03 — Balanced Ensemble via class_weight
========================================

CONCEPT:
  Another way to handle imbalance (besides resampling): tell the
  model to pay more attention to the minority class.

  class_weight='balanced' → sklearn auto-computes weights inversely
  proportional to class frequency. No extra libraries needed.

  The tradeoff is real: balanced model catches the minority class
  but creates more false alarms (lower precision/F1).

PROBLEM:
  Write `compare_balanced()` that:
    1. make_classification(1000, 10 features, weights=[0.95,0.05],
       n_informative=5, flip_y=0.0, seed=42); split 80/20 (seed=42)
    2. Train LogisticRegression(seed=42, max_iter=1000) — default
    3. Train same model + class_weight='balanced'
    4. Returns (recall_default, recall_balanced, f1_default, f1_balanced)

TRY THIS INPUT:
  ```python
  rd, rb, fd, fb = compare_balanced()
  print(f"{rd:.4f} {rb:.4f} {fd:.4f} {fb:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  0.0000 0.8571 0.0000 0.2500
  ```
  (Default model catches ZERO minority samples — recall 0!
   Balanced catches 86% — but F1 drops to 0.25 from false alarms.
   THAT'S the precision-recall tradeoff in action.)

HINT:
  from sklearn.metrics import recall_score, f1_score
  recall_score(y_test, y_pred) — pos_label defaults to 1.

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# rd, rb, fd, fb = compare_balanced()
# print(rd, rb, fd, fb)
