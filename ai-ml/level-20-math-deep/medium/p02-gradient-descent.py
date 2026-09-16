"""
LEVEL 20 — Deep Math for ML
MEDIUM P02 — Gradient Descent (Generic Optimizer)
========================================

CONCEPT:
  Gradient descent minimizes a function by repeatedly stepping
  opposite the gradient:

      x ← x - lr · ∇f(x)

  Every optimizer in deep learning (SGD, Momentum, Adam) is this
  loop with extra bookkeeping. Writing it generically — taking f
  and df as arguments — is exactly how torch.optim works under the
  hood: the model hands you gradients, you update parameters.

  Track f(x) each iteration into `history` — plotting it is how
  you diagnose lr-too-big (divergence) vs lr-too-small (plateau).

PROBLEM:
  Write `gradient_descent(f, df, x0, lr=0.1, iters=100)`:
    - f:   callable, returns scalar loss
    - df:  callable, returns gradient (same shape as x0)
    - x0:  starting point (float or np.array)
    Returns (x, history) where history = [f(x) after each update].

TRY THIS INPUT:
  ```python
  f  = lambda x: (x - 3.0)**2
  df = lambda x: 2.0*(x - 3.0)
  x, hist = gradient_descent(f, df, 0.0, lr=0.1, iters=50)
  print(x)          # ≈ 3.0
  print(hist[-1])   # ≈ 0.0
  ```

EXPECTED OUTPUT:
  ```
  2.999999999999999
  ~1e-28
  ```

HINT:
  x = np.array(x0, dtype=float) handles both scalars and vectors.
  Loop: x = x - lr*df(x); history.append(f(x)).

CHECK: python3 check.py medium/p02
"""

import numpy as np


# === WRITE YOUR CODE BELOW ===
def gradient_descent(f, df, x0, lr=0.1, iters=100):
    # TODO: x ← x - lr*df(x), record f(x) each step, return (x, history)
    pass


# === TEST ===
# f  = lambda x: (x - 3.0)**2
# df = lambda x: 2.0*(x - 3.0)
# x, hist = gradient_descent(f, df, 0.0, lr=0.1, iters=50)
# print(x, hist[-1])
