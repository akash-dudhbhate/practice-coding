"""
LEVEL 17 PROJECT — Fine-Tuning Pipeline
========================================

Build a mini fine-tuning pipeline that ties the whole level
together: freeze → replace head → LoRA → compare → forgetting.

BUILD class `FineTuner`:
  - __init__(X_tr, y_tr, X_te, y_te):
      stores the data, builds + PRETRAINS a base model
      nn.Sequential(Linear(8,32), ReLU, Linear(32,3))
      (torch.manual_seed(42); Adam lr=0.01, 100 epochs)
  - finetune(mode, epochs=100):
      deepcopy the pretrained base, then adapt it:
        'full' → train all params
        'head' → freeze backbone, train only last layer
        'lora' → wrap both Linears with rank-4 adapters,
                 train only A/B params (50 epochs is enough)
      returns test accuracy (float)
  - report():
      runs all three modes, prints a table like:
        mode    trainable_params    test_acc
        full    387                 0.98
        head    99                  1.00
        lora    259                 0.96

  Plus a LoRALinear class (from medium/p02): frozen base Linear +
  trainable A (rank×in), B (out×rank, init 0), forward
  base(x) + (x @ A.T) @ B.T.

DATA (put at top of file):
  X, y = make_classification(n_samples=200, n_features=8, n_classes=3,
                             n_informative=6, n_clusters_per_class=1,
                             class_sep=1.5, random_state=42)
  → float32 / long tensors, split [:150] train / [150:] test

TEST RUN:
  ```python
  ft = FineTuner(X_tr, y_tr, X_te, y_te)
  ft.report()
  ```

EXPECTED (approx):
  ```
  mode    trainable   test_acc
  full    387         0.98
  head    99          1.00
  lora    259         0.96
  ```

STRETCH:
  - Add mode='both': LoRA on hidden layer + trainable head
  - Track forgetting: after each finetune on NEW data
    (make_classification random_state=7), eval orig acc and
    show lora_recovered == orig_before
"""

# === WRITE YOUR CODE BELOW ===
import copy

import torch
import torch.nn as nn
from sklearn.datasets import make_classification


# TODO: build the dataset (see spec above)


class LoRALinear(nn.Module):
    def __init__(self, linear, rank):
        super().__init__()
        # TODO: frozen base + trainable A (rank×in), B (out×rank)=0
        pass

    def forward(self, x):
        # TODO: base(x) + (x @ A.T) @ B.T
        pass


class FineTuner:
    def __init__(self, X_tr, y_tr, X_te, y_te):
        # TODO: store data; seed, build + pretrain self.base
        pass

    def _train(self, model, epochs, lr=0.01):
        # TODO: Adam on trainable params, CrossEntropyLoss, full batch
        pass

    def _acc(self, model, X, y):
        # TODO: argmax accuracy under torch.no_grad()
        pass

    def finetune(self, mode, epochs=100):
        # TODO: deepcopy base, apply mode-specific freezing/wrapping,
        #       train, return test acc
        pass

    def report(self):
        # TODO: run all 3 modes, print table with trainable counts
        pass


if __name__ == "__main__":
    # TODO: build data, create FineTuner, call report()
    pass
