"""
LEVEL 09 — Deep Learning
HARD P03 — Custom nn.Module (The Real Way)
========================================

CONCEPT:
  nn.Sequential is fine for simple stacks, but real models
  need custom forward passes (skip connections, multiple heads,
  branching). Subclass nn.Module:

    class MyNet(nn.Module):
        def __init__(self):
            super().__init__()
            self.conv1 = nn.Conv2d(...)
            ...
        def forward(self, x):
            x = self.conv1(x)
            ...
            return x

PROBLEM:
  Write a class `CustomCNN(nn.Module)` that:
    - conv1: Conv2d(3, 32, 3, padding=1)
    - conv2: Conv2d(32, 64, 3, padding=1)
    - pool: MaxPool2d(2)
    - fc1: Linear(64*8*8, 128)
    - fc2: Linear(128, 10)
  forward: conv→relu→pool → conv→relu→pool → flatten→fc1→relu→fc2

  Then `count_params(model)` → total parameter count.

TRY THIS INPUT:
  ```python
  model = CustomCNN()
  x = torch.randn(4, 3, 32, 32)  # batch of 4 CIFAR images
  out = model(x)
  print(out.shape)              # torch.Size([4, 10])
  print(count_params(model))    # ~545K
  ```

EXPECTED OUTPUT:
  ```
  torch.Size([4, 10])
  545098
  ```

HINT:
  32×32 → pool → 16×16 → pool → 8×8; 64×8×8 = 4096
  x = x.view(x.size(0), -1) or nn.Flatten()

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import torch
# m = CustomCNN()
# print(m(torch.randn(4,3,32,32)).shape)
# print(count_params(m))
