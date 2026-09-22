"""
LEVEL 09 — Deep Learning
MEDIUM P01 — Train a CNN on CIFAR-10
========================================

CONCEPT:
  CIFAR-10 = 60,000 color images (32×32), 10 classes.
  CNNs preserve spatial structure — Conv2d slides filters
  over the image instead of flattening immediately.

  Same training loop as before, but the model sees IMAGES.

PROBLEM:
  Write `train_cnn()` that:
    1. torchvision.datasets.CIFAR10('./data', download=True)
    2. Model: Conv(3→16) → ReLU → MaxPool → Conv(16→32) → ReLU
       → MaxPool → Flatten → Linear → 10 classes
    3. CrossEntropyLoss + Adam; 3 epochs
    4. Returns (test_accuracy, model)

TRY THIS INPUT:
  ```python
  acc, model = train_cnn()
  print(f"{acc:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  ~0.60-0.65  (3 epochs is short — more epochs = higher)
  ```

HINT:
  32×32 → pool → 16×16 → pool → 8×8; 32×8×8 = 2048
  transforms.Compose([ToTensor(), Normalize(0.5,0.5)])

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# acc, m = train_cnn()
# print(acc)
