"""Level 20 — Deep Math for ML — Hard P01 Solution"""

import numpy as np


def newton_sqrt(n, x0, iters=20):
    x = float(x0)
    for i in range(1, iters + 1):
        x_new = 0.5 * (x + n / x)
        if abs(x_new - x) < 1e-12:
            return x_new, i
        x = x_new
    return x, iters


if __name__ == "__main__":
    r, it = newton_sqrt(2.0, 1.0)
    print(r, it)
