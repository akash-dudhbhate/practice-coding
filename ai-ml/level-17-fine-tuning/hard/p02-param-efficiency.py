"""
LEVEL 17 — Fine-Tuning / LoRA
HARD P02 — Parameter Efficiency Report
========================================

CONCEPT:
  The selling point of LoRA is parameter efficiency. The metric:
      ratio = trainable_params(lora_model) / trainable_params(full_model)
  On real LLMs this ratio is often 0.001–0.01 — you train <1% of
  the weights and still adapt the model.

PROBLEM:
  Write `param_efficiency(model, lora_model)` that returns a dict:
      {
        'full_trainable': int,   # params with requires_grad in model
        'lora_trainable': int,   # params with requires_grad in lora_model
        'ratio': float,          # lora_trainable / full_trainable
      }

  Signature:
      def param_efficiency(model, lora_model):
          # model:      normally-trainable nn.Module
          # lora_model: nn.Module with most params frozen
          # returns: dict with the 3 keys above

TRY THIS INPUT:
  ```python
  import torch, torch.nn as nn
  torch.manual_seed(42)
  model = nn.Sequential(nn.Linear(8,32), nn.ReLU(), nn.Linear(32,3))
  torch.manual_seed(42)
  lora_model = nn.Sequential(nn.Linear(8,32), nn.ReLU(), nn.Linear(32,3))
  for p in lora_model[0].parameters(): p.requires_grad_(False)
  print(param_efficiency(model, lora_model))
  ```

EXPECTED OUTPUT:
  ```
  {'full_trainable': 387, 'lora_trainable': 99, 'ratio': 0.2558...}
  ```

HINT:
  Filter `model.parameters()` on `p.requires_grad`, sum `p.numel()`.

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import torch, torch.nn as nn
# torch.manual_seed(42)
# model = nn.Sequential(nn.Linear(8,32), nn.ReLU(), nn.Linear(32,3))
# lora_model = nn.Sequential(nn.Linear(8,32), nn.ReLU(), nn.Linear(32,3))
# for p in lora_model[0].parameters(): p.requires_grad_(False)
# print(param_efficiency(model, lora_model))
