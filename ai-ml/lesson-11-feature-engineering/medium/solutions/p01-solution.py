"""
Date Feature Engineering
========================
Extract useful features from datetime columns: year, month, day of week,
is_weekend, and quarter using pandas datetime methods.
"""

import numpy as np
import pandas as pd


if __name__ == "__main__":
    # Sample date range spanning different months and days of week
    dates = pd.date_range(start="2024-01-01", periods=15, freq="3D")
    df = pd.DataFrame({"date": dates, "sales": np.random.randint(100, 500, size=15)})

    print("=== Original DataFrame ===")
    print(df.head(10))
    print()

    # Ensure the column is datetime type
    df["date"] = pd.to_datetime(df["date"])

    # Extract calendar features
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["day_of_week"] = df["date"].dt.dayofweek       # Monday=0, Sunday=6
    df["day_name"] = df["date"].dt.day_name()          # human-readable
    df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)  # Sat/Sun = 1
    df["quarter"] = df["date"].dt.quarter

    print("=== After date feature engineering ===")
    print(df.head(10))
    print()

    # Show weekend vs weekday sales summary
    print("=== Weekend vs Weekday sales ===")
    print(df.groupby("is_weekend")["sales"].agg(["mean", "count"]))
