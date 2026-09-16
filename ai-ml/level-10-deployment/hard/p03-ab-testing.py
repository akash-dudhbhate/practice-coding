"""
LEVEL 10 — Model Deployment
HARD P03 — A/B Testing Models
========================================

CONCEPT:
  A/B testing: send some traffic to model A, some to model B.
  Compare which performs better on real predictions.

  Route by hash of input — same input always goes to same model
  (consistent experience), but different inputs split ~50/50.

PROBLEM:
  Write `ab_test()` that:
    1. Trains two models on iris: LR (model A) and RF (model B)
    2. For 100 random samples, routes each to A or B
       (hash of features → even=A, odd=B)
    3. Returns dict: {'model_a': {count, correct}, 'model_b': {count, correct}}

TRY THIS INPUT:
  ```python
  r = ab_test()
  print(r['model_a']['count'], r['model_b']['count'])
  # ~50/50 split
  ```

EXPECTED OUTPUT:
  ```
  45 55  (or similar — roughly half each)
  ```

HINT:
  hash(tuple(features)) % 2 → 0 for A, 1 for B
  Track count and correct predictions per model.

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# r = ab_test()
# print(r)
