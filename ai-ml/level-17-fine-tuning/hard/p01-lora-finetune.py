"""
LEVEL 17 — Fine-Tuning / LoRA
HARD P01 — LoRA Fine-Tuning End-to-End
========================================

CONCEPT:
  Real LoRA fine-tuning: wrap a backbone layer with a low-rank
  adapter, freeze ALL base weights, and train only the tiny A/B
  matrices (plus the head). You get near-full-FT accuracy while
  touching <10% of the parameters.

PROBLEM:
  Write `lora_finetune(X_tr, y_tr, X_te, y_te, rank=4)` that:
    1. torch.manual_seed(42), builds
       nn.Sequential(Linear(8,32), ReLU, Linear(32,3))
    2. Replaces model[0] with a LoRA wrapper:
         - frozen base Linear(8,32) (copy the original weights in)
         - trainable A (rank×8), B (32×rank); B starts at 0
         - forward: base(x) + (x @ A.T) @ B.T
    3. Trains ONLY the trainable params (A, B, and head):
       CrossEntropyLoss + Adam(lr=0.01), full-batch, 100 epochs
    4. Returns test accuracy as a float

  Signature:
      def lora_finetune(X_tr, y_tr, X_te, y_te, rank=4):
          # returns: float — test accuracy

TRY THIS INPUT:
  ```python
  from sklearn.datasets import make_classification
  import torch
  X, y = make_classification(n_samples=200, n_features=8, n_classes=3,
                             n_informative=6, n_clusters_per_class=1,
                             class_sep=1.5, random_state=42)
  X = torch.tensor(X, dtype=torch.float32)
  y = torch.tensor(y, dtype=torch.long)
  acc = lora_finetune(X[:150], y[:150], X[150:], y[150:], rank=4)
  print(f"{acc:.3f}")
  ```

EXPECTED OUTPUT:
  ```
  0.980   (259 trainable params vs 387 for full FT — same accuracy)
  ```

HINT:
  Reuse the LoRALinear idea from medium/p02. After wrapping,
  copy model[0]'s old weights into lora.base so the adapted model
  starts identical to the original.

CHECK: python3 check.py hard/p01
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
# print(lora_finetune(X[:150], y[:150], X[150:], y[150:]))
