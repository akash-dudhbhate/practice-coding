"""
LEVEL 19 — MLOps
MEDIUM P01 — ExperimentTracker Class
========================================

CONCEPT:
  easy/p01's log_run works, but real tracking is a LIFECYCLE:
  start a run → log things as you go → end it. That's the
  mlflow pattern (`with mlflow.start_run(): ...`).

  Keep the open run in memory; only write to disk on end_run().

PROBLEM:
  Write class `ExperimentTracker`:
    __init__(self, path=None)
        path defaults to runs.jsonl in THIS file's directory
    start_run(self, name)
        opens a fresh run: {"timestamp": time.time(), "name": name,
                            "params": {}, "metrics": {}}
    log_param(self, key, value)   → run["params"][key] = value
    log_metric(self, key, value)  → run["metrics"][key] = value
    end_run(self)
        append the run as one JSON line to path, clear the open
        run, and return the run dict

TRY THIS INPUT:
  ```python
  t = ExperimentTracker()
  t.start_run("lr-v1")
  t.log_param("C", 1.0)
  t.log_metric("accuracy", 0.95)
  print(t.end_run())
  ```

EXPECTED OUTPUT:
  ```
  {'timestamp': 1717..., 'name': 'lr-v1', 'params': {'C': 1.0},
   'metrics': {'accuracy': 0.95}}
  ```
  (plus one line appended to runs.jsonl)

HINT:
  self._run = None in __init__; guard log_* with
  "if self._run is None: raise RuntimeError('no active run')"

CHECK: python3 check.py medium/p01
"""

import json
import os
import time


# === WRITE YOUR CODE BELOW ===
class ExperimentTracker:
    """Minimal experiment tracker: start → log → end → jsonl line."""

    def __init__(self, path=None):
        # TODO
        pass

    def start_run(self, name):
        # TODO
        pass

    def log_param(self, key, value):
        # TODO
        pass

    def log_metric(self, key, value):
        # TODO
        pass

    def end_run(self):
        # TODO
        pass


# === TEST ===
# t = ExperimentTracker()
# t.start_run("lr-v1")
# t.log_param("C", 1.0)
# t.log_metric("accuracy", 0.95)
# print(t.end_run())
