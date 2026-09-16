"""
LEVEL 00 — Setup & Math
HARD P03 — Matrix Multiplication
========================================

CONCEPT:
  Matrix multiply: each output cell = row · column.

    A = [[1,2],[3,4]]   B = [[5,6],[7,8]]
    A·B[0][0] = 1×5 + 2×7 = 19
    A·B = [[19,22],[43,50]]

  Neural networks are giant matrix multiplications.
  (batch × features) @ (features × neurons) = outputs.

PROBLEM:
  Write `matmul(A, B)` — multiply two 2D lists (no numpy).
  Return the result as a 2D list.

TRY THIS INPUT:
  ```python
  A = [[1,2],[3,4]]
  B = [[5,6],[7,8]]
  print(matmul(A, B))   # [[19,22],[43,50]]
  ```

EXPECTED OUTPUT:
  ```
  [[19, 22], [43, 50]]
  ```

HINT:
  result[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(matmul([[1,2],[3,4]], [[5,6],[7,8]]))
