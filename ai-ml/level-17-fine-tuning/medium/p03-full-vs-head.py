"""
LEVEL 17 — Fine-Tuning / LoRA
MEDIUM P03 — Full Fine-Tune vs Head-Only
========================================

CONCEPT:
  Two ends of the fine-tuning spectrum:
    FULL FT   — every parameter trains. Max flexibility, max cost,
                max risk of forgetting the original task.
    HEAD-ONLY — backbone frozen, only the head trains. Cheap and
                safe, but limited by the frozen features.
  When the backbone's features already separate the new data,
  head-only matches full FT at a fraction of the cost.

PROBLEM:
  Write `full_vs_head(X_tr, y_tr, X_te, y_te)` that:
    1. Trains model A: full fine-tune (all params trainable)
    2. Trains model B: head-only (backbone model[0] frozen)
    Both: torch.manual_seed(42) before each build,
    nn.Sequential(Linear(8,32), ReLU, Linear(32,3)),
    CrossEntropyLoss + Adam(lr=0.01), full-batch, 100 epochs.
    3. Returns (full_acc, head_acc) — test accuracies as floats

  Signature:
      def full_vs_head(X_tr, y_tr, X_te, y_te):
          # returns: (float, float) — (full_finetune_acc, head_only_acc)

TRY THIS INPUT:
  ```python
  from sklearn.datasets import make_classification
  import torch
  X, y = make_classification(n_samples=200, n_features=8, n_classes=3,
                             n_informative=6, n_clusters_per_class=1,
                             class_sep=1.5, random_state=42)
  X = torch.tensor(X, dtype=torch.float32)
  y = torch.tensor(y, dtype=torch.long)
  fa, ha = full_vs_head(X[:150], y[:150], X[150:], y[150:])
  print(f"full={fa:.3f} head={ha:.3f}")
  ```

EXPECTED OUTPUT:
  ```
  full=0.980 head=1.000    (head-only can match — or beat — full FT here)
  ```

HINT:
  Write a small train(model) helper; freeze model[0] for the
  head-only run BEFORE creating the Adam optimizer.

CHECK: python3 check.py medium/p03
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
# print(full_vs_head(X[:150], y[:150], X[150:], y[150:]))
