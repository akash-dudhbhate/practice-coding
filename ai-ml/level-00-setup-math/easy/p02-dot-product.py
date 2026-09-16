"""
LEVEL 00 — Setup & Math
EASY P02 — Dot Product
========================================

CONCEPT:
  The dot product of two vectors = multiply matching elements,
  then sum the results:

    a = [1, 2, 3]
    b = [4, 5, 6]
    a · b = 1×4 + 2×5 + 3×6 = 4 + 10 + 18 = 32

  THIS IS THE SINGLE MOST IMPORTANT OPERATION IN ML.
  Every neuron computes: output = weights · inputs + bias.

PROBLEM:
  Write `dot(a, b)` that computes the dot product of two lists
  WITHOUT using numpy's np.dot (do it yourself).

TRY THIS INPUT:
  ```python
  print(dot([1,2,3], [4,5,6]))    # 32
  print(dot([0,1], [5,5]))        # 5
  print(dot([2,0,2], [1,1,1]))    # 4
  ```

EXPECTED OUTPUT:
  ```
  32
  5
  4
  ```

HINT:
  sum(x * y for x, y in zip(a, b))

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(dot([1,2,3], [4,5,6]))
