"""
LEVEL 05 — Model Evaluation
HARD P03 — Nested Cross-Validation
========================================

CONCEPT:
  Regular CV + grid search on the same data = biased estimate
  (you tuned ON the test folds). Nested CV fixes it:

    Outer loop (5-fold): splits data for honest evaluation
    Inner loop (3-fold): tunes hyperparameters within each
                         outer train fold only

  Result = unbiased estimate of the tuned pipeline's performance.

PROBLEM:
  Write `nested_cv()` that:
    1. make_classification(200, 10 features, seed=42)
    2. Inner: GridSearchCV(RandomForest(seed=42),
       {n_estimators:[50,100], max_depth:[3,5]}, cv=3)
    3. Outer: cross_val_score(inner_cv_object, X, y, cv=5)
    4. Returns the 5 outer scores array

TRY THIS INPUT:
  ```python
  s = nested_cv()
  print(f"{s.mean():.4f} ± {s.std():.4f}")
  ```

EXPECTED OUTPUT:
  ```
  0.8850 ± 0.0300
  ```

HINT:
  Pass the GridSearchCV OBJECT to cross_val_score —
  it refits (and retunes) inside each outer fold.

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# s = nested_cv()
# print(s.mean(), s.std())
