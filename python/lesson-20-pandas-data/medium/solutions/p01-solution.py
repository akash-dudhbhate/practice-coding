"""SOLUTION: GroupBy sales analysis (Medium)"""
import pandas as pd

def main():
    df = pd.DataFrame({
        "product": ["A", "B", "A", "C", "B", "A", "C", "B"],
        "region": ["North", "South", "North", "East", "South", "East", "North", "East"],
        "sales": [100, 200, 150, 300, 250, 120, 180, 220],
        "date": pd.date_range("2024-01-01", periods=8)
    })
    total_by_region = df.groupby("region")["sales"].sum()
    avg_by_product = df.groupby("product")["sales"].mean()
    print("Total sales by region:\n", total_by_region)
    print("\nAverage sales by product:\n", avg_by_product)

if __name__ == "__main__":
    main()
