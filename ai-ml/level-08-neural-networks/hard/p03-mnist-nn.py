"""
LEVEL 08 — Neural Networks
HARD P03 — MNIST Digit Recognizer
========================================

CONCEPT:
  MNIST = 70,000 handwritten digits (28×28 grayscale).
  The "hello world" of deep learning.

  torchvision.datasets.MNIST downloads it automatically.
  Flatten 28×28 → 784 input features → Linear(784,10).

PROBLEM:
  Write `train_mnist()` that:
    1. Loads MNIST train/test (downloads to ./data)
    2. Flatten → Linear(784, 128) → ReLU → Linear(128, 10)
    3. CrossEntropyLoss + Adam(0.001); 3 epochs
    4. Returns (test_accuracy, model)

TRY THIS INPUT:
  ```python
  acc, model = train_mnist()
  print(f"{acc:.4f}")   # ~0.97 on first try!
  ```

EXPECTED OUTPUT:
  ```
  ~0.97
  ```

HINT:
  from torchvision import datasets, transforms
  datasets.MNIST('./data', train=True, download=True,
                 transform=transforms.ToTensor())

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# acc, model = train_mnist()
# print(acc)
