"""Level 03 — Data Visualization — Medium P02 Solution"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_dashboard():
    np.random.seed(42)
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Data Dashboard', fontsize=16)
    x = np.linspace(0, 10, 100)
    axes[0, 0].plot(x, np.sin(x), 'r-')
    axes[0, 0].set_title('Line Plot')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 1].scatter(np.random.randn(50), np.random.randn(50), alpha=0.6)
    axes[0, 1].set_title('Scatter Plot')
    axes[0, 1].grid(True, alpha=0.3)
    axes[1, 0].hist(np.random.randn(200), bins=20, edgecolor='black', alpha=0.7)
    axes[1, 0].set_title('Histogram')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 1].bar(['A', 'B', 'C', 'D'], [23, 45, 56, 78],
                   color=['red', 'blue', 'green', 'orange'])
    axes[1, 1].set_title('Bar Chart')
    axes[1, 1].grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('dashboard.png', dpi=150, bbox_inches='tight')
    plt.close()
    return fig

if __name__ == "__main__":
    fig = plot_dashboard()
    print(len(fig.axes))
