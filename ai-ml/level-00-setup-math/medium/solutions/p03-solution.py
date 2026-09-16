"""Level 00 — Setup & Math — Medium P03 Solution"""

import math

def euclidean(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

if __name__ == "__main__":
    print(euclidean([0, 0], [3, 4]))
    print(euclidean([1, 1, 1], [1, 1, 1]))
