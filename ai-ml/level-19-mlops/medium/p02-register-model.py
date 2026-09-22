"""
LEVEL 19 — MLOps
MEDIUM P02 — Model Registry
========================================

CONCEPT:
  A registry answers: "what models do we have, which version is
  which, and how good is each?" It's just a JSON file mapping
  "name-vN" → metadata + a saved model artifact.

  registry.json:
    {"iris-v1": {"name": "iris", "version": 1, "hash": "ab12...",
                 "metrics": {"accuracy": 0.9}, "timestamp": ...,
                 "model_path": ".../iris_v1.joblib"}}

PROBLEM:
  Write `register_model(model, name, metrics)` that:
    1. Loads registry.json from THIS file's directory
       (empty dict {} if it doesn't exist)
    2. version = (# existing entries for `name`) + 1
    3. Saves the model as {name}_v{version}.joblib in that dir
    4. Adds entry: {"name", "version", "hash", "metrics",
                    "timestamp", "model_path"}
       hash = md5 of json.dumps(model.get_params(), sort_keys=True)
    5. Writes registry.json back (json.dump, indent=2)
    6. Returns the entry dict

TRY THIS INPUT:
  ```python
  m = LogisticRegression(max_iter=200).fit(X, y)
  e1 = register_model(m, "iris", {"accuracy": 0.93})
  e2 = register_model(m, "iris", {"accuracy": 0.95})
  print(e1["version"], e2["version"])
  ```

EXPECTED OUTPUT:
  ```
  1 2
  ```

HINT:
  key = f"{name}-v{version}"
  versions = [k for k in reg if k.startswith(f"{name}-v")]

CHECK: python3 check.py medium/p02
"""

import hashlib
import json
import os
import time

import joblib


# === WRITE YOUR CODE BELOW ===
def register_model(model, name, metrics):
    """Save model + record a versioned entry in registry.json."""
    # TODO
    pass


# === TEST ===
# from sklearn.datasets import load_iris
# from sklearn.linear_model import LogisticRegression
# X, y = load_iris(return_X_y=True)
# m = LogisticRegression(max_iter=200).fit(X, y)
# print(register_model(m, "iris", {"accuracy": 0.93}))
