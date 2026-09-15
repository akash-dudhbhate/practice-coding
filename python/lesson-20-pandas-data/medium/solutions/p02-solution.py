"""SOLUTION: Merge DataFrames and find top users (Medium)"""
import pandas as pd

def main():
    users = pd.DataFrame({
        "id": [1, 2, 3, 4],
        "name": ["Alice", "Bob", "Charlie", "Diana"],
        "city": ["Mumbai", "Delhi", "Pune", "Bangalore"]
    })
    orders = pd.DataFrame({
        "id": [101, 102, 103, 104, 105],
        "user_id": [1, 2, 1, 3, 2],
        "amount": [500, 300, 700, 200, 600],
        "date": pd.date_range("2024-01-01", periods=5)
    })
    merged = users.merge(orders, left_on="id", right_on="user_id")
    total_by_user = merged.groupby("name")["amount"].sum().sort_values(ascending=False)
    print("Merged:\n", merged[["name", "amount"]])
    print("\nTop 3 users by total amount:\n", total_by_user.head(3))

if __name__ == "__main__":
    main()
