"""
LEVEL 19 — MLOps
EASY P02 — Save and Load a Model
========================================

CONCEPT:
  A trained model is an ARTIFACT. Save it once, load it anywhere —
  a registry, a server, a CI job. joblib is the standard for
  sklearn models (fast, handles numpy arrays well).

PROBLEM:
  Write two functions:
    `save_model(model, path)` → joblib.dump(model, path), return path
    `load_model(path)`        → joblib.load(path), return the model

TRY THIS INPUT:
  ```python
  from sklearn.datasets import load_iris
  from sklearn.linear_model import LogisticRegression
  X, y = load_iris(return_X_y=True)
  m = LogisticRegression(max_iter=200).fit(X, y)
  p = save_model(m, "model.joblib")
  m2 = load_model(p)
  print(m2.predict(X[:3]))
  ```

EXPECTED OUTPUT:
  ```
  [0 0 0]
  ```

HINT:
  import joblib
  joblib.dump(model, path)
  model = joblib.load(path)

CHECK: python3 check.py easy/p02
"""

import joblib


# === WRITE YOUR CODE BELOW ===
def save_model(model, path):
    """Persist model to path with joblib. Returns path."""
    # TODO
    pass


def load_model(path):
    """Load and return a joblib-persisted model."""
    # TODO
    pass


# === TEST ===
# from sklearn.datasets import load_iris
# from sklearn.linear_model import LogisticRegression
# X, y = load_iris(return_X_y=True)
# m = LogisticRegression(max_iter=200).fit(X, y)
# save_model(m, "model.joblib")
# print(load_model("model.joblib").predict(X[:3]))
