"""Level 03 Visualization — Medium P01 Solution"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def solve():
    np.random.seed(42)
    data = pd.DataFrame({
        'feature_a': np.random.randn(100),
        'feature_b': np.random.randn(100),
        'feature_c': np.random.randn(100),
        'feature_d': np.random.randn(100),
        'target': np.random.randn(100)
    })
    corr = data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f',
                square=True, linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Plot saved to correlation_heatmap.png")

if __name__ == "__main__":
    solve()