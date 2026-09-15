"""
Lesson 04 - Hard P01
Customer analytics: compute per-customer features:
  - total_spent
  - num_transactions
  - avg_transaction
  - first_purchase_date
  - days_since_last_purchase

Solution:
  1. Create a transactions dataset with customer_id, date, and amount.
  2. Group by customer_id and compute aggregations.
  3. Compute days since last purchase relative to a reference date.
  4. Return a customer-level feature DataFrame.
"""

import pandas as pd

# ---------------------------------------------------------------------------
# 1. Create a transactions dataset
# ---------------------------------------------------------------------------
data = {
    "customer_id": [1, 2, 1, 3, 2, 1, 3, 2, 4, 1, 3, 4],
    "transaction_date": [
        "2023-01-15", "2023-02-01", "2023-03-10", "2023-01-20",
        "2023-04-05", "2023-06-15", "2023-05-22", "2023-07-30",
        "2023-03-01", "2023-09-10", "2023-08-15", "2023-10-01",
    ],
    "amount": [120, 85, 200, 50, 300, 175, 90, 60, 400, 250, 110, 350],
}
df = pd.DataFrame(data)
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

print("Transactions DataFrame:")
print(df)
print()

# ---------------------------------------------------------------------------
# 2. Compute per-customer aggregations
# ---------------------------------------------------------------------------
# Solution: Group by customer_id and compute multiple aggregations at once
# using .agg() with named columns.
customer_features = df.groupby("customer_id").agg(
    total_spent=("amount", "sum"),
    num_transactions=("amount", "count"),
    avg_transaction=("amount", "mean"),
    first_purchase_date=("transaction_date", "min"),
    last_purchase_date=("transaction_date", "max"),
).reset_index()

# ---------------------------------------------------------------------------
# 3. Compute days since last purchase
# ---------------------------------------------------------------------------
# Solution: Use a reference date (e.g., the latest date in the dataset or today)
# and subtract each customer's last purchase date.
reference_date = df["transaction_date"].max()
customer_features["days_since_last_purchase"] = (
    reference_date - customer_features["last_purchase_date"]
).dt.days

# Round average transaction
customer_features["avg_transaction"] = customer_features["avg_transaction"].round(2)

print("Customer-level features:")
print(customer_features)
print()

# ---------------------------------------------------------------------------
# 4. Summary insights
# ---------------------------------------------------------------------------
print("Summary insights:")
print(f"  Total customers:          {len(customer_features)}")
print(f"  Highest spender:          Customer {customer_features.loc[customer_features['total_spent'].idxmax(), 'customer_id']}")
print(f"  Most active customer:     Customer {customer_features.loc[customer_features['num_transactions'].idxmax(), 'customer_id']}")
print(f"  Avg spend per customer:   ${customer_features['total_spent'].mean():.2f}")
print(f"  Avg transactions/customer:{customer_features['num_transactions'].mean():.1f}")
print()

# Sort by total_spent descending
print("Customers ranked by total spent:")
print(customer_features.sort_values("total_spent", ascending=False))
