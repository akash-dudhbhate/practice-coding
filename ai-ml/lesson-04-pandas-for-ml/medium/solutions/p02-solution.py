"""
Lesson 04 - Medium P02
Merge employees and departments tables using a left join.
Handle unmatched employees by filling with "Unassigned".

Solution:
  1. Create employees and departments DataFrames.
  2. Merge with how='left' to keep all employees.
  3. Fill unmatched department names with "Unassigned".
"""

import pandas as pd

# ---------------------------------------------------------------------------
# 1. Create employees and departments DataFrames
# ---------------------------------------------------------------------------
employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "dept_id": [10, 20, 10, 30, 40],  # dept_id 40 does not exist in departments
})
departments = pd.DataFrame({
    "dept_id": [10, 20, 30],
    "dept_name": ["Engineering", "Sales", "Marketing"],
})

print("Employees:")
print(employees)
print("\nDepartments:")
print(departments)
print()

# ---------------------------------------------------------------------------
# 2. Merge with a left join
# ---------------------------------------------------------------------------
# Solution: how='left' keeps all rows from the left (employees) table.
# Unmatched dept_id values will have NaN in the dept_name column.
merged = pd.merge(employees, departments, on="dept_id", how="left")
print("Merged (left join, before filling NaN):")
print(merged)
print()

# ---------------------------------------------------------------------------
# 3. Handle unmatched departments -> "Unassigned"
# ---------------------------------------------------------------------------
# Solution: Fill NaN in dept_name with "Unassigned" for employees whose
# department does not exist in the departments table.
merged["dept_name"] = merged["dept_name"].fillna("Unassigned")
print("Merged (left join, after filling NaN with 'Unassigned'):")
print(merged)
print()

# ---------------------------------------------------------------------------
# 4. Show which employees were unmatched
# ---------------------------------------------------------------------------
unmatched = merged[merged["dept_name"] == "Unassigned"]
print(f"Unmatched employees ({len(unmatched)}):")
print(unmatched[["emp_id", "name", "dept_id"]])
