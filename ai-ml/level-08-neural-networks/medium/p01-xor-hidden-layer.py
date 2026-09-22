"""
LEVEL 08 — Neural Networks
MEDIUM P01 — XOR Gate (Why We Need Hidden Layers)
========================================

CONCEPT:
  XOR: output 1 when inputs DIFFER.
    [0,0]→0  [0,1]→1  [1,0]→1  [1,1]→0

  A single perceptron CANNOT solve XOR — no straight line separates
  the classes. You need a HIDDEN LAYER: 2 inputs → 2 hidden → 1 output.

  This is THE reason deep learning exists.

PROBLEM:
  Write `solve_xor()` that:
    1. X = [[0,0],[0,1],[1,0],[1,1]], y = [0,1,1,0]
    2. Builds 2→2→1 network (hidden sigmoid, output sigmoid)
    3. Trains 1000 epochs with lr=0.5 (manual or numpy)
    4. Returns (predictions, loss_history)

TRY THIS INPUT:
  ```python
  preds, losses = solve_xor()
  for x, p, t in zip(X, preds, y):
      print(f"{x} -> {p:.4f} (expected {t})")
  ```

EXPECTED OUTPUT:
  ```
  [0 0] -> 0.05xx (expected 0)
  [0 1] -> 0.95xx (expected 1)
  [1 0] -> 0.95xx (expected 1)
  [1 1] -> 0.04xx (expected 0)
  Final loss: ~0.002
  ```

HINT:
  Hidden layer: h = sigmoid(X @ W1 + b1)
  Output: out = sigmoid(h @ W2 + b2)
  Backprop: compute gradients for W2, b2, W1, b1 and update all.

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import numpy as np
# preds, losses = solve_xor()
# print(preds)
