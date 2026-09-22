"""Level 02 — Python for ML — Easy P01 Solution"""

import numpy as np

def create_array():
    np.random.seed(42)
    return np.random.randint(0, 100, (4, 5))

if __name__ == "__main__":
    arr = create_array()
    print(arr.shape)
    print(arr.dtype)
    print(arr.ndim)
    print(arr.size)
    print(arr.mean(axis=0))
