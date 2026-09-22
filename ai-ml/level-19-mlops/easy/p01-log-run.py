"""
LEVEL 19 — MLOps
EASY P01 — Log a Training Run
========================================

CONCEPT:
  Experiment tracking = write one JSON line per training run.
  Every run records WHEN (timestamp), WHAT (name, params) and
  HOW WELL (metrics). Append-only: history is never overwritten.

  This is exactly what mlflow.log_param / wandb.log do —
  here it's just a file called runs.jsonl.

PROBLEM:
  Write `log_run(run_name, params, metrics)` that:
    1. Builds a record: {"timestamp": time.time(), "name": run_name,
                         "params": params, "metrics": metrics}
    2. Appends it as ONE JSON line to runs.jsonl
       (in this file's directory — use os.path.dirname(__file__))
    3. Returns the record dict

TRY THIS INPUT:
  ```python
  log_run("lr-baseline", {"C": 1.0}, {"accuracy": 0.95})
  log_run("lr-strong",   {"C": 10.0}, {"accuracy": 0.97})
  ```

EXPECTED OUTPUT (runs.jsonl):
  ```
  {"timestamp": 1717..., "name": "lr-baseline", "params": {"C": 1.0}, "metrics": {"accuracy": 0.95}}
  {"timestamp": 1717..., "name": "lr-strong", "params": {"C": 10.0}, "metrics": {"accuracy": 0.97}}
  ```

HINT:
  path = os.path.join(os.path.dirname(__file__), "runs.jsonl")
  with open(path, "a") as f:          # 'a' = append
      f.write(json.dumps(record) + "\n")

CHECK: python3 check.py easy/p01
"""

import json
import os
import time


# === WRITE YOUR CODE BELOW ===
def log_run(run_name, params, metrics):
    """Append one run record to runs.jsonl. Returns the record."""
    # TODO
    pass


# === TEST ===
# print(log_run("test", {"C": 1.0}, {"accuracy": 0.9}))
