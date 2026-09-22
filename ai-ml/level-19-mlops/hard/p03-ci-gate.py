"""
LEVEL 19 — MLOps
HARD P03 — CI Gate for Models
========================================

CONCEPT:
  Software CI blocks merges when tests fail. ML CI blocks
  DEPLOYS when metrics drop: "accuracy must be >= 0.85,
  f1 >= 0.80" — a model that misses the bar never ships.

  Key design rule: report EVERY failure, don't just assert the
  first one. Engineers need the full list to debug.

PROBLEM:
  Write `ci_gate(metrics, thresholds)` that:
    - for each (metric, min_value) in thresholds:
        missing metric      → failure "missing metric: {name}"
        value < min_value   → failure "{name}: {value} < {min}"
    - returns {"pass": no failures, "failures": [str, ...]}

TRY THIS INPUT:
  ```python
  print(ci_gate({"accuracy": 0.9, "f1": 0.85},
                {"accuracy": 0.8, "f1": 0.9}))
  ```

EXPECTED OUTPUT:
  ```
  {'pass': False, 'failures': ['f1: 0.85 < 0.9']}
  ```

HINT:
  failures = []
  for k, req in thresholds.items():
      if k not in metrics: ...
      elif metrics[k] < req: ...

CHECK: python3 check.py hard/p03
"""


# === WRITE YOUR CODE BELOW ===
def ci_gate(metrics, thresholds):
    """Check metrics against thresholds. Returns pass/fail report."""
    # TODO
    pass


# === TEST ===
# print(ci_gate({"accuracy": 0.9}, {"accuracy": 0.8}))
# print(ci_gate({"accuracy": 0.7}, {"accuracy": 0.8}))
