"""
LEVEL 10 — Model Deployment
EASY P01 — Save and Load a Model
========================================

CONCEPT:
  Once trained, save the model to disk. Then any app can load
  and predict — no retraining needed.

  joblib.dump(model, 'model.pkl') → save
  joblib.load('model.pkl') → load

PROBLEM:
  Write `save_and_load()` that:
    1. Trains LogisticRegression on iris (seed=42)
    2. Saves to 'model.pkl'
    3. Loads it back
    4. Returns predictions for the first 5 test samples

TRY THIS INPUT:
  ```python
  preds = save_and_load()
  print(preds)   # [0 1 0 0 1]
  ```

EXPECTED OUTPUT:
  ```
  [1 0 2 1 1]
  ```

HINT:
  import joblib
  joblib.dump(model, 'model.pkl')
  loaded = joblib.load('model.pkl')

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# p = save_and_load()
# print(p)
