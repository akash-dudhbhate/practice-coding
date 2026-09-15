"""
Lesson 02 - Medium P02
Detect and handle outliers using the IQR method and winsorization.

Solution:
  1. Create a dataset with injected outliers.
  2. Detect outliers using the IQR method (values outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR]).
  3. Handle outliers via winsorization (clip to the IQR fences).
  4. Compare before and after.
"""

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# 1. Create sample data with injected outliers
# ---------------------------------------------------------------------------
np.random.seed(42)
data = np.random.normal(loc=100, scale=15, size=200)
# Inject extreme outliers
data[0] = 300
data[1] = -50
data[2] = 250
df = pd.DataFrame({"value": data})

print("Original data summary:")
print(df.describe())
print()

# ---------------------------------------------------------------------------
# 2. Detect outliers using the IQR method
# ---------------------------------------------------------------------------
# Solution: IQR = Q3 - Q1. Any value below Q1 - 1.5*IQR or above Q3 + 1.5*IQR
# is considered an outlier.
Q1 = df["value"].quantile(0.25)
Q3 = df["value"].quantile(0.75)
IQR = Q3 - Q1
lower_fence = Q1 - 1.5 * IQR
upper_fence = Q3 + 1.5 * IQR

print(f"Q1 = {Q1:.2f}, Q3 = {Q3:.2f}, IQR = {IQR:.2f}")
print(f"Lower fence = {lower_fence:.2f}, Upper fence = {upper_fence:.2f}")

outlier_mask = (df["value"] < lower_fence) | (df["value"] > upper_fence)
num_outliers = outlier_mask.sum()
print(f"Number of outliers detected: {num_outliers}")
print(f"Outlier values: {df.loc[outlier_mask, 'value'].tolist()}")
print()

# ---------------------------------------------------------------------------
# 3. Handle outliers via winsorization (clip to fences)
# ---------------------------------------------------------------------------
# Solution: Winsorization replaces extreme values with the fence values instead
# of deleting them. This preserves the row count and reduces the influence of
# outliers without losing data.
df_winsorized = df.copy()
df_winsorized["value"] = df_winsorized["value"].clip(lower=lower_fence, upper=upper_fence)

print("Data after winsorization:")
print(df_winsorized.describe())
print()

# ---------------------------------------------------------------------------
# 4. Compare distributions before and after
# ---------------------------------------------------------------------------
print("Comparison:")
print(f"  Original  -> min: {df['value'].min():.2f}, max: {df['value'].max():.2f}, mean: {df['value'].mean():.2f}, std: {df['value'].std():.2f}")
print(f"  Winsorized-> min: {df_winsorized['value'].min():.2f}, max: {df_winsorized['value'].max():.2f}, mean: {df_winsorized['value'].mean():.2f}, std: {df_winsorized['value'].std():.2f}")
print()

# Verify no outliers remain after winsorization
new_outliers = ((df_winsorized["value"] < lower_fence) | (df_winsorized["value"] > upper_fence)).sum()
print(f"Outliers remaining after winsorization: {new_outliers}")
