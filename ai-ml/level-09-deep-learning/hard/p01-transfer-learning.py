"""
LEVEL 09 — Deep Learning
HARD P01 — Transfer Learning
========================================

CONCEPT:
  Don't train from scratch — take a pretrained model (ResNet18
  trained on ImageNet), chop off its classifier head, replace
  with your own for YOUR classes.

  The pretrained layers already know edges, textures, shapes —
  you only need to teach it your specific classes.

  Freeze the backbone; train only the new head (fast!).

PROBLEM:
  Write `transfer_learn()` that:
    1. Loads resnet18 (weights=None for speed — or pretrained if available)
    2. Replaces fc layer: nn.Linear(model.fc.in_features, 10)
    3. Trains on CIFAR-10, 2 epochs
    4. Returns (test_accuracy, model)

TRY THIS INPUT:
  ```python
  acc, model = transfer_learn()
  print(f"{acc:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  ~0.5x-0.7x  (2 epochs on CIFAR-10 — even untrained ResNet helps)
  ```

HINT:
  from torchvision import models
  model = models.resnet18(weights=None)
  model.fc = nn.Linear(model.fc.in_features, 10)

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# acc, m = transfer_learn()
# print(acc)
