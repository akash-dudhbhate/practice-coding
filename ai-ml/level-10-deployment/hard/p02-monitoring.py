"""
LEVEL 10 — Model Deployment
HARD P02 — Model Monitoring (Latency + Stats)
========================================

CONCEPT:
  In production, monitor your model: how fast is it? how many
  predictions? what's the error rate?

  A monitoring decorator wraps predict() to log:
    - prediction value
    - latency (time taken)
    - running stats

PROBLEM:
  Write `create_monitored_model()` that:
    1. Trains iris model
    2. Returns a wrapper function `predict(features)` that:
       - measures latency
       - logs "Prediction: X, latency: Ys"
       - tracks stats in a dict
    3. Also returns the stats dict

TRY THIS INPUT:
  ```python
  predict, stats = create_monitored_model()
  predict([5.1,3.5,1.4,0.2])
  predict([6.0,2.2,5.0,1.5])
  print(stats)  # {'total_predictions': 2, 'avg_latency': ...}
  ```

EXPECTED OUTPUT:
  ```
  INFO - Prediction: 0, latency: 0.0xxx s
  INFO - Prediction: 2, latency: 0.0xxx s
  {'total_predictions': 2, 'avg_latency': 0.0xxx}
  ```

HINT:
  import time; time.time() before and after predict.
  stats['total_predictions'] += 1; update avg_latency.

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# p, s = create_monitored_model()
# p([5.1,3.5,1.4,0.2])
# print(s)
