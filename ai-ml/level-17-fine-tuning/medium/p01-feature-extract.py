"""
LEVEL 17 — Fine-Tuning / LoRA
MEDIUM P01 — Feature Extraction (Frozen Backbone + Trained Head)
========================================

CONCEPT:
  The cheapest fine-tuning strategy: treat the pretrained backbone
  as a FIXED feature extractor. Freeze it completely, then train
  only the classification head on your new data. No gradients flow
  into the backbone, so its learned features are preserved exactly.

PROBLEM:
  Write `feature_extract_finetune(X_tr, y_tr, X_te, y_te)` that:
    1. torch.manual_seed(42), builds
       nn.Sequential(Linear(8,32), ReLU, Linear(32,3))
    2. Freezes the backbone (model[0]) — only the head trains
    3. Trains: CrossEntropyLoss + Adam(lr=0.01) on ONLY the
       trainable params, full-batch, 100 epochs
    4. Returns test accuracy as a float in [0, 1]

  Signature:
      def feature_extract_finetune(X_tr, y_tr, X_te, y_te):
          # X_tr/X_te: float tensors (N,8)   y_tr/y_te: long tensors (N,)
          # returns: float — accuracy on (X_te, y_te)

TRY THIS INPUT:
  ```python
  from sklearn.datasets import make_classification
  import torch
  X, y = make_classification(n_samples=200, n_features=8, n_classes=3,
                             n_informative=6, n_clusters_per_class=1,
                             class_sep=1.5, random_state=42)
  X = torch.tensor(X, dtype=torch.float32)
  y = torch.tensor(y, dtype=torch.long)
  acc = feature_extract_finetune(X[:150], y[:150], X[150:], y[150:])
  print(f"{acc:.3f}")
  ```

EXPECTED OUTPUT:
  ```
  1.000   (frozen random features + a trained head already separates this data)
  ```

HINT:
  optimizer = Adam([p for p in model.parameters() if p.requires_grad], lr=0.01)
  eval: model(X_te).argmax(dim=1) == y_te → .float().mean().item()

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# from sklearn.datasets import make_classification
# import torch
# X, y = make_classification(n_samples=200, n_features=8, n_classes=3,
#                            n_informative=6, n_clusters_per_class=1,
#                            class_sep=1.5, random_state=42)
# X = torch.tensor(X, dtype=torch.float32); y = torch.tensor(y, dtype=torch.long)
# print(feature_extract_finetune(X[:150], y[:150], X[150:], y[150:]))
