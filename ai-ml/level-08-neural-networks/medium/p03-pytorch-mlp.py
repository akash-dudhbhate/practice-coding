"""
LEVEL 08 — Neural Networks
MEDIUM P03 — PyTorch MLP Classifier
========================================

CONCEPT:
  MLP (Multi-Layer Perceptron) = stack of Linear layers with
  activations between them:
    input → Linear → ReLU → Linear → output

  For classification: output layer gives logits, use
  CrossEntropyLoss (combines softmax + negative log likelihood).

PROBLEM:
  Write `train_mlp()` that:
    1. make_classification(200, 5 features, seed=42) → tensors
    2. Split 80/20
    3. Model: Linear(5,10) → ReLU → Linear(10,2)
    4. CrossEntropyLoss + Adam(lr=0.01), 200 epochs
    5. Returns test accuracy

TRY THIS INPUT:
  ```python
  acc = train_mlp()
  print(f"{acc:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  1.0000  (perfect — this dataset is easy for an MLP)
  ```

HINT:
  model = nn.Sequential(nn.Linear(5,10), nn.ReLU(), nn.Linear(10,2))
  Convert numpy → torch: torch.tensor(X, dtype=torch.float32)

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# acc = train_mlp()
# print(acc)
