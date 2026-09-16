"""Level 03 Visualization — Hard P01 Solution"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def solve():
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
    # Revenue over time
    data.groupby('date')['revenue'].sum().plot(ax=axes[0, 0], title='Revenue Over Time')
    # Revenue by product
    data.groupby('product')['revenue'].sum().plot(kind='bar', ax=axes[0, 1], title='Revenue by Product')
    # Revenue by region
    data.groupby('region')['revenue'].sum().plot(kind='pie', ax=axes[1, 0], title='Revenue by Region', autopct='%1.1f%%')
    # Correlation
    numeric_data = data.groupby(['product', 'region'])['revenue'].sum().unstack()
    sns.heatmap(numeric_data, annot=True, ax=axes[1, 1], cmap='YlOrRd')
    axes[1, 1].set_title('Product × Region Revenue')
    plt.tight_layout()
    plt.savefig('sales_dashboard.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Plot saved to sales_dashboard.png")

if __name__ == "__main__":
    solve()