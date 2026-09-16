"""Level 03 Visualization — Easy P02 Solution"""

import numpy as np
import matplotlib.pyplot as plt

def solve():
    np.random.seed(42)
    height = np.random.normal(170, 10, 100)
    weight = height * 0.6 + np.random.normal(0, 5, 100)
    gender = np.random.choice(['M', 'F'], 100)
    colors = {'M': 'blue', 'F': 'red'}
    plt.figure(figsize=(10, 6))
    for g in ['M', 'F']:
        mask = gender == g
        plt.scatter(height[mask], weight[mask], c=colors[g], label=g, alpha=0.6)
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')
    plt.title('Height vs Weight by Gender')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('scatter_plot.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Plot saved to scatter_plot.png")

if __name__ == "__main__":
    solve()