"""Level 03 Visualization — Hard P02 Solution"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def solve():
    np.random.seed(42)
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.linspace(0, 2 * np.pi, 100)
    line, = ax.plot(x, np.sin(x))
    ax.set_ylim(-1.5, 1.5)
    ax.set_title('Animated Sine Wave')
    ax.grid(True, alpha=0.3)
    def update(frame):
        line.set_ydata(np.sin(x + frame / 10))
        return line,
    anim = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
    plt.show()
    print("Animation displayed")

if __name__ == "__main__":
    solve()