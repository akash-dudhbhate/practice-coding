"""
LEVEL 20 — Deep Math for ML
HARD P03 — Adam Optimizer
========================================

CONCEPT:
  Adam = Momentum + RMSProp + bias correction. It keeps two
  running averages of the gradient g:

      m ← β₁·m + (1−β₁)·g        first moment — smoothed gradient
      v ← β₂·v + (1−β₂)·g²       second moment — smoothed grad²

  Early steps are biased toward 0 (m,v start at 0), so correct:

      m̂ = m / (1−β₁ᵗ)      v̂ = v / (1−β₂ᵗ)     t = step number (1,2,…)

  Update (per-parameter adaptive learning rate):

      x ← x − lr · m̂ / (√v̂ + ε)

  Defaults: β₁=0.9, β₂=0.999, ε=1e-8 — this is EXACTLY
  torch.optim.Adam. Dimensions with big gradients get smaller
  effective steps → it navigates narrow valleys GD can't.

PROBLEM:
  Write `adam_optimize(f, df, x0, lr=0.01, iters=200,
                      beta1=0.9, beta2=0.999, eps=1e-8)`
  Same signature as gradient_descent; return (x, history) with
  history = [f(x) after each update].

TRY THIS INPUT:
  ```python
  f  = lambda x: float(np.sum((x - 3.0)**2))
  df = lambda x: 2.0*(x - 3.0)
  x, hist = adam_optimize(f, df, np.zeros(4), lr=0.1, iters=300)
  print(x)          # ≈ [3, 3, 3, 3]
  print(hist[-1])   # ≈ 0
  ```

EXPECTED OUTPUT:
  ```
  [2.999… 2.999… 2.999… 2.999…]
  ~1e-6 or smaller
  ```

HINT:
  m = np.zeros_like(x); v = np.zeros_like(x)
  for t in 1..iters:
      g = df(x)
      m = beta1*m + (1-beta1)*g
      v = beta2*v + (1-beta2)*g**2
      m_hat = m / (1 - beta1**t)
      v_hat = v / (1 - beta2**t)
      x = x - lr * m_hat / (np.sqrt(v_hat) + eps)
      history.append(f(x))

CHECK: python3 check.py hard/p03
"""

import numpy as np


# === WRITE YOUR CODE BELOW ===
def adam_optimize(f, df, x0, lr=0.01, iters=200, beta1=0.9, beta2=0.999, eps=1e-8):
    # TODO: Adam update loop; return (x, history of f(x))
    pass


# === TEST ===
# f  = lambda x: float(np.sum((x - 3.0)**2))
# df = lambda x: 2.0*(x - 3.0)
# x, hist = adam_optimize(f, df, np.zeros(4), lr=0.1, iters=300)
# print(x)
# print(hist[-1])
