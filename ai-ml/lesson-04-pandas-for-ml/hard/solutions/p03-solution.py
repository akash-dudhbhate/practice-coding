"""
Lesson 04 - Hard P03
Pivot tables and crosstabs:
  - Sales by month x product (pivot table)
  - Product x region average sales (pivot table)
  - Best-selling product per region

Solution:
  1. Create a sales dataset with dates, products, regions, and amounts.
  2. Use pd.pivot_table() to create month x product and product x region tables.
  3. Use pd.crosstab() for a count-based cross-tabulation.
  4. Find the best-selling product per region.
"""

import pandas as pd

# ---------------------------------------------------------------------------
# 1. Create a sales dataset
# ---------------------------------------------------------------------------
data = {
    "date": pd.to_datetime([
        "2023-01-15", "2023-01-20", "2023-02-10", "2023-02-15",
        "2023-01-25", "2023-03-05", "2023-03-10", "2023-02-28",
        "2023-03-20", "2023-01-30", "2023-03-25", "2023-02-05",
        "2023-03-15", "2023-01-10", "2023-02-20",
    ]),
    "product": ["A", "B", "A", "C", "B", "A", "C", "B",
                "A", "C", "B", "A", "C", "B", "C"],
    "region": ["North", "South", "North", "East", "South", "West", "East",
               "West", "North", "South", "East", "West", "North", "South", "East"],
    "amount": [100, 200, 150, 300, 250, 180, 350, 220,
               130, 280, 190, 170, 310, 210, 290],
}
df = pd.DataFrame(data)
df["month"] = df["date"].dt.month_name()

print("Sales DataFrame:")
print(df)
print()

# ---------------------------------------------------------------------------
# 2. Pivot table: total sales by month x product
# ---------------------------------------------------------------------------
# Solution: pd.pivot_table() reshapes data with rows=month, columns=product,
# values=amount, aggregated by sum.
pivot_month_product = pd.pivot_table(
    df, values="amount", index="month", columns="product", aggfunc="sum",
    fill_value=0,
)
print("Total sales by month x product:")
print(pivot_month_product)
print()

# ---------------------------------------------------------------------------
# 3. Pivot table: average sales by product x region
# ---------------------------------------------------------------------------
# Solution: rows=product, columns=region, values=amount, aggregated by mean.
pivot_product_region = pd.pivot_table(
    df, values="amount", index="product", columns="region", aggfunc="mean",
    fill_value=0,
).round(2)
print("Average sales by product x region:")
print(pivot_product_region)
print()

# ---------------------------------------------------------------------------
# 4. Crosstab: transaction count by product x region
# ---------------------------------------------------------------------------
# Solution: pd.crosstab() counts occurrences (frequency table).
crosstab_count = pd.crosstab(df["product"], df["region"])
print("Transaction count by product x region (crosstab):")
print(crosstab_count)
print()

# ---------------------------------------------------------------------------
# 5. Best-selling product per region (by total sales)
# ---------------------------------------------------------------------------
# Solution: Group by region and product, sum amounts, then find the product
# with the max total in each region.
region_product_sales = df.groupby(["region", "product"])["amount"].sum().reset_index()
best_selling = region_product_sales.loc[
    region_product_sales.groupby("region")["amount"].idxmax()
].reset_index(drop=True)
best_selling = best_selling.rename(columns={"amount": "total_sales"})

print("Best-selling product per region (by total sales):")
print(best_selling)
print()

# Alternative using pivot table + idxmax
pivot_region_product = pd.pivot_table(
    df, values="amount", index="region", columns="product", aggfunc="sum", fill_value=0
)
best_per_region = pivot_region_product.idxmax(axis=1)
print("Best product per region (via pivot idxmax):")
for region, product in best_per_region.items():
    sales = pivot_region_product.loc[region, product]
    print(f"  {region}: {product} (${sales})")
