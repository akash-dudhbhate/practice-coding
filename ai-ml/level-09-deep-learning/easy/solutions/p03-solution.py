"""Level 09 Deep Learning — Easy P03 Solution"""

import numpy as np

def solve():
    # Max pooling and average pooling
    image = np.array([[1, 3, 2, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]])
    pool_size = 2
    h, w = image.shape
    # Max pooling
    max_pool = np.zeros((h // pool_size, w // pool_size))
    for i in range(h // pool_size):
        for j in range(w // pool_size):
            max_pool[i, j] = np.max(image[i*pool_size:(i+1)*pool_size, j*pool_size:(j+1)*pool_size])
    # Average pooling
    avg_pool = np.zeros((h // pool_size, w // pool_size))
    for i in range(h // pool_size):
        for j in range(w // pool_size):
            avg_pool[i, j] = np.mean(image[i*pool_size:(i+1)*pool_size, j*pool_size:(j+1)*pool_size])
    print("Original:")
    print(image)
    print("\nMax pooling:")
    print(max_pool)
    print("\nAverage pooling:")
    print(avg_pool)
    return max_pool, avg_pool

if __name__ == "__main__":
    solve()