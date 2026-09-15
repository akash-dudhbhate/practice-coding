"""
Lesson 04 - Medium P03
Feature extraction from dates: year, month, day_of_week, is_weekend, quarter.

Solution:
  1. Create a DataFrame with a date column.
  2. Convert to datetime with pd.to_datetime().
  3. Extract year, month, day_of_week, is_weekend, and quarter.
  4. Print the enriched DataFrame.
"""

import pandas as pd

# ---------------------------------------------------------------------------
# 1. Create a DataFrame with date strings
# ---------------------------------------------------------------------------
data = {
    "order_id": [101, 102, 103, 104, 105, 106, 107],
    "order_date": [
        "2023-01-15",   # Sunday
        "2023-03-22",   # Wednesday
        "2023-06-10",   # Saturday
        "2023-09-05",   # Tuesday
        "2023-12-01",   # Friday
        "2024-02-28",   # Wednesday
        "2024-07-20",   # Saturday
    ],
    "amount": [250, 45, 120, 899, 300, 75, 500],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print()

# ---------------------------------------------------------------------------
# 2. Convert to datetime
# ---------------------------------------------------------------------------
df["order_date"] = pd.to_datetime(df["order_date"])

# ---------------------------------------------------------------------------
# 3. Extract date-based features
# ---------------------------------------------------------------------------
# Solution: Use the .dt accessor to extract components from datetime columns.
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["day"] = df["order_date"].dt.day
df["day_of_week"] = df["order_date"].dt.dayofweek    # 0=Monday, 6=Sunday
df["day_name"] = df["order_date"].dt.day_name()       # readable day name
df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)  # 1 if Sat/Sun
df["quarter"] = df["order_date"].dt.quarter           # 1-4

print("DataFrame with extracted date features:")
print(df)
print()

# ---------------------------------------------------------------------------
# 4. Show feature summary
# ---------------------------------------------------------------------------
print("Feature summary:")
print(f"  Years present:      {sorted(df['year'].unique())}")
print(f"  Quarters present:   {sorted(df['quarter'].unique())}")
print(f"  Weekend orders:     {df['is_weekend'].sum()}")
print(f"  Weekday orders:     {(df['is_weekend'] == 0).sum()}")
print()

# Bonus: average amount by weekend vs weekday
print("Average amount: weekend vs weekday:")
print(df.groupby("is_weekend")["amount"].mean().rename({0: "Weekday", 1: "Weekend"}))
