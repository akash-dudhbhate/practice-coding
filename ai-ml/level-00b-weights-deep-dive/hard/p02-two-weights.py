"""
LEVEL 00B — Weights & Training
HARD P02 (Chapter 8) — Two Weights: the Dot Product
=====================================================

CONCEPT:
  Real inputs have many features. prediction = w₁·size + w₂·rooms + b.
  The pattern w₁x₁+w₂x₂+... is the DOT PRODUCT — each input votes,
  its weight says how loudly. Each weight updates with ITS OWN input:
      wᵢ −= step × res × xᵢ
  A neuron = dot product + bias. You're at the atom of deep learning.

PROBLEM:
  Write predict_multi(features, weights, bias) → dot + bias.
  features and weights are same-length lists.

TRY THIS INPUT:
  ```python
  print(predict_multi([1500, 3, 10], [0.15, 5.0, -0.5], 10.0))
  #                     size  rooms  age
  ```

EXPECTED OUTPUT:
  ```
  245.0
  ```
  (0.15·1500 + 5·3 + (−0.5)·10 + 10 = 225 + 15 − 5 + 10 = 245)

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement predict_multi(features, weights, bias)


def predict_multi(features, weights, bias):
    """prediction = Σ wᵢxᵢ + b — one neuron, three votes."""
    pass


# === TEST ===
# print(predict_multi([1500, 3, 10], [0.15, 5.0, -0.5], 10.0))
