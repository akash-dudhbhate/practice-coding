"""
LEVEL 15 — Transformers from Scratch
EASY P03 — Softmax: Scores to Probabilities
========================================

CONCEPT:
  Attention produces raw scores like [2.1, -0.4, 5.0] — arbitrary
  numbers, possibly negative. Softmax turns them into a
  probability distribution: all positive, summing to 1. Those
  probabilities become the "how much do I attend" weights.

    softmax(x_i) = exp(x_i) / sum(exp(x_j))

  GOTCHA: exp() overflows for big inputs. Always subtract
  max(scores) first — the result is identical but stable.

PROBLEM:
  Write `softmax_row(scores)` that:
    - INPUT: 1D array of floats (attention scores)
    - OUTPUT: 1D array, same length, sums to 1.0
    - Must be numerically stable (subtract the max first)

TRY THIS INPUT:
  ```python
  print(softmax_row([1.0, 2.0, 3.0]))
  print(softmax_row([0.0, 0.0, 0.0]))
  print(softmax_row([1000.0, 1001.0]))   # must NOT overflow
  ```

EXPECTED OUTPUT:
  ```
  [0.09   0.2447 0.6652]
  [0.3333 0.3333 0.3333]
  [0.2689 0.7311]        (approximately — finite, sums to 1)
  ```

HINT:
  s = scores - scores.max(); e = np.exp(s); return e / e.sum()

CHECK: python3 check.py easy/p03
"""

import numpy as np

# === WRITE YOUR CODE BELOW ===

def softmax_row(scores):
    """scores: 1D array-like of floats -> 1D probability array."""
    # TODO: stable softmax (subtract max, exp, normalize)
    pass


# === TEST ===
# print(softmax_row([1.0, 2.0, 3.0]))
