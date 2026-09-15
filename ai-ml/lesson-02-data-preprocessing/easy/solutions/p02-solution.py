"""
Lesson 02 - Easy P02
One-hot encode a categorical column using pd.get_dummies().

Solution:
  1. Create a DataFrame with a categorical column.
  2. Use pd.get_dummies() to convert it into binary indicator columns.
  3. Show the result with drop_first=False and drop_first=True.
"""

import pandas as pd

# ---------------------------------------------------------------------------
# 1. Create sample data
# ---------------------------------------------------------------------------
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "department": ["Engineering", "Sales", "Engineering", "Marketing", "Sales"],
    "salary": [70000, 55000, 72000, 60000, 58000],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print()

# ---------------------------------------------------------------------------
# 2. One-hot encode the 'department' column
# ---------------------------------------------------------------------------
# Solution: pd.get_dummies() creates a new binary column for each category.
df_encoded = pd.get_dummies(df, columns=["department"], prefix="dept")
print("After one-hot encoding (drop_first=False):")
print(df_encoded)
print()

# ---------------------------------------------------------------------------
# 3. One-hot encode with drop_first=True (avoid multicollinearity)
# ---------------------------------------------------------------------------
# Solution: drop_first=True drops the first category column. This is useful
# for linear models to avoid the dummy-variable trap (perfect multicollinearity).
df_encoded_drop = pd.get_dummies(df, columns=["department"], prefix="dept", drop_first=True)
print("After one-hot encoding (drop_first=True):")
print(df_encoded_drop)
print()

# ---------------------------------------------------------------------------
# 4. Convert boolean columns to integers (0/1) for ML compatibility
# ---------------------------------------------------------------------------
df_encoded_int = df_encoded.copy()
bool_cols = df_encoded_int.select_dtypes(include=["bool"]).columns
df_encoded_int[bool_cols] = df_encoded_int[bool_cols].astype(int)
print("Encoded with integer 0/1 values:")
print(df_encoded_int)
