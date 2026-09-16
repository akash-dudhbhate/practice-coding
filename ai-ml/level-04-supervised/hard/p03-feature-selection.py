"""
LEVEL 04 — Supervised Learning
HARD P03 — Feature Selection (RFE)
========================================

CONCEPT:
  RFE (Recursive Feature Elimination): train a model, drop the
  least important feature, repeat until you have N left.
  Finds which features actually matter — noise features hurt models.

  rfe.support_ → boolean mask of kept features
  X[:, mask] → keep only selected columns

PROBLEM:
  Write `select_features()` that:
    1. make_classification(200, 10 features, n_informative=5, seed=42)
    2. Split 80/20 (seed=42)
    3. RFE(RandomForestClassifier(seed=42), n_features_to_select=5)
    4. Retrain RF on selected features, return
       (selected_feature_indices_list, test_accuracy)

TRY THIS INPUT:
  ```python
  feats, acc = select_features()
  print(feats)      # [3, 4, 5, 6, 8]
  print(f"{acc:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  [3, 4, 5, 6, 8]
  0.9250
  ```

HINT:
  from sklearn.feature_selection import RFE
  np.where(rfe.support_)[0].tolist() → indices

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# f, a = select_features()
# print(f, a)
