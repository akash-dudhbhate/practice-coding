"""SOLUTION: Time-series with pivot_table (Hard)"""
import pandas as pd
import numpy as np
import random

def main():
    random.seed(42)
    dates = pd.date_range("2024-01-01", periods=12, freq="ME")
    products = ["A", "B", "C"]
    rows = []
    for d in dates:
        for p in products:
            rows.append({"date": d, "product": p, "sales": random.randint(100, 500)})
    df = pd.DataFrame(rows)

    df["month"] = df["date"].dt.month_name()
    pivot = df.pivot_table(index="product", columns="month", values="sales", aggfunc="sum")
    print("Pivot table:\n", pivot)

    growth = pivot.pct_change(axis=1)
    print("\nMonth-over-month growth:\n", growth)

    # Trending products: positive growth for 3+ consecutive months
    trending = []
    for product in pivot.index:
        product_growth = growth.loc[product].dropna()
        consecutive = 0
        max_consecutive = 0
        for g in product_growth:
            if g > 0:
                consecutive += 1
                max_consecutive = max(max_consecutive, consecutive)
            else:
                consecutive = 0
        if max_consecutive >= 3:
            trending.append(product)

    print(f"\nTrending products (3+ consecutive positive growth): {trending}")

if __name__ == "__main__":
    main()
