# Level 17 — Fine-Tuning / LoRA

## What You'll Learn
- Freezing layers — `requires_grad=False` on a pretrained backbone
- Counting trainable vs total parameters
- Head replacement — swap the final classifier for a new task
- Feature extraction — frozen backbone + trained head
- LoRA — Low-Rank Adaptation: train tiny A/B matrices instead of W
- Full fine-tune vs head-only vs LoRA trade-offs
- Parameter efficiency — how few weights can you get away with?
- Catastrophic forgetting — and why LoRA keeps the base model recoverable

## Prerequisites
- Level 08 (PyTorch: nn.Linear, training loops, CrossEntropyLoss)
- Level 09 (transfer learning intuition helps)
- `pip install torch scikit-learn` (CPU is fine)

## Setup

All problems use the same tiny "pretrained" model and dataset:

```python
import torch, torch.nn as nn
from sklearn.datasets import make_classification

# Data — a small 3-class problem
X, y = make_classification(n_samples=200, n_features=8, n_classes=3,
                           n_informative=6, n_clusters_per_class=1,
                           class_sep=1.5, random_state=42)
X = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.long)
X_tr, y_tr, X_te, y_te = X[:150], y[:150], X[150:], y[150:]

# Model — our stand-in for a big pretrained net
torch.manual_seed(42)
model = nn.Sequential(nn.Linear(8, 32), nn.ReLU(), nn.Linear(32, 3))
```

Training convention everywhere: `CrossEntropyLoss` + `Adam(lr=0.01)`,
full-batch, ~50–100 epochs, always `torch.manual_seed(42)` before
building a model.

## Problems

### Easy
1. `easy/p01-freeze-backbone.py` — `freeze_backbone(model)` → freeze all but last layer
2. `easy/p02-count-trainable.py` — `count_trainable(model)` → (total, trainable)
3. `easy/p03-replace-head.py` — `replace_head(model, n_classes)` → new final Linear

### Medium
4. `medium/p01-feature-extract.py` — `feature_extract_finetune(...)` → frozen backbone, train head
5. `medium/p02-lora-linear.py` — `lora_linear(in_f, out_f, rank)` → LoRA-wrapped Linear
6. `medium/p03-full-vs-head.py` — `full_vs_head(...)` → compare both strategies

### Hard
7. `hard/p01-lora-finetune.py` — `lora_finetune(..., rank=4)` → LoRA on hidden layer
8. `hard/p02-param-efficiency.py` — `param_efficiency(model, lora_model)` → trainable counts
9. `hard/p03-catastrophic-forgetting.py` — `catastrophic_forgetting(...)` → forgetting vs LoRA

### Project
`project/` — Build a fine-tuning pipeline supporting `full` / `head` / `lora`
modes with an accuracy + parameter report.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
