"""
LEVEL 05 — Model Evaluation
MEDIUM P02 — Hyperparameter Grid Search
========================================

CONCEPT:
  Hyperparameters = knobs you set BEFORE training
  (n_estimators, max_depth...). Grid search tries every
  combination and picks the best via cross-validation.

  GridSearchCV(model, param_grid, cv=3) → .best_params_, .best_score_

PROBLEM:
  Write `grid_search()` that:
    1. make_classification(200, 10 features, seed=42); split 80/20
    2. GridSearchCV over:
       n_estimators [50,100,200], max_depth [3,5,10],
       min_samples_split [2,5]
    3. Returns (best_params, best_cv_score, test_score)

TRY THIS INPUT:
  ```python
  params, cv, test = grid_search()
  print(params)
  print(f"{cv:.4f} {test:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  {'max_depth': 10, 'min_samples_split': 5, 'n_estimators': 200}
  0.9xxx 0.9xxx
  ```

HINT:
  GridSearchCV(RandomForestClassifier(random_state=42), grid, cv=3)

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# p, c, t = grid_search()
# print(p, c, t)
