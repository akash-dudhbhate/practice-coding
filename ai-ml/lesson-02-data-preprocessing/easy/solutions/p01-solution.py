"""
Lesson 02 - Easy P01
Fill missing values: impute numeric columns with the median and categorical
columns with the most frequent value, using pandas and sklearn SimpleImputer.

Solution:
  1. Create a sample DataFrame with missing values.
  2. Identify numeric vs categorical columns.
  3. Use SimpleImputer(strategy='median') for numeric.
  4. Use SimpleImputer(strategy='most_frequent') for categorical.
  5. Reconstruct the DataFrame and print before/after.
"""

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# ---------------------------------------------------------------------------
# 1. Create sample data with missing values
# ---------------------------------------------------------------------------
np.random.seed(42)
data = {
    "age": [25, 30, np.nan, 45, 35, np.nan, 50, 40],
    "salary": [50000, 60000, 55000, np.nan, 70000, 65000, np.nan, 80000],
    "department": ["Engineering", "Sales", "Sales", np.nan, "Engineering", "Marketing", "Engineering", np.nan],
}
df = pd.DataFrame(data)
print("Original DataFrame (with missing values):")
print(df)
print()

# ---------------------------------------------------------------------------
# 2. Separate numeric and categorical columns
# ---------------------------------------------------------------------------
numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
categorical_cols = df.select_dtypes(exclude=["number"]).columns.tolist()
print(f"Numeric columns:     {numeric_cols}")
print(f"Categorical columns: {categorical_cols}")
print()

# ---------------------------------------------------------------------------
# 3. Impute numeric columns with median
# ---------------------------------------------------------------------------
# Solution: median is robust to outliers compared to mean.
numeric_imputer = SimpleImputer(strategy="median")
df_numeric_imputed = pd.DataFrame(
    numeric_imputer.fit_transform(df[numeric_cols]),
    columns=numeric_cols,
    index=df.index,
)

# ---------------------------------------------------------------------------
# 4. Impute categorical columns with most frequent value
# ---------------------------------------------------------------------------
categorical_imputer = SimpleImputer(strategy="most_frequent")
df_categorical_imputed = pd.DataFrame(
    categorical_imputer.fit_transform(df[categorical_cols]),
    columns=categorical_cols,
    index=df.index,
)

# ---------------------------------------------------------------------------
# 5. Combine imputed columns back into one DataFrame
# ---------------------------------------------------------------------------
df_imputed = pd.concat([df_numeric_imputed, df_categorical_imputed], axis=1)
# Restore original column order
df_imputed = df_imputed[df.columns]

print("DataFrame after imputation:")
print(df_imputed)
print()

# Verify no missing values remain
print(f"Remaining missing values: {df_imputed.isnull().sum().sum()}")
