"""
LEVEL 17 — Fine-Tuning / LoRA
HARD P03 — Catastrophic Forgetting: Full FT vs LoRA
========================================

CONCEPT:
  Fine-tune a model on a NEW task and it forgets the OLD one —
  "catastrophic forgetting". Full FT overwrites every weight, so
  the original skill is gone for good. LoRA freezes the base
  weights: the adapter may still distort behavior while attached,
  but REMOVE the adapter and the original model comes back intact.
  Forgetting with LoRA isn't avoided — it's *reversible*.

PROBLEM:
  Write `catastrophic_forgetting(orig_data, new_data)` that:
    1. orig_data = (X, y), new_data = (X2, y2) — tensor pairs
    2. Split orig into first-150 train / last-50 test
    3. PRETRAIN: torch.manual_seed(42), build
       nn.Sequential(Linear(8,32), ReLU, Linear(32,3)), train on
       orig train split (Adam 0.01, 100 epochs) → orig test acc
    4. FULL FT: deepcopy the pretrained model, train ALL params on
       new_data (100 epochs) → orig test acc again (should crash)
    5. LORA FT: deepcopy the pretrained model, wrap BOTH Linear
       layers with rank-4 LoRA adapters, train only A/B params on
       new_data (lr=0.01, 50 epochs) → orig test acc with adapter
    6. RECOVER: rebuild a plain Sequential from the frozen base
       weights inside the LoRA wrappers → orig test acc restored
    7. Return dict with keys:
         'orig_before', 'after_full', 'after_lora', 'lora_recovered'

  Signature:
      def catastrophic_forgetting(orig_data, new_data):
          # orig_data, new_data: (X, y) tuples of tensors
          # returns: dict of 4 floats

TRY THIS INPUT:
  ```python
  from sklearn.datasets import make_classification
  import torch
  X, y = make_classification(n_samples=200, n_features=8, n_classes=3,
                             n_informative=6, n_clusters_per_class=1,
                             class_sep=1.5, random_state=42)
  X2, y2 = make_classification(n_samples=150, n_features=8, n_classes=3,
                               n_informative=6, n_clusters_per_class=1,
                               class_sep=1.5, random_state=7)
  orig = (torch.tensor(X, dtype=torch.float32),
          torch.tensor(y, dtype=torch.long))
  new = (torch.tensor(X2, dtype=torch.float32),
         torch.tensor(y2, dtype=torch.long))
  print(catastrophic_forgetting(orig, new))
  ```

EXPECTED OUTPUT (approx):
  ```
  {'orig_before': 0.98, 'after_full': 0.06,
   'after_lora': 0.20, 'lora_recovered': 0.98}
  ```

HINT:
  copy.deepcopy before wrapping. For step 6:
  nn.Sequential(lora0.base, nn.ReLU(), lora2.base) — the base
  weights were never updated.

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# See docstring above for the full input example.
