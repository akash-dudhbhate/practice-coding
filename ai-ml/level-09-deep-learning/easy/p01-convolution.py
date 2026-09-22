"""
LEVEL 09 — Deep Learning
EASY P01 — Convolution (The Filter)
========================================

CONCEPT:
  Convolution = slide a small kernel over the image, computing
  dot products at each position. Detects edges, textures, shapes.

  A vertical-edge kernel [1,0,-1] finds left-right brightness changes.

PROBLEM:
  Write `convolve(image, kernel)` that does 2D convolution:
    output[i][j] = sum of (image_patch × kernel) at each position
    (valid convolution — no padding)

TRY THIS INPUT:
  ```python
  img = np.array([[1,2,3,0],[4,5,6,0],[7,8,9,0],[0,0,0,0]])
  kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
  out = convolve(img, kernel)
  print(out.shape)    # (2, 2)
  print(out[0][0])    # -6.0 (edge detected!)
  ```

EXPECTED OUTPUT:
  ```
  (2, 2)
  -6.0
  ```
  (strong negative values = vertical edge detected)

HINT:
  result[i,j] = np.sum(image[i:i+3, j:j+3] * kernel)
  output size = (H-2, W-2) for 3×3 kernel, no padding

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import numpy as np
# img = np.array([[1,2,3,0],[4,5,6,0],[7,8,9,0],[0,0,0,0]])
# kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
# print(convolve(img, kernel))
