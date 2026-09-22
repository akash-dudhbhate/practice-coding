"""
LEVEL 08 — Neural Networks
HARD P01 — Manual Backpropagation (XOR)
========================================

CONCEPT:
  Backprop = chain rule applied backwards through layers.
  For each weight: gradient = how much does the loss change
  if I nudge this weight?

  dL/dW2 = error_out · sigmoid'(out) · h
  dL/dW1 = (error_out · sigmoid'(out) · W2) · sigmoid'(h) · X

  You'll implement forward pass AND backward pass by hand.
  No autograd — pure numpy. This is the "under the hood" view.

PROBLEM:
  Write `train_manual()` that:
    1. X = [[0,0],[0,1],[1,0],[1,1]], y = [0,1,1,0] (XOR)
    2. W1 (2→2), b1, W2 (2→1), b2 — random init, seed=42
    3. Forward: h = sigmoid(X@W1 + b1); out = sigmoid(h@W2 + b2)
    4. Loss = MSE; backprop gradients; update with lr=0.5
    5. 5000 epochs; returns (predictions, losses)

TRY THIS INPUT:
  ```python
  preds, losses = train_manual()
  print(f"Final loss: {losses[-1]:.6f}")
  for x, p in zip(X, preds):
      print(x, f"{p:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  Final loss: ~0.0005
  [0 0] -> 0.02xx (expected 0)
  [0 1] -> 0.97xx (expected 1)
  [1 0] -> 0.97xx (expected 1)
  [1 1] -> 0.02xx (expected 0)
  ```

HINT:
  sigmoid'(x) = sigmoid(x) * (1 - sigmoid(x))
  error = out - y; then work backwards through the layers.

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# preds, losses = train_manual()
# print(losses[-1], preds)
