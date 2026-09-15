"""
Fill Missing Values: Numeric -> Median, Categorical -> Mode
============================================================
Handle missing data in a mixed-type DataFrame by filling numeric columns
with their median and categorical columns with their mode.
"""

import numpy as np
import pandas as pd


if __name__ == "__main__":
    # Dataset with missing values in both numeric and categorical columns
    data = {
        "age": [25, np.nan, 30, 45, np.nan, 50, 35, 60],
        "income": [50000, 60000, np.nan, 80000, 45000, np.nan, 55000, 90000],
        "city": ["NYC", "LA", "NYC", np.nan, "LA", "Chicago", "NYC", np.nan],
        "gender": ["M", "F", np.nan, "M", "F", "F", "M", "F"],
    }
    df = pd.DataFrame(data)

    print("=== Before filling missing values ===")
    print(df)
    print(f"\nMissing counts:\n{df.isnull().sum()}\n")

    # Fill numeric columns with median (robust to outliers)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)
        print(f"Filled {col} with median: {median_val}")

    # Fill categorical columns with mode (most frequent value)
    categorical_cols = df.select_dtypes(include=["object"]).columns
    for col in categorical_cols:
        mode_val = df[col].mode()[0]  # mode() returns a Series; take first
        df[col] = df[col].fillna(mode_val)
        print(f"Filled {col} with mode: {mode_val}")

    print(f"\n=== After filling missing values ===")
    print(df)
    print(f"\nMissing counts after:\n{df.isnull().sum()}")
