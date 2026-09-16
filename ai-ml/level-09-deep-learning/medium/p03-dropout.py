"""
LEVEL 09 — Deep Learning
MEDIUM P03 — Dropout Regularization
========================================

CONCEPT:
  Dropout randomly kills a fraction of neurons during training.
  The network can't rely on any single neuron → learns redundant,
  robust features. Only active during model.train(), not .eval().

  nn.Dropout(0.5) — randomly zero 50% of activations each pass.

PROBLEM:
  Write `compare_dropout()` that trains two MLPs on
  make_classification(200, 20 features, seed=42):
    Model A: Linear(20→64) → ReLU → Linear(64→2)
    Model B: Linear(20→64) → ReLU → Dropout(0.5) → Linear(64→2)
    200 epochs, Adam(0.01). Returns (acc_A, acc_B)

TRY THIS INPUT:
  ```python
  a, b = compare_dropout()
  print(f"No dropout: {a:.4f}  With dropout: {b:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  ~0.9x ~0.9x  (may be similar or dropout slightly lower —
   it fights overfitting, which matters more on harder data)
  ```

HINT:
  Model trains in .train() mode — dropout is active.
  Always call .eval() before testing.

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# a, b = compare_dropout()
# print(a, b)
