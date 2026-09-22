"""
LEVEL 19 — MLOps
HARD P02 — Reproduce a Run
========================================

CONCEPT:
  A run record is only trustworthy if you can REPRODUCE it:
  same data + same params + same seed → same metrics.
  This is the audit behind "the model got 0.97 accuracy".

  Recipe:
    run = {run_id, params, data_hash, metrics}
    1. Find the run in run_file (jsonl, one run per line)
    2. Rebuild the canonical dataset — check its hash matches
    3. Retrain LogisticRegression(**run["params"]) on the
       standard split (test_size=0.25, random_state=42)
    4. Compare new accuracy vs run["metrics"]["accuracy"]
       within tolerance

PROBLEM:
  Write `reproduce_run(run_file, run_id, tol=0.01)` that returns:
    {"found": bool,        # was run_id in the file?
     "data_ok": bool,      # does the dataset hash still match?
     "expected": float,    # accuracy the run logged
     "actual": float,      # accuracy from retraining
     "match": bool}        # |expected - actual| <= tol AND data_ok

  If the run isn't found: found=False, everything else False/None.
  If data hash mismatches: data_ok=False, match=False (still
  retrain so `actual` is informative).

  `make_dataset()` and `data_version_hash()` are PROVIDED —
  the canonical dataset and the p01 fingerprint.

TRY THIS INPUT:
  ```python
  res = reproduce_run("runs.jsonl", "run-1")
  print(res)
  ```

EXPECTED OUTPUT:
  ```
  {'found': True, 'data_ok': True, 'expected': 0.96,
   'actual': 0.96, 'match': True}
  ```

HINT:
  LogisticRegression(**run["params"]) — params must include
  random_state for determinism. score() on the test split.

CHECK: python3 check.py hard/p02
"""

import hashlib
import json

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# === PROVIDED HELPERS (from earlier problems) ===
def make_dataset():
    """The canonical dataset every run in this level trains on."""
    return make_classification(
        n_samples=200, n_features=5, n_informative=3, random_state=42)


def data_version_hash(X, y):
    """Deterministic hex digest fingerprinting a dataset (see p01)."""
    if hasattr(X, "tolist"):
        X = X.tolist()
    if hasattr(y, "tolist"):
        y = y.tolist()
    payload = {
        "n_rows": len(X),
        "n_cols": len(X[0]) if X else 0,
        "n_labels": len(y),
        "x_head": [[round(float(v), 6) for v in row] for row in X[:5]],
        "x_tail": [[round(float(v), 6) for v in row] for row in X[-5:]],
        "y_head": [int(v) for v in y[:5]],
        "y_tail": [int(v) for v in y[-5:]],
    }
    return hashlib.md5(
        json.dumps(payload, sort_keys=True).encode()).hexdigest()


# === WRITE YOUR CODE BELOW ===
def reproduce_run(run_file, run_id, tol=0.01):
    """Reload a logged run, retrain, verify metrics match."""
    # TODO
    pass


# === TEST ===
# import os, time, joblib
# X, y = make_dataset()
# Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42)
# params = {"C": 1.0, "max_iter": 300, "random_state": 42}
# acc = LogisticRegression(**params).fit(Xtr, ytr).score(Xte, yte)
# with open("runs.jsonl", "w") as f:
#     f.write(json.dumps({"run_id": "r1", "params": params,
#                         "data_hash": data_version_hash(X, y),
#                         "metrics": {"accuracy": acc}}) + "\n")
# print(reproduce_run("runs.jsonl", "r1"))
