"""
LEVEL 00 — Setup & Math
HARD P01 — Gradient Descent Intuition
========================================

CONCEPT:
  To minimize f(x) = x², walk opposite to the slope:
    x_new = x - lr × f'(x)    where f'(x) = 2x

  Start at x=5, lr=0.1:
    x = 5 - 0.1×(2×5) = 5 - 1.0 = 4.0
    x = 4 - 0.1×(2×4) = 4 - 0.8 = 3.2
    ...keeps shrinking toward 0 (the minimum)

  This is literally how every ML model learns.

PROBLEM:
  Write `descend(x0, lr, steps)` that runs gradient descent on
  f(x) = x² and returns the list of x values visited.

TRY THIS INPUT:
  ```python
  path = descend(5.0, 0.1, 20)
  print(f"{path[0]:.2f} -> {path[-1]:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  5.00 -> 0.0576
  ```
  (converging toward 0 — the minimum of x²)

HINT:
  path = [x0]; loop: x = x - lr * (2*x); path.append(x)

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# path = descend(5.0, 0.1, 20)
# print(path[0], path[-1])
