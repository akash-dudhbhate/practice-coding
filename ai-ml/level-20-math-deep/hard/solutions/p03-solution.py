"""Level 20 — Deep Math for ML — Hard P03 Solution"""

import numpy as np


def adam_optimize(f, df, x0, lr=0.01, iters=200, beta1=0.9, beta2=0.999, eps=1e-8):
    x = np.array(x0, dtype=float)
    m = np.zeros_like(x)
    v = np.zeros_like(x)
    history = []
    for t in range(1, iters + 1):
        g = df(x)
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * g ** 2
        m_hat = m / (1 - beta1 ** t)
        v_hat = v / (1 - beta2 ** t)
        x = x - lr * m_hat / (np.sqrt(v_hat) + eps)
        history.append(f(x))
    return x, history


if __name__ == "__main__":
    f = lambda x: float(np.sum((x - 3.0) ** 2))
    df = lambda x: 2.0 * (x - 3.0)
    x, hist = adam_optimize(f, df, np.zeros(4), lr=0.1, iters=300)
    print(x)
    print(hist[-1])
