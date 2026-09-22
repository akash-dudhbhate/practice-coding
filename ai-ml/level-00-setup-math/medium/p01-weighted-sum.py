"""
LEVEL 00 — Setup & Math
MEDIUM P01 — Weighted Sum (The Neuron)
========================================

CONCEPT:
  Every neuron in a neural network computes:
    output = x₁w₁ + x₂w₂ + ... + xₙwₙ + b
           = dot(inputs, weights) + bias

  That's it. A whole neural network = this, repeated and stacked.

  Example: inputs [2, 3], weights [0.5, 1.5], bias 1
    = 2×0.5 + 3×1.5 + 1 = 1 + 4.5 + 1 = 6.5

PROBLEM:
  Write `weighted_sum(inputs, weights, bias)` that returns the
  neuron's raw output (before any activation function).

TRY THIS INPUT:
  ```python
  print(weighted_sum([2, 3], [0.5, 1.5], 1))   # 6.5
  print(weighted_sum([1, 1], [2, 2], 0))       # 4.0
  ```

EXPECTED OUTPUT:
  ```
  6.5
  4.0
  ```

HINT:
  Reuse your dot product logic: sum(x*w for x, w in zip(inputs, weights)) + bias

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(weighted_sum([2, 3], [0.5, 1.5], 1))
