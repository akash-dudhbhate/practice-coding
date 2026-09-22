"""
LEVEL 04 — Supervised Learning
HARD P02 — Ensemble Comparison
========================================

CONCEPT:
  Ensembles combine multiple models:
    Decision Tree: 1 tree — fast, but overfits (train 1.0!)
    Random Forest: many trees on random subsets — less overfit
    Gradient Boosting: trees built sequentially, each fixing errors

  Watch train vs test gap: 1.0 train / 0.92 test = overfitting.

PROBLEM:
  Write `compare_ensembles()` that:
    1. make_classification(500, 10 features, seed=42); split 80/20
    2. Trains DecisionTree, RandomForest, GradientBoosting (all seed=42)
    3. Returns dict {name: (train_acc, test_acc)}

TRY THIS INPUT:
  ```python
  r = compare_ensembles()
  for name, (tr, te) in r.items():
      print(f"{name}: {tr:.4f} / {te:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  Decision Tree: 1.0000 / 0.9200
  Random Forest: 1.0000 / 0.9400
  Gradient Boosting: 1.0000 / 0.9500
  ```

HINT:
  All three are in sklearn.tree / sklearn.ensemble.

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# r = compare_ensembles()
# print(r)
