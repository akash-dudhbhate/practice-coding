"""
Lesson 04 - Easy P03
Handle missing values: fill numeric NaN with the median and categorical NaN
with "Unknown".

Solution:
  1. Create a DataFrame with missing values in both numeric and categorical columns.
  2. Fill numeric NaN with column median.
  3. Fill categorical NaN with "Unknown".
  4. Verify no missing values remain.
"""

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# 1. Create a DataFrame with missing values
# ---------------------------------------------------------------------------
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "age": [28, np.nan, 42, 31, np.nan, 38],
    "salary": [70000, 85000, np.nan, 62000, 58000, np.nan],
    "department": ["Engineering", np.nan, "Sales", "Marketing", "Sales", np.nan],
}
df = pd.DataFrame(data)
print("Original DataFrame (with missing values):")
print(df)
print(f"\nMissing values per column:\n{df.isnull().sum()}\n")

# ---------------------------------------------------------------------------
# 2. Fill numeric NaN with median
# ---------------------------------------------------------------------------
# Solution: Median is robust to outliers. We fill only numeric columns.
numeric_cols = df.select_dtypes(include=["number"]).columns
for col in numeric_cols:
    median_val = df[col].median()
    df[col] = df[col].fillna(median_val)
    print(f"  Filled '{col}' NaN with median: {median_val}")

# ---------------------------------------------------------------------------
# 3. Fill categorical NaN with "Unknown"
# ---------------------------------------------------------------------------
# Solution: For categorical/text columns, fill with a placeholder string.
categorical_cols = df.select_dtypes(exclude=["number"]).columns
for col in categorical_cols:
    df[col] = df[col].fillna("Unknown")
    print(f"  Filled '{col}' NaN with 'Unknown'")

print()

# ---------------------------------------------------------------------------
# 4. Verify no missing values remain
# ---------------------------------------------------------------------------
print("DataFrame after handling missing values:")
print(df)
print(f"\nRemaining missing values: {df.isnull().sum().sum()}")
