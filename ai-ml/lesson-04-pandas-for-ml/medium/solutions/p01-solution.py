"""
Lesson 04 - Medium P01
GroupBy operations:
  - Total revenue per product
  - Average quantity per region
  - Count of transactions per product per region

Solution:
  Use df.groupby() with .sum(), .mean(), .count() / .size() aggregations.
"""

import pandas as pd

# ---------------------------------------------------------------------------
# 1. Create a sales dataset
# ---------------------------------------------------------------------------
data = {
    "product": ["A", "B", "A", "C", "B", "A", "C", "B", "C", "A"],
    "region": ["North", "South", "North", "East", "South", "West", "East", "West", "North", "South"],
    "quantity": [10, 5, 8, 3, 7, 12, 6, 4, 9, 15],
    "revenue": [1000, 500, 800, 300, 700, 1200, 600, 400, 900, 1500],
}
df = pd.DataFrame(data)
print("Sales DataFrame:")
print(df)
print()

# ---------------------------------------------------------------------------
# 2. Total revenue per product
# ---------------------------------------------------------------------------
# Solution: groupby('product') then sum the 'revenue' column.
revenue_per_product = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
print("Total revenue per product:")
print(revenue_per_product)
print()

# ---------------------------------------------------------------------------
# 3. Average quantity per region
# ---------------------------------------------------------------------------
# Solution: groupby('region') then mean the 'quantity' column.
avg_qty_per_region = df.groupby("region")["quantity"].mean().sort_values(ascending=False)
print("Average quantity per region:")
print(avg_qty_per_region.round(2))
print()

# ---------------------------------------------------------------------------
# 4. Count of transactions per product per region
# ---------------------------------------------------------------------------
# Solution: groupby(['product', 'region']) then count rows (or use .size()).
count_per_product_region = df.groupby(["product", "region"]).size()
print("Transaction count per product per region:")
print(count_per_product_region)
print()

# Bonus: Multiple aggregations at once
print("Multiple aggregations per product:")
agg_result = df.groupby("product").agg(
    total_revenue=("revenue", "sum"),
    avg_quantity=("quantity", "mean"),
    num_transactions=("revenue", "count"),
)
print(agg_result)
