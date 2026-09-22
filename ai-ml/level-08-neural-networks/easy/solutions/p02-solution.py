"""Level 08 — Neural Networks — Easy P02 Solution"""

import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def relu(z):
    return np.maximum(0, z)

def tanh(z):
    return np.tanh(z)

if __name__ == "__main__":
    print(sigmoid(0))
    print(relu(-2))
    print(relu(3))
    print(tanh(0))
