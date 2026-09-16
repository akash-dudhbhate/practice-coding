"""Level 03 — Data Visualization — Medium P01 Solution"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def plot_corr():
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
    plt.close()
    return corr

if __name__ == "__main__":
    c = plot_corr()
    print(c.shape)
    print(c.loc['feature_a', 'feature_a'])
