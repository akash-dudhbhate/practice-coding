"""
LEVEL 05 — Model Evaluation
EASY P03 — K-Fold Cross-Validation
========================================

CONCEPT:
  One train/test split can be lucky or unlucky. K-fold CV:
    split data into 5 parts → train on 4, test on 1, rotate ×5
    → 5 scores. Mean = estimate. Std = stability.

  cross_val_score(model, X, y, cv=5)

PROBLEM:
  Write `cross_validate()` that:
    1. Loads iris
    2. cross_val_score(RandomForestClassifier(seed=42), X, y, cv=5)
    3. Returns (mean_accuracy, std_accuracy)

TRY THIS INPUT:
  ```python
  m, s = cross_validate()
  print(f"{m:.4f} ± {s:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  0.9667 ± 0.0211
  ```

HINT:
  from sklearn.model_selection import cross_val_score
  scores.mean(), scores.std()

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# m, s = cross_validate()
# print(m, s)
