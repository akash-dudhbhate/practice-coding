"""Level 20 — Deep Math for ML — Easy P02 Solution"""

import numpy as np


def project(v, u):
    return (np.dot(v, u) / np.dot(u, u)) * u


if __name__ == "__main__":
    v = np.array([3.0, 4.0])
    u = np.array([1.0, 0.0])
    print(project(v, u))
