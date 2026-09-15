"""
Lesson 04 - Easy P01
Create a DataFrame from a dictionary with 5 rows (name, age, salary, department).
Print shape, dtypes, and describe().

Solution:
  1. Define a dict of column data.
  2. Create a DataFrame with pd.DataFrame().
  3. Print shape, dtypes, and summary statistics.
"""

import pandas as pd

# ---------------------------------------------------------------------------
# 1. Create the DataFrame from a dictionary
# ---------------------------------------------------------------------------
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age": [28, 35, 42, 31, 26],
    "salary": [70000, 85000, 95000, 62000, 58000],
    "department": ["Engineering", "Engineering", "Sales", "Marketing", "Sales"],
}
df = pd.DataFrame(data)

# ---------------------------------------------------------------------------
# 2. Print the DataFrame
# ---------------------------------------------------------------------------
print("DataFrame:")
print(df)
print()

# ---------------------------------------------------------------------------
# 3. Print shape, dtypes, and describe
# ---------------------------------------------------------------------------
print(f"Shape: {df.shape}  (rows, columns)")
print()

print("Column data types:")
print(df.dtypes)
print()

print("Summary statistics (describe):")
print(df.describe())
print()

print("Summary statistics (include all columns):")
print(df.describe(include="all"))
