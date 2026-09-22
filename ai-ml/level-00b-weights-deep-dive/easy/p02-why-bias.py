"""
LEVEL 00B — Weights & Training
EASY P02 (Chapter 2) — Why Bias?
=================================

CONCEPT:
  weight × input can never beat this fact: anything × 0 = 0.
  If an empty plot (0 sqft) costs $50k, w·x alone CANNOT produce
  50. You need a term that doesn't multiply by the input:

      prediction = weight × input + bias

  bias = the answer when every input is zero. On a graph it's the
  intercept — where the line starts. (w·m + c from school.)

PROBLEM:
  Write predict2(size, weight, bias) → returns weight*size + bias.
  Check the data that w·x alone failed: (0→50), (1000→250)
  uses weight=0.2, bias=50.

TRY THIS INPUT:
  ```python
  print(predict2(0, 0.2, 50))
  print(predict2(1000, 0.2, 50))
  print(predict2(1000, 0.2, 0))    # no bias — what was wrong before
  ```

EXPECTED OUTPUT:
  ```
  50.0
  250.0
  200.0
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement predict2(size, weight, bias)


def predict2(size, weight, bias):
    """prediction = weight × size + bias — now 0 input can give nonzero."""
    pass


# === TEST ===
# print(predict2(0, 0.2, 50))
# print(predict2(1000, 0.2, 50))
# print(predict2(1000, 0.2, 0))
