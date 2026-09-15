"""
Lesson 04 - Hard P02
Merge users and purchases tables, then compute per-user features:
  - total_spent
  - num_purchases
  - avg_purchase
  - favorite_category (most frequent)
  - purchase_date_range (days between first and last purchase)

Solution:
  1. Create users and purchases DataFrames.
  2. Left join users with purchases on user_id.
  3. Handle users with no purchases.
  4. Group by user and compute features.
"""

import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# 1. Create users and purchases DataFrames
# ---------------------------------------------------------------------------
users = pd.DataFrame({
    "user_id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "signup_date": pd.to_datetime(["2023-01-01", "2023-02-01", "2023-01-15", "2023-03-01", "2023-02-15"]),
})

purchases = pd.DataFrame({
    "user_id": [1, 1, 2, 1, 3, 2, 3, 3, 4, 1, 2, 3],
    "purchase_date": pd.to_datetime([
        "2023-01-10", "2023-02-15", "2023-03-01", "2023-04-20",
        "2023-02-10", "2023-05-15", "2023-03-22", "2023-06-01",
        "2023-04-05", "2023-07-10", "2023-08-20", "2023-09-15",
    ]),
    "amount": [100, 250, 80, 150, 300, 120, 90, 200, 500, 175, 60, 110],
    "category": ["Electronics", "Books", "Food", "Electronics", "Books",
                 "Food", "Electronics", "Books", "Electronics", "Food", "Books", "Food"],
})

print("Users:")
print(users)
print(f"\nPurchases:")
print(purchases)
print()

# ---------------------------------------------------------------------------
# 2. Left join users with purchases
# ---------------------------------------------------------------------------
# Solution: how='left' keeps all users, even those with no purchases (user 5).
merged = pd.merge(users, purchases, on="user_id", how="left")
print("Merged (left join):")
print(merged)
print()

# ---------------------------------------------------------------------------
# 3. Compute per-user features
# ---------------------------------------------------------------------------
# Solution: Group the merged data by user and compute aggregations.
# For users with no purchases, fill with sensible defaults.

# Numeric aggregations
user_features = merged.groupby(["user_id", "name"]).agg(
    total_spent=("amount", "sum"),
    num_purchases=("amount", "count"),
    avg_purchase=("amount", "mean"),
    first_purchase=("purchase_date", "min"),
    last_purchase=("purchase_date", "max"),
).reset_index()

# Favorite category: most frequent category per user
# Solution: groupby user_id + category, count, then pick the max per user.
cat_counts = merged.groupby(["user_id", "category"]).size().reset_index(name="count")
favorite = cat_counts.sort_values("count", ascending=False).drop_duplicates("user_id")
favorite = favorite[["user_id", "category"]].rename(columns={"category": "favorite_category"})

user_features = pd.merge(user_features, favorite, on="user_id", how="left")

# Purchase date range (days between first and last purchase)
user_features["purchase_date_range"] = (
    user_features["last_purchase"] - user_features["first_purchase"]
).dt.days

# Handle users with no purchases (NaN values)
user_features["total_spent"] = user_features["total_spent"].fillna(0)
user_features["num_purchases"] = user_features["num_purchases"].fillna(0).astype(int)
user_features["avg_purchase"] = user_features["avg_purchase"].fillna(0).round(2)
user_features["favorite_category"] = user_features["favorite_category"].fillna("None")
user_features["purchase_date_range"] = user_features["purchase_date_range"].fillna(0).astype(int)

print("Per-user features:")
print(user_features)
print()

# ---------------------------------------------------------------------------
# 4. Insights
# ---------------------------------------------------------------------------
print("Insights:")
print(f"  Users with purchases:    {(user_features['num_purchases'] > 0).sum()}")
print(f"  Users without purchases: {(user_features['num_purchases'] == 0).sum()}")
print(f"  Highest spender:         {user_features.loc[user_features['total_spent'].idxmax(), 'name']}")
print(f"  Most frequent buyer:     {user_features.loc[user_features['num_purchases'].idxmax(), 'name']}")
