"""
LEVEL 00 — Setup & Math
HARD P02 — Bayes' Theorem (Medical Test)
========================================

CONCEPT:
  Bayes' theorem: P(sick | positive test) — the probability you
  ACTUALLY have the disease given a positive result.

    P(sick|+) = P(+|sick)·P(sick) / [P(+|sick)·P(sick) + P(+|healthy)·P(healthy)]

  Example: disease rate 1%, test catches 95% of sick, 10% false alarms
    P(sick|+) = 0.95×0.01 / (0.95×0.01 + 0.10×0.99) ≈ 0.0876

  Only 8.8%! Rare diseases + imperfect tests = mostly false alarms.
  This is why recall/precision matter (Level 05).

PROBLEM:
  Write `bayes(prior, sensitivity, false_positive_rate)` that returns
  P(sick | positive test).

TRY THIS INPUT:
  ```python
  p = bayes(0.01, 0.95, 0.10)
  print(f"{p:.4f}")   # 0.0876
  ```

EXPECTED OUTPUT:
  ```
  0.0876
  ```

HINT:
  numerator = sensitivity * prior
  denominator = numerator + false_positive_rate * (1 - prior)

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(bayes(0.01, 0.95, 0.10))
