"""
Lesson 04 - Easy P02
Filter rows from a DataFrame:
  - salary > 60000
  - department == 'Engineering'
  - both conditions combined

Solution:
  Use boolean indexing: df[condition].
  Combine conditions with & (and) and | (or), using parentheses.
"""

import pandas as pd

# ---------------------------------------------------------------------------
# 1. Create the DataFrame
# ---------------------------------------------------------------------------
data = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "age": [28, 35, 42, 31, 26, 38],
    "salary": [70000, 85000, 95000, 62000, 58000, 90000],
    "department": ["Engineering", "Engineering", "Sales", "Marketing", "Sales", "Engineering"],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print()

# ---------------------------------------------------------------------------
# 2. Filter: salary > 60000
# ---------------------------------------------------------------------------
# Solution: Boolean indexing returns rows where the condition is True.
high_salary = df[df["salary"] > 60000]
print("Rows where salary > 60000:")
print(high_salary)
print()

# ---------------------------------------------------------------------------
# 3. Filter: department == 'Engineering'
# ---------------------------------------------------------------------------
engineering = df[df["department"] == "Engineering"]
print("Rows where department == 'Engineering':")
print(engineering)
print()

# ---------------------------------------------------------------------------
# 4. Filter: both conditions (salary > 60000 AND department == 'Engineering')
# ---------------------------------------------------------------------------
# Solution: Combine conditions with & and wrap each in parentheses.
both = df[(df["salary"] > 60000) & (df["department"] == "Engineering")]
print("Rows where salary > 60000 AND department == 'Engineering':")
print(both)
print()

# Bonus: OR condition
or_condition = df[(df["salary"] > 80000) | (df["department"] == "Marketing")]
print("Rows where salary > 80000 OR department == 'Marketing':")
print(or_condition)
