"""
LEVEL 10 — Model Deployment
MEDIUM P03 — Model Versioning
========================================

CONCEPT:
  Track which model version produced which score.
  A versioned registry = a dict of {version: {model, accuracy}}.
  Later versions can be rolled back if performance drops.

PROBLEM:
  Write `build_registry()` that:
    1. Trains 3 models on iris: LogisticRegression,
       RandomForest, GradientBoosting (all seed=42)
    2. Stores each with a version key: v1, v2, v3
    3. Returns the registry dict

TRY THIS INPUT:
  ```python
  reg = build_registry()
  print(reg['v1'])  # {'model': 'logistic_regression', 'accuracy': 0.82}
  ```

EXPECTED OUTPUT:
  ```
  {'model': 'logistic_regression', 'accuracy': 0.82}
  {'model': 'random_forest', 'accuracy': 0.88}
  {'model': 'gradient_boosting', 'accuracy': 0.91}
  ```

HINT:
  registry = {}
  registry['v1'] = {'model': 'logistic_regression', 'accuracy': score}

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# r = build_registry()
# print(r)
