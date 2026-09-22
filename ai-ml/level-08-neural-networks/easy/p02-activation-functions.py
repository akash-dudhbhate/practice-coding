"""
LEVEL 08 — Neural Networks
EASY P02 — Activation Functions
========================================

CONCEPT:
  Without activation functions, a neural network = just one big
  linear regression. Activations add the nonlinearity that lets
  networks learn curves, circles, anything.

  Key ones:
    sigmoid(z)  = 1/(1+e^-z)      — squash to (0,1)
    relu(z)     = max(0, z)        — kill negatives
    tanh(z)     = (e^z - e^-z)/(e^z + e^-z) — squash to (-1,1)

PROBLEM:
  Write three functions: `sigmoid(z)`, `relu(z)`, `tanh(z)`
  Each takes a number or array, returns the activated value.

TRY THIS INPUT:
  ```python
  print(sigmoid(0))     # 0.5
  print(relu(-2))       # 0
  print(relu(3))        # 3
  print(tanh(0))        # 0.0
  ```

EXPECTED OUTPUT:
  ```
  0.5
  0
  3
  0.0
  ```

HINT:
  import numpy as np
  sigmoid: 1 / (1 + np.exp(-z))
  relu: np.maximum(0, z)
  tanh: np.tanh(z)

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(sigmoid(0), relu(-2), relu(3), tanh(0))
