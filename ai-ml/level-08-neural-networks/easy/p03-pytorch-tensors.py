"""
LEVEL 08 — Neural Networks
EASY P03 — PyTorch Tensor Basics
========================================

CONCEPT:
  PyTorch tensors = NumPy arrays + GPU + automatic gradients.
  torch.tensor([1,2,3]) creates one.
  .requires_grad_(True) → torch tracks operations for backprop.
  .backward() → computes gradients automatically.

PROBLEM:
  Write `tensor_basics()` that:
    1. Creates a = torch.tensor([1.,2.,3.], requires_grad=True)
    2. Creates b = torch.tensor([4.,5.,6.])
    3. Computes a + b, a * b, dot product
    4. Returns (sum_result, product_result, dot_result)

TRY THIS INPUT:
  ```python
  s, p, d = tensor_basics()
  print(s)   # tensor([5., 7., 9.])
  print(d)   # 32.0
  ```

EXPECTED OUTPUT:
  ```
  tensor([5., 7., 9.])
  tensor([ 4., 10., 18.])
  32.0
  ```

HINT:
  import torch
  torch.dot(a, b) for dot product

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# s, p, d = tensor_basics()
# print(s, p, d)
