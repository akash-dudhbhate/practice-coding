"""Level 09 Deep Learning — Easy P01 Solution"""

import numpy as np

def solve():
    # Simple 3x3 convolution
    image = np.array([[1, 2, 3, 0],
                      [4, 5, 6, 0],
                      [7, 8, 9, 0],
                      [0, 0, 0, 0]])
    kernel = np.array([[1, 0, -1],
                       [1, 0, -1],
                       [1, 0, -1]])
    h, w = image.shape
    kh, kw = kernel.shape
    output = np.zeros((h - kh + 1, w - kw + 1))
    for i in range(h - kh + 1):
        for j in range(w - kw + 1):
            output[i, j] = np.sum(image[i:i+kh, j:j+kw] * kernel)
    print("Input image:")
    print(image)
    print("\nKernel:")
    print(kernel)
    print("\nOutput:")
    print(output)
    return output

if __name__ == "__main__":
    solve()