"""
LEVEL 09 — Deep Learning
EASY P02 — Build a CNN Architecture
========================================

CONCEPT:
  CNN = Convolution → Activation → Pooling, repeated, then
  flatten → fully-connected layers for classification.

  Conv2d(1, 16, kernel_size=3, padding=1) — 1 channel in, 16 out
  MaxPool2d(2) — halve spatial size
  Flatten → Linear — classify

PROBLEM:
  Write `build_cnn()` that returns an nn.Sequential:
    Conv2d(1,16,3,padding=1) → ReLU → MaxPool2d(2)
    Conv2d(16,32,3,padding=1) → ReLU → MaxPool2d(2)
    Flatten() → Linear(1568, 128) → ReLU → Linear(128, 10)

TRY THIS INPUT:
  ```python
  model = build_cnn()
  print(model[0])          # Conv2d layer
  x = torch.randn(1,1,28,28)
  out = model(x)
  print(out.shape)         # torch.Size([1, 10])
  ```

EXPECTED OUTPUT:
  ```
  Conv2d(1, 16, kernel_size=(3,3), padding=(1,1))
  torch.Size([1, 10])
  ```

HINT:
  28×28 → pool → 14×14 → pool → 7×7; 32×7×7 = 1568

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import torch
# m = build_cnn()
# print(m(torch.randn(1,1,28,28)).shape)
