"""
LEVEL 04 — Supervised Learning
MEDIUM P02 — Random Forest Feature Importance
========================================

CONCEPT:
  RandomForestClassifier = many decision trees voting together.
  feature_importances_ = which features the trees relied on most.
  Sums to 1.0. High importance = that feature drives predictions.

PROBLEM:
  Write `train_forest()` that:
    1. make_classification(200, 5 features, n_informative=3, seed=42)
    2. Split 80/20 (seed=42)
    3. RandomForestClassifier(100 trees, seed=42)
    4. Returns (test_accuracy, feature_importances_array)

TRY THIS INPUT:
  ```python
  acc, imp = train_forest()
  print(f"{acc:.4f}")
  print(f"{imp[0]:.4f}")   # feature 0 importance
  ```

EXPECTED OUTPUT:
  ```
  0.9500
  0.4379
  ```
  (Feature 0 dominates — it's an "informative" feature)

HINT:
  rf.feature_importances_ — numpy array, one value per feature.

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# acc, imp = train_forest()
# print(acc, imp)
