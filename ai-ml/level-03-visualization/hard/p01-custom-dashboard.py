"""
LEVEL 03 — Data Visualization
HARD P01 — 4-Panel Sales Dashboard
========================================

CONCEPT:
  groupby aggregates data: df.groupby('col')['val'].sum()
  plot(kind='bar'/'pie'/'line') — pandas quick plots.
  pd.date_range('2024-01-01', periods=90) — date index.

PROBLEM:
  Write `plot_sales()` that:
    1. np.random.seed(42); 90 days of sales data:
       date, revenue ~ normal(10000, 2000),
       product A/B/C, region North/South/East/West
    2. 2×2 figure:
       [0,0] revenue over time (line)
       [0,1] revenue by product (bar)
       [1,0] revenue by region (pie, autopct)
       [1,1] product × region revenue heatmap
    3. Save 'sales_dashboard.png', show, return the DataFrame

TRY THIS INPUT:
  ```python
  df = plot_sales()
  print(df.shape)             # (90, 4)
  print(df['revenue'].mean()) # ~10000
  ```

EXPECTED OUTPUT:
  ```
  (90, 4)
  ~10000.0
  ```

HINT:
  data.groupby('product')['revenue'].sum().plot(kind='bar', ax=axes[0,1])
  For the heatmap: groupby(['product','region'])['revenue'].sum().unstack()

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# df = plot_sales()
# print(df.shape)
