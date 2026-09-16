"""Level 03 Visualization — Easy P01 Solution"""

import numpy as np
import matplotlib.pyplot as plt

def solve():
    x = np.linspace(0, 10, 100)
    plt.figure(figsize=(10, 6))
    plt.plot(x, np.sin(x), label='sin(x)', linewidth=2)
    plt.plot(x, np.cos(x), label='cos(x)', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sine and Cosine Waves')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('trig_plot.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Plot saved to trig_plot.png")

if __name__ == "__main__":
    solve()