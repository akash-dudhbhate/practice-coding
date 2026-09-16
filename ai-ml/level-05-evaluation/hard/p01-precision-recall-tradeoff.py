"""
LEVEL 05 — Model Evaluation
HARD P01 — Precision-Recall Threshold Tuning
========================================

CONCEPT:
  Default threshold = 0.5. But for imbalanced data (fraud,
  disease), you tune it: lower threshold → catch more positives
  (higher recall) but more false alarms (lower precision).

  precision_recall_curve gives (precisions, recalls, thresholds)
  for every possible threshold.

PROBLEM:
  Write `find_threshold()` that:
    1. make_classification(1000, 10 features, weights=[0.9,0.1],
       seed=42); split 80/20
    2. LogisticRegression(seed=42, max_iter=1000)
    3. precision_recall_curve on test probabilities
    4. Find threshold where recall ≈ 0.80 (closest index)
    5. Return (threshold, precision_at_that_threshold)

TRY THIS INPUT:
  ```python
  t, p = find_threshold()
  print(f"{t:.4f} {p:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  0.1466 0.5000
  ```
  (threshold dropped to 0.15 to catch 80% of the rare class —
   and precision fell to 0.50. That's the tradeoff.)

HINT:
  idx = np.argmin(np.abs(recalls - 0.8))
  thresholds[idx], precisions[idx]

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# t, p = find_threshold()
# print(t, p)
