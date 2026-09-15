"""
Lesson 05 - Medium P02
Box plots by category using seaborn with 3+ categories. Save the figure.

Solution:
  1. Create a DataFrame with a numeric column and a categorical column (3+ categories).
  2. Use seaborn boxplot() to show the distribution per category.
  3. Add labels, title, and save.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------------------------
# 1. Create data with 3+ categories
# ---------------------------------------------------------------------------
np.random.seed(42)
n_per_group = 100

data = {
    "score": np.concatenate([
        np.random.normal(75, 10, n_per_group),   # Group A
        np.random.normal(65, 15, n_per_group),   # Group B
        np.random.normal(80, 8, n_per_group),    # Group C
        np.random.normal(70, 12, n_per_group),   # Group D
    ]),
    "group": np.repeat(["A", "B", "C", "D"], n_per_group),
}
df = pd.DataFrame(data)

print("DataFrame summary:")
print(df.groupby("group")["score"].describe().round(2))
print()

# ---------------------------------------------------------------------------
# 2. Create box plots by category
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))

# Solution: seaborn boxplot() shows the median, quartiles, whiskers, and
# outliers for each category, making it easy to compare distributions.
sns.boxplot(
    data=df,
    x="group",
    y="score",
    hue="group",
    palette="Set2",
    ax=ax,
)

# Overlay individual data points for more detail
sns.stripplot(
    data=df,
    x="group",
    y="score",
    color="black",
    alpha=0.3,
    size=3,
    ax=ax,
)

# ---------------------------------------------------------------------------
# 3. Add labels and title
# ---------------------------------------------------------------------------
ax.set_xlabel("Group")
ax.set_ylabel("Score")
ax.set_title("Box Plots of Scores by Group (4 Categories)")
ax.grid(True, alpha=0.3, axis="y")

# ---------------------------------------------------------------------------
# 4. Save and show
# ---------------------------------------------------------------------------
plt.tight_layout()
plt.savefig("lesson-05-data-visualization/medium/solutions/boxplot_by_category.png", dpi=150, bbox_inches="tight")
print("Figure saved to: lesson-05-data-visualization/medium/solutions/boxplot_by_category.png")
plt.show()
