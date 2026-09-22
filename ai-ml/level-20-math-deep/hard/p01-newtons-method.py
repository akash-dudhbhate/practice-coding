"""
LEVEL 20 — Deep Math for ML
HARD P01 — Newton's Method (Second-Order Optimization)
========================================

CONCEPT:
  Gradient descent uses only the first derivative. Newton's method
  also uses curvature, so it converges QUADRATICALLY — the number
  of correct digits roughly doubles each step.

  To find a root of g(x), iterate:  x ← x − g(x)/g′(x)

  For √n we solve g(x) = x² − n = 0, and g′(x) = 2x, so:

      x ← x − (x² − n)/(2x)  =  (x + n/x) / 2

  That's Heron's formula — 2000 years old and still optimal.

  In ML the same idea is x ← x − H⁻¹∇f where H is the Hessian.
  H is too big to invert in deep learning, which is why we use
  Adam instead — but papers still cite Newton/L-BFGS constantly.

PROBLEM:
  Write `newton_sqrt(n, x0, iters=20)` that runs Newton's method
  to compute √n. Return (result, iterations_used). Stop early
  (break) when |x_new − x| < 1e-12 — that's convergence.

TRY THIS INPUT:
  ```python
  r, it = newton_sqrt(2.0, x0=1.0)
  print(r)     # 1.4142135623730951 — matches np.sqrt(2)
  print(it)    # ~5 iterations (quadratic convergence is FAST)
  ```

EXPECTED OUTPUT:
  ```
  1.4142135623730951
  4 or 5
  ```

HINT:
  x = x0
  for i in range(iters):
      x_new = 0.5 * (x + n / x)
      if abs(x_new - x) < 1e-12: return x_new, i+1
      x = x_new
  Return the count of iterations actually performed.

CHECK: python3 check.py hard/p01
"""

import numpy as np


# === WRITE YOUR CODE BELOW ===
def newton_sqrt(n, x0, iters=20):
    # TODO: Newton iterate x ← (x + n/x)/2, early-stop on convergence
    # Return (result, iterations_performed)
    pass


# === TEST ===
# r, it = newton_sqrt(2.0, 1.0)
# print(r, it)
