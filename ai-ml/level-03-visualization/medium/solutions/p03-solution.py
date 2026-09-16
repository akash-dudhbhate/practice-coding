"""Level 03 — Data Visualization — Medium P03 Solution"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def plot_box():
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
    sns.boxplot(x='category', y='value', data=data, hue='category', palette='Set2', legend=False)
    sns.swarmplot(x='category', y='value', data=data, color='black', alpha=0.5, size=3)
    plt.title('Distribution by Category')
    plt.savefig('boxplot.png', dpi=150, bbox_inches='tight')
    plt.close()
    return data

if __name__ == "__main__":
    df = plot_box()
    print(df.shape)
    print(df.groupby('category')['value'].mean())
