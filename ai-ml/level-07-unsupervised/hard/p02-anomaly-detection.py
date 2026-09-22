"""
LEVEL 07 — Unsupervised Learning
HARD P02 — Anomaly Detection (IsolationForest)
========================================

CONCEPT:
  IsolationForest: anomalies are "easy to isolate" — a random
  split tree reaches them in fewer steps. contamination = the
  fraction of expected anomalies.

  predict() returns -1 (anomaly) or 1 (normal).

PROBLEM:
  Write `detect_anomalies()` that:
    1. Normal data: np.random.normal(0, 0.5, (100,2)) seed=42
    2. Inject 10 outliers: uniform(-5,5,(10,2))
    3. IsolationForest(contamination=0.1, random_state=42)
    4. Returns (predictions_array, n_anomalies_detected)

TRY THIS INPUT:
  ```python
  preds, n = detect_anomalies()
  print(len(preds))   # 110
  print(n)            # ~11 anomalies flagged
  ```

EXPECTED OUTPUT:
  ```
  110
  11
  ```

HINT:
  np.vstack([normal, outliers]) to combine.
  preds == -1 → anomalies.

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# preds, n = detect_anomalies()
# print(len(preds), n)
