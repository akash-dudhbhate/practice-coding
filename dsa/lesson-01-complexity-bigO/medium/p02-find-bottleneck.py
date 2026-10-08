"""
LESSON 01 — Time/Space Complexity & Big-O
MEDIUM P02 — Find The Bottleneck
============================================

CONCEPT:
  Real programs run in phases. The Big-O of the whole program is the
  Big-O of the LARGEST phase — lower terms get dropped. If your program
  does O(n) + O(n log n) + O(n^2) work, it is O(n^2).

PROBLEM:
  Write two functions:
    `phase_ops(n: int) -> dict` returning
        {"linear": n, "nlogn": n*log2(n) as int, "quadratic": n*n}
    `bottleneck_phase(n: int) -> str` returning the key of the phase
        with the most operations.

TRY THIS INPUT:
  ```python
  print(phase_ops(8))
  print(bottleneck_phase(8))
  print(bottleneck_phase(2))
  ```

EXPECTED OUTPUT:
  ```
  {'linear': 8, 'nlogn': 24, 'quadratic': 64}
  quadratic
  quadratic
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
