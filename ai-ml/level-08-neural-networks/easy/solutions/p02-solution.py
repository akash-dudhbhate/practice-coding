"""Level 08 Neural Networks — Easy P02 Solution"""

import numpy as np
import matplotlib.pyplot as plt

def solve():
    x = np.linspace(-5, 5, 100)
    sigmoid = 1 / (1 + np.exp(-x))
    relu = np.maximum(0, x)
    tanh = np.tanh(x)
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.plot(x, sigmoid)
    plt.title('Sigmoid')
    plt.grid(True, alpha=0.3)
    plt.subplot(1, 3, 2)
    plt.plot(x, relu)
    plt.title('ReLU')
    plt.grid(True, alpha=0.3)
    plt.subplot(1, 3, 3)
    plt.plot(x, tanh)
    plt.title('Tanh')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('activations.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Activation functions plotted")

if __name__ == "__main__":
    solve()