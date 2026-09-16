"""Level 03 Visualization — Hard P03 Solution"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def solve():
    matplotlib.rcParams['font.family'] = 'serif'
    matplotlib.rcParams['font.size'] = 12
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, np.sin(x), 'b-', linewidth=2, label='sin(x)')
    ax.plot(x, np.cos(x), 'r--', linewidth=2, label='cos(x)')
    ax.fill_between(x, np.sin(x), np.cos(x), alpha=0.2, color='purple')
    ax.set_xlabel('X Axis Label', fontsize=14)
    ax.set_ylabel('Y Axis Label', fontsize=14)
    ax.set_title('Publication Quality Figure', fontsize=16)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig('publication_figure.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("Plot saved to publication_figure.png at 300 DPI")

if __name__ == "__main__":
    solve()