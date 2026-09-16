"""Level 03 — Data Visualization — Hard P02 Solution"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate():
    x = np.linspace(0, 2 * np.pi, 100)
    fig, ax = plt.subplots(figsize=(10, 6))
    line, = ax.plot(x, np.sin(x))
    ax.set_ylim(-1.5, 1.5)
    ax.set_title('Animated Sine Wave')
    ax.grid(True, alpha=0.3)
    def update(frame):
        line.set_ydata(np.sin(x + frame / 10))
        return line,
    anim = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
    # Save as GIF instead of showing (headless)
    anim.save('sine_wave.gif', writer='pillow', fps=20)
    plt.close()
    return x

if __name__ == "__main__":
    x = animate()
    print(len(x))
    print(f"{x[-1]:.4f}")
