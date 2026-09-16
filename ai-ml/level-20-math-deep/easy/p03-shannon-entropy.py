"""
LEVEL 20 — Deep Math for ML
EASY P03 — Shannon Entropy
========================================

CONCEPT:
  Entropy H(p) = -Σ pᵢ log₂(pᵢ) measures the uncertainty of a
  probability distribution, in BITS.
    - Fair coin [0.5, 0.5]        → 1 bit (max for 2 outcomes)
    - Certain outcome [1, 0, 0]   → 0 bits
    - Uniform over 4 [¼,¼,¼,¼]    → 2 bits

  Entropy shows up everywhere: decision-tree splits, language-model
  perplexity (2^entropy), and RL exploration bonuses.

  Edge case: 0·log(0) is defined as 0 — you must mask zero entries
  before taking the log, or you'll get NaN.

PROBLEM:
  Write `entropy(p)` that returns the Shannon entropy of a
  probability vector, in bits. Handle zeros safely.

TRY THIS INPUT:
  ```python
  print(entropy(np.array([0.5, 0.5])))       # 1.0
  print(entropy(np.array([0.25]*4)))          # 2.0
  print(entropy(np.array([1.0, 0.0, 0.0])))   # 0.0 — no crash!
  ```

EXPECTED OUTPUT:
  ```
  1.0
  2.0
  0.0
  ```

HINT:
  p = p[p > 0]                  # drop zeros first
  return -np.sum(p * np.log2(p))

CHECK: python3 check.py easy/p03
"""

import numpy as np


# === WRITE YOUR CODE BELOW ===
def entropy(p):
    # TODO: -sum(p_i * log2(p_i)), skipping zero probabilities
    pass


# === TEST ===
# print(entropy(np.array([0.5, 0.5])))
# print(entropy(np.array([0.25]*4)))
# print(entropy(np.array([1.0, 0.0, 0.0])))
