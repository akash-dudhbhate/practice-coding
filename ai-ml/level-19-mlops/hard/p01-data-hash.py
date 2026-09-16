"""
LEVEL 19 — MLOps
HARD P01 — Dataset Version Hash
========================================

CONCEPT:
  Reproducibility needs THREE pins: code, hyperparameters, and
  DATA. If the dataset changes silently (new rows, a fixed bug
  in preprocessing), old metrics become meaningless.

  A data hash fingerprints a dataset: shape + sample values.
  Change anything → different hash → "this isn't the same data
  the original run used."

  (Production tools do this with DVC / lakeFS / delta tables —
  same idea, one hash per dataset version.)

PROBLEM:
  Write `data_version_hash(X, y)` that returns a deterministic
  hex digest covering:
    - number of rows, number of feature columns, number of labels
    - first 5 and last 5 rows of X (rounded to 6 decimals)
    - first 5 and last 5 values of y (as ints)

  Steps:
    1. X.tolist() / y.tolist() if they have it (numpy → lists)
    2. Build a payload dict of the fields above
    3. hashlib.md5(json.dumps(payload, sort_keys=True).encode())

TRY THIS INPUT:
  ```python
  from sklearn.datasets import load_iris
  X, y = load_iris(return_X_y=True)
  h1 = data_version_hash(X, y)
  h2 = data_version_hash(X[:100], y[:100])
  print(h1 == h2)
  ```

EXPECTED OUTPUT:
  ```
  False          # different data → different hash
  ```

HINT:
  payload = {"n_rows": len(Xl), "n_cols": len(Xl[0]),
             "x_head": Xl[:5], "x_tail": Xl[-5:],
             "y_head": [int(v) for v in yl[:5]], ...}

CHECK: python3 check.py hard/p01
"""

import hashlib
import json


# === WRITE YOUR CODE BELOW ===
def data_version_hash(X, y):
    """Deterministic hex digest fingerprinting a dataset."""
    # TODO
    pass


# === TEST ===
# from sklearn.datasets import load_iris
# X, y = load_iris(return_X_y=True)
# print(data_version_hash(X, y))
