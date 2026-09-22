"""
LEVEL 08 — Neural Networks
HARD P02 — PyTorch Full Training Loop
========================================

CONCEPT:
  A real PyTorch training loop has:
    - DataLoader (batches)
    - model.train() / model.eval() modes
    - Train loop + validation loop
    - Track losses for plotting

PROBLEM:
  Write `train()` that:
    1. make_classification(500, 10 features, seed=42) → tensors
    2. TensorDataset + DataLoader(batch_size=32, shuffle=True)
    3. Model: Linear(10,32) → ReLU → Linear(32,2)
    4. CrossEntropyLoss + Adam(0.001); 50 epochs
    5. Track train loss + val accuracy per epoch
    6. Returns (train_losses, val_accs)

TRY THIS INPUT:
  ```python
  losses, accs = train()
  print(f"{losses[0]:.4f} -> {losses[-1]:.4f}")
  print(f"{accs[-1]:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  0.xxxx -> 0.0xxx
  ~0.95+   (val accuracy near perfect)
  ```

HINT:
  TensorDataset(X_tensor, y_tensor)
  DataLoader(ds, batch_size=32, shuffle=True)
  model.eval() + torch.no_grad() for validation.

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# l, a = train()
# print(l[-1], a[-1])
