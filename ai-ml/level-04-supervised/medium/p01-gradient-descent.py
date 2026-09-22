"""
LEVEL 04 — Supervised Learning
MEDIUM P01 — Gradient Descent From Scratch
========================================

CONCEPT:
  Gradient descent = iterative optimization. Instead of the
  closed-form formula, we nudge m and b downhill on the MSE surface:

    MSE = mean((y - ŷ)²)
    dm = -2·mean(x·(y - ŷ));  db = -2·mean(y - ŷ)
    m -= lr·dm;  b -= lr·db

  Repeat until loss stops dropping.

PROBLEM:
  Write `gradient_descent()` that:
    1. np.random.seed(42); X = randn(100); y = 3X + 2 + noise(0.5)
    2. Starts m=0, b=0, lr=0.1, runs 100 iterations
    3. Tracks MSE each iteration
    4. Returns (m, b, losses)

TRY THIS INPUT:
  ```python
  m, b, losses = gradient_descent()
  print(f"{m:.4f} {b:.4f}")
  print(f"{losses[0]:.4f} -> {losses[-1]:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  2.9284 2.0037
  10.1116 -> 0.2209
  ```
  (m≈3, b≈2 — recovered the true line; loss dropped 10→0.22)

HINT:
  y_pred = m * X + b; MSE = np.mean((y - y_pred) ** 2)

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# m, b, losses = gradient_descent()
# print(m, b, losses[-1])
