"""
LEVEL 04 — Supervised Learning
EASY P02 — Logistic Regression From Scratch
========================================

CONCEPT:
  Logistic regression predicts a PROBABILITY using sigmoid:
    sigmoid(z) = 1 / (1 + e^-z)   — squashes any number to 0-1
    z = w·x + b

  Training = gradient descent on the weights to minimize error.

PROBLEM:
  Write `sigmoid(z)` and `train_logreg(X, y, lr, epochs)` that:
    1. sigmoid: returns 1/(1+exp(-z))
    2. train_logreg: trains weights via gradient descent,
       returns (w, b)

TRY THIS INPUT:
  ```python
  print(sigmoid(0))   # 0.5
  w, b = train_logreg([[1,2],[2,3],[3,4],[4,5],[5,6]],
                      [0,0,0,1,1], lr=0.1, epochs=1000)
  preds = (sigmoid(np.array(X) @ w + b) > 0.5)
  ```

EXPECTED OUTPUT:
  ```
  0.5
  Accuracy: 1.0000
  Weights: [ 3.42 -1.52]  Bias: -4.94
  ```

HINT:
  Gradient: dw = X.T @ (p - y) / n; db = sum(p - y) / n

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import numpy as np
# print(sigmoid(0))
