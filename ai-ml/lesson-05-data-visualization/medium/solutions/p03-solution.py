# Lesson 05 — Medium P03: Subplots (2x2 grid)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset using the modern numpy.random.Generator API
rng = np.random.default_rng(42)
n = 200
data = pd.DataFrame({
    "x": rng.standard_normal(n),
    "y": rng.standard_normal(n) * 2 + 1,
    "category": rng.choice(["A", "B", "C"], n),
})

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# (1) Histogram
axes[0, 0].hist(data["x"], bins=30, color="steelblue", edgecolor="white")
axes[0, 0].set_title("Histogram of x")
axes[0, 0].set_xlabel("x")
axes[0, 0].set_ylabel("Frequency")

# (2) Scatter plot
axes[0, 1].scatter(data["x"], data["y"], alpha=0.5, color="coral")
axes[0, 1].set_title("Scatter: x vs y")
axes[0, 1].set_xlabel("x")
axes[0, 1].set_ylabel("y")

# (3) Box plot by category
categories = data["category"].unique()
box_data = [data[data["category"] == c]["y"].values for c in categories]
axes[1, 0].boxplot(box_data, labels=categories)
axes[1, 0].set_title("Box Plot of y by Category")
axes[1, 0].set_xlabel("Category")
axes[1, 0].set_ylabel("y")

# (4) Line plot (cumulative sum for visual interest)
axes[1, 1].plot(data["x"].cumsum(), color="green")
axes[1, 1].set_title("Cumulative Sum of x")
axes[1, 1].set_xlabel("Index")
axes[1, 1].set_ylabel("Cumulative x")

plt.tight_layout()
plt.savefig("subplots.png", dpi=150)
print("Figure saved to subplots.png")
