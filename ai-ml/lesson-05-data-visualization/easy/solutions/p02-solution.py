"""
Lesson 05 - Easy P02
Histogram: 1000 normal random numbers (mean=50, std=15), 30 bins, with a
vertical line at the mean. Save the figure.

Solution:
  1. Generate 1000 samples from N(50, 15).
  2. Plot a histogram with 30 bins.
  3. Add a vertical line at the mean.
  4. Add labels, title, and save.
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 1. Generate data
# ---------------------------------------------------------------------------
np.random.seed(42)
data = np.random.normal(loc=50, scale=15, size=1000)

# ---------------------------------------------------------------------------
# 2. Create the histogram
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))

ax.hist(data, bins=30, color="steelblue", edgecolor="white", alpha=0.8)

# ---------------------------------------------------------------------------
# 3. Add vertical line at the mean
# ---------------------------------------------------------------------------
mean_val = np.mean(data)
ax.axvline(mean_val, color="red", linestyle="--", linewidth=2, label=f"Mean = {mean_val:.2f}")

# ---------------------------------------------------------------------------
# 4. Add labels, title, legend
# ---------------------------------------------------------------------------
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
ax.set_title("Histogram of Normal Distribution (mean=50, std=15, n=1000)")
ax.legend()
ax.grid(True, alpha=0.3, axis="y")

# ---------------------------------------------------------------------------
# 5. Save and show
# ---------------------------------------------------------------------------
plt.tight_layout()
plt.savefig("lesson-05-data-visualization/easy/solutions/histogram_normal.png", dpi=150, bbox_inches="tight")
print(f"Mean: {mean_val:.2f}, Std: {np.std(data):.2f}")
print("Figure saved to: lesson-05-data-visualization/easy/solutions/histogram_normal.png")
plt.show()
