"""
LEVEL 09 — Deep Learning
EASY P03 — Max Pooling
========================================

CONCEPT:
  Pooling downsamples: take the max in each 2×2 window.
  Keeps the strongest signal, halves the size. 4×4 → 2×2.

  Why: makes the network focus on "is a feature present?" not
  "exactly where is it?" — translation invariance.

PROBLEM:
  Write `max_pool(image)` that does 2×2 max pooling
  on a 2D array (even dimensions).

TRY THIS INPUT:
  ```python
  img = np.array([[1,3,2,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
  out = max_pool(img)
  print(out)   # [[6,8],[14,16]]
  ```

EXPECTED OUTPUT:
  ```
  [[ 6.  8.]
   [14. 16.]]
  ```
  (top-left 2×2 block [1,3,5,6] → max is 6)

HINT:
  Loop over i in range(0, H, 2), j in range(0, W, 2):
  result[i//2, j//2] = image[i:i+2, j:j+2].max()

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import numpy as np
# img = np.array([[1,3,2,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# print(max_pool(img))
