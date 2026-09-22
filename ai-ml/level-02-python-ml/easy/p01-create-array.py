"""
LEVEL 02 — Python for ML
EASY P01 — Create a NumPy Array
========================================

CONCEPT:
  NumPy arrays are the foundation of ML in Python. Unlike Python lists,
  they store numbers in a grid and let you do math on the whole array
  at once (fast!).

  Key properties:
    - shape: dimensions, e.g. (4, 5) = 4 rows × 5 cols
    - dtype: data type, e.g. int64
    - ndim: number of dimensions
    - size: total elements
    - mean(axis=0): mean of each column
    - seed: makes random numbers reproducible

PROBLEM:
  Write `create_array()` that:
    1. Sets random seed to 42 (np.random.seed(42))
    2. Creates a 4×5 array of random integers from 0-99
    3. Returns the array

TRY THIS INPUT:
  ```python
  arr = create_array()
  print(arr.shape)          # (4, 5)
  print(arr.dtype)          # int64
  print(arr.ndim)           # 2
  print(arr.size)           # 20
  print(arr.mean(axis=0))   # column means
  ```

EXPECTED OUTPUT:
  ```
  (4, 5)
  int64
  2
  20
  [52.5 68.5 52.5 44.  48. ]
  ```
  The array itself (for your reference):
  [[51 92 14 71 60]
   [20 82 86 74 74]
   [87 99 23  2 21]
   [52  1 87 29 37]]

HINT:
  np.random.seed(42) then np.random.randint(0, 100, size=(4, 5))

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# Uncomment to test:
# arr = create_array()
# print(arr.shape)
# print(arr.mean(axis=0))
