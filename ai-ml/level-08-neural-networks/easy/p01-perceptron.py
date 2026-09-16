"""
LEVEL 08 — Neural Networks
EASY P01 — Perceptron (Simplest Neuron)
========================================

CONCEPT:
  A perceptron = weighted_sum + step function.
    output = 1 if (x·w + b) > 0 else 0

  Training: if prediction wrong, nudge weights toward the right answer:
    if y==1 and pred==0: w += x (increase)
    if y==0 and pred==1: w -= x (decrease)

PROBLEM:
  Write `train_perceptron()` that:
    1. X = [[0,0],[0,1],[1,0],[1,1]], y = [0,1,1,1] (OR gate)
    2. w = [0.1, 0.1], b = 0.0, epochs = 20
    3. For each epoch: for each sample, predict, update w/b
    4. Returns (w, b)

TRY THIS INPUT:
  ```python
  w, b = train_perceptron()
  print(w, b)
  # Test: for each X, compute step(x·w + b)
  ```

EXPECTED OUTPUT:
  ```
  [0.1 0.1] 0.0   (or converged weights that solve OR)
  [0 0] -> 0 (expected 0)
  [0 1] -> 1 (expected 1)
  [1 0] -> 1 (expected 1)
  [1 1] -> 1 (expected 1)
  ```

HINT:
  pred = 1 if np.dot(x, w) + b > 0 else 0
  if y == 1 and pred == 0: w += x; b += 0.1
  if y == 0 and pred == 1: w -= x; b -= 0.1

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import numpy as np
# w, b = train_perceptron()
# for x in [[0,0],[0,1],[1,0],[1,1]]:
#     print(x, 1 if np.dot(x, w) + b > 0 else 0)
