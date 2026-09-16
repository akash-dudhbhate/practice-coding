"""Level 03 Visualization — Medium P03 Solution"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def solve():
    np.random.seed(42)
    data = pd.DataFrame({
        'category': np.repeat(['A', 'B', 'C', 'D'], 50),
        'value': np.concatenate([
            np.random.normal(50, 10, 50),
            np.random.normal(60, 15, 50),
            np.random.normal(55, 12, 50),
            np.random.normal(70, 8, 50)
        ])
    })
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='category', y='value', data=data, palette='Set2')
    sns.swarmplot(x='category', y='value', data=data, color='black', alpha=0.5, size=3)
    plt.title('Distribution by Category')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.grid(True, alpha=0.3)
    plt.savefig('boxplot.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Plot saved to boxplot.png")

if __name__ == "__main__":
    solve()