"""
Lesson 05 - Medium P01
Correlation heatmap with seaborn using 5 numeric columns and the "coolwarm"
colormap. Save the figure.

Solution:
  1. Create a DataFrame with 5 numeric columns.
  2. Compute the correlation matrix.
  3. Plot a heatmap with seaborn using annot=True and cmap="coolwarm".
  4. Save the figure.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------------------------
# 1. Create a DataFrame with 5 numeric columns
# ---------------------------------------------------------------------------
np.random.seed(42)
n = 200
data = {
    "height_cm": np.random.normal(170, 10, n),
    "weight_kg": np.random.normal(70, 12, n),
    "age_years": np.random.randint(18, 65, n),
    "bmi": np.random.normal(24, 4, n),
    "resting_hr": np.random.normal(70, 10, n),
}
# Introduce some correlations
data["weight_kg"] = data["height_cm"] * 0.4 + data["weight_kg"] * 0.6
data["bmi"] = data["weight_kg"] / (data["height_cm"] / 100) ** 2

df = pd.DataFrame(data)
print("DataFrame (first 5 rows):")
print(df.head())
print()

# ---------------------------------------------------------------------------
# 2. Compute the correlation matrix
# ---------------------------------------------------------------------------
corr_matrix = df.corr()
print("Correlation matrix:")
print(corr_matrix.round(3))
print()

# ---------------------------------------------------------------------------
# 3. Plot the heatmap
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))

# Solution: seaborn heatmap with annot=True shows correlation values in each
# cell. cmap="coolwarm" makes positive correlations red and negative blue.
# center=0 ensures the colormap is centered at zero.
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    vmin=-1,
    vmax=1,
    square=True,
    linewidths=0.5,
    ax=ax,
)

ax.set_title("Correlation Heatmap of 5 Numeric Features")

# ---------------------------------------------------------------------------
# 4. Save and show
# ---------------------------------------------------------------------------
plt.tight_layout()
plt.savefig("lesson-05-data-visualization/medium/solutions/correlation_heatmap.png", dpi=150, bbox_inches="tight")
print("Figure saved to: lesson-05-data-visualization/medium/solutions/correlation_heatmap.png")
plt.show()
