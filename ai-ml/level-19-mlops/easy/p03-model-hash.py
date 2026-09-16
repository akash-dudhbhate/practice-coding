"""
LEVEL 19 — MLOps
EASY P03 — Hash a Model's Configuration
========================================

CONCEPT:
  A model registry needs a stable ID for "this exact
  configuration". Hash the hyperparameters: same params →
  same hash, different params → different hash. Use it to
  dedupe runs or look up whether you've trained this before.

  Python's builtin hash() is NOT stable across processes —
  use hashlib (md5/sha256) on a canonical JSON string.

PROBLEM:
  Write `model_hash(model)` that:
    1. Gets params via model.get_params()
    2. Dumps to JSON with sort_keys=True, default=str
    3. Returns hashlib.md5(...).hexdigest()

TRY THIS INPUT:
  ```python
  from sklearn.linear_model import LogisticRegression
  a = LogisticRegression(C=1.0, max_iter=200)
  b = LogisticRegression(C=1.0, max_iter=200)
  c = LogisticRegression(C=5.0, max_iter=200)
  print(model_hash(a) == model_hash(b))   # True
  print(model_hash(a) == model_hash(c))   # False
  ```

EXPECTED OUTPUT:
  ```
  True
  False
  ```

HINT:
  s = json.dumps(model.get_params(), sort_keys=True, default=str)
  return hashlib.md5(s.encode()).hexdigest()

CHECK: python3 check.py easy/p03
"""

import hashlib
import json


# === WRITE YOUR CODE BELOW ===
def model_hash(model):
    """Deterministic hex digest of the model's hyperparameters."""
    # TODO
    pass


# === TEST ===
# from sklearn.linear_model import LogisticRegression
# print(model_hash(LogisticRegression(C=1.0)))
# print(model_hash(LogisticRegression(C=2.0)))
