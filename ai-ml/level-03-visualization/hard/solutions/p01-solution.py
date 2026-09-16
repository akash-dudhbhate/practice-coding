"""Level 03 — Data Visualization — Hard P01 Solution"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales():
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=90)
    data = pd.DataFrame({
        'date': dates,
        'revenue': np.random.normal(10000, 2000, 90),
        'product': np.random.choice(['A', 'B', 'C'], 90),
        'region': np.random.choice(['North', 'South', 'East', 'West'], 90)
    })
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Sales Dashboard', fontsize=16)
    data.groupby('date')['revenue'].sum().plot(ax=axes[0, 0])
    axes[0, 0].set_title('Revenue Over Time')
    data.groupby('product')['revenue'].sum().plot(kind='bar', ax=axes[0, 1])
    axes[0, 1].set_title('Revenue by Product')
    data.groupby('region')['revenue'].sum().plot(kind='pie', ax=axes[1, 0], autopct='%1.1f%%')
    axes[1, 0].set_title('Revenue by Region')
    axes[1, 0].set_ylabel('')
    pivot = data.groupby(['product', 'region'])['revenue'].sum().unstack()
    sns.heatmap(pivot, annot=True, ax=axes[1, 1], cmap='YlOrRd', fmt='.0f')
    axes[1, 1].set_title('Product × Region Revenue')
    plt.tight_layout()
    plt.savefig('sales_dashboard.png', dpi=150, bbox_inches='tight')
    plt.close()
    return data

if __name__ == "__main__":
    df = plot_sales()
    print(df.shape)
    print(f"{df['revenue'].mean():.1f}")
