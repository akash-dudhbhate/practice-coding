"""
Lesson 02 - Easy P03
Standardize features with StandardScaler and verify mean ~ 0 and std ~ 1.

Solution:
  1. Create a sample feature matrix with different scales.
  2. Fit StandardScaler (z = (x - mean) / std).
  3. Verify each column has mean ~ 0 and std ~ 1.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# ---------------------------------------------------------------------------
# 1. Create sample data with very different scales
# ---------------------------------------------------------------------------
np.random.seed(42)
data = {
    "age": np.random.randint(20, 70, size=100),          # range ~20-70
    "income": np.random.randint(30000, 120000, size=100),  # range ~30k-120k
    "credit_score": np.random.randint(300, 850, size=100),  # range ~300-850
}
df = pd.DataFrame(data)
print("Original data (first 5 rows):")
print(df.head())
print(f"\nOriginal means:\n{df.mean()}")
print(f"\nOriginal stds:\n{df.std()}")
print()

# ---------------------------------------------------------------------------
# 2. Standardize with StandardScaler
# ---------------------------------------------------------------------------
# Solution: StandardScaler transforms each feature to have mean=0 and std=1
# using z = (x - mean) / std. This puts all features on the same scale,
# which is important for distance-based and gradient-based algorithms.
scaler = StandardScaler()
scaled_array = scaler.fit_transform(df)
df_scaled = pd.DataFrame(scaled_array, columns=df.columns)

print("Scaled data (first 5 rows):")
print(df_scaled.head())
print()

# ---------------------------------------------------------------------------
# 3. Verify mean ~ 0 and std ~ 1
# ---------------------------------------------------------------------------
print("Verification after scaling:")
print(f"  Means: {df_scaled.mean().values}")
print(f"  Stds:  {df_scaled.std().values}")
print()

# Check that means are close to 0 and stds close to 1
means_close_to_zero = np.allclose(df_scaled.mean(), 0.0, atol=1e-10)
stds_close_to_one = np.allclose(df_scaled.std(), 1.0, atol=1e-10)
print(f"All means ~ 0: {means_close_to_zero}")
print(f"All stds  ~ 1: {stds_close_to_one}")
