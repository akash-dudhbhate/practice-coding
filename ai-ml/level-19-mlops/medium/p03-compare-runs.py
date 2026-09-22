"""
LEVEL 19 — MLOps
MEDIUM P03 — Compare Runs, Pick the Best
========================================

CONCEPT:
  Tracking is useless unless you can answer "which run won?"
  Scan every line of runs.jsonl, keep the run with the highest
  value for one metric. This is `mlflow.search_runs` +
  `order_by("metrics.accuracy DESC")` — minus the database.

PROBLEM:
  Write `compare_runs(file, metric="accuracy")` that:
    1. Reads every non-empty line of `file` as a JSON run
    2. Ignores runs that don't have `metric` in their metrics
    3. Returns the run (dict) with the HIGHEST metric value
       — or None if no run qualifies

TRY THIS INPUT:
  ```python
  # runs.jsonl contains 3 runs with accuracy 0.90, 0.97, 0.93
  best = compare_runs("runs.jsonl")
  print(best["name"], best["metrics"]["accuracy"])
  ```

EXPECTED OUTPUT:
  ```
  lr-strong 0.97
  ```

HINT:
  best = None
  if metric in run.get("metrics", {}):
      if best is None or run["metrics"][metric] > best["metrics"][metric]:
          best = run

CHECK: python3 check.py medium/p03
"""

import json


# === WRITE YOUR CODE BELOW ===
def compare_runs(file, metric="accuracy"):
    """Return the run dict with the highest value for `metric`."""
    # TODO
    pass


# === TEST ===
# best = compare_runs("runs.jsonl")
# print(best["name"] if best else "no runs")
