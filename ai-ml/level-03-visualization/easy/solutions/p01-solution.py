"""Level 03 — Data Visualization — Easy P01 Solution"""

import numpy as np
import matplotlib
matplotlib.use('Agg')  # headless — remove if you want plt.show()
import matplotlib.pyplot as plt

def plot_trig():
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
    plt.close()
    return x

if __name__ == "__main__":
    x = plot_trig()
    print(len(x))
    print(x[0], x[-1])
