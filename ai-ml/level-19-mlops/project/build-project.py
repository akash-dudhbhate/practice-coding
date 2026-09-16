"""
LEVEL 19 PROJECT — Mini MLOps Pipeline
=======================================

The whole level in one function: train several configs → track
every run → pick the best → register it → gate it for release.

BUILD `run_pipeline()` that:

  1. Loads iris (train_test_split, test_size=0.25, random_state=42)
  2. Trains 3 LogisticRegression configs: C = 0.1, 1.0, 10.0
     (max_iter=300, random_state=42)
  3. Logs EACH run to runs.jsonl in this file's directory:
     {timestamp, name (f"lr-C{C}"), params, metrics: {"accuracy": ...}}
  4. Picks the best run by accuracy
  5. Registers it: appends to registry.json in this dir —
     {"name": "iris-lr", "version": <next int>, "hash": <md5 of
      get_params json>, "metrics": ..., "timestamp": ...,
      "model_path": <saved joblib file iris-lr_vN.joblib>}
  6. CI gate: accuracy >= 0.80 → deploy, else block

  Returns:
    {"best_run": <run dict>,
     "registered": <registry entry dict>,
     "gate": {"pass": bool, "failures": [str]}}

TEST IT:
  ```python
  r = run_pipeline()
  print(r["best_run"]["name"], r["best_run"]["metrics"]["accuracy"])
  print(r["registered"]["version"], r["gate"]["pass"])
  ```

EXPECTED:
  ```
  lr-C10.0 0.9x
  1 True
  ```

BONUS: verify reproducibility — hash the dataset before training,
store it in each run, then confirm retraining reproduces the metric.
"""

import hashlib
import json
import os
import time

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# === WRITE YOUR CODE BELOW ===

def run_pipeline():
    # TODO
    pass


if __name__ == "__main__":
    r = run_pipeline()
    print(r["best_run"]["name"], r["best_run"]["metrics"]["accuracy"])
    print("registered version:", r["registered"]["version"])
    print("gate:", r["gate"])
