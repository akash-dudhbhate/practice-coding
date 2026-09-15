"""
Lesson 05 - Easy P03
Scatter plot: two correlated arrays with alpha=0.5 and the correlation
coefficient displayed on the plot. Save the figure.

Solution:
  1. Generate two correlated arrays.
  2. Plot a scatter plot with alpha=0.5.
  3. Compute and display the Pearson correlation coefficient.
  4. Add labels, title, and save.
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 1. Generate correlated data
# ---------------------------------------------------------------------------
np.random.seed(42)
n = 200
x = np.random.randn(n) * 10 + 50  # e.g., study hours
# y is correlated with x plus some noise
noise = np.random.randn(n) * 5
y = 2.5 * x + 10 + noise  # e.g., exam scores

# ---------------------------------------------------------------------------
# 2. Compute correlation coefficient
# ---------------------------------------------------------------------------
correlation = np.corrcoef(x, y)[0, 1]

# ---------------------------------------------------------------------------
# 3. Create the scatter plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(x, y, alpha=0.5, color="steelblue", edgecolors="navy", linewidth=0.5)

# ---------------------------------------------------------------------------
# 4. Add correlation coefficient text on the plot
# ---------------------------------------------------------------------------
ax.text(
    0.05, 0.95, f"Pearson r = {correlation:.4f}",
    transform=ax.transAxes, fontsize=12, verticalalignment="top",
    bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5),
)

# ---------------------------------------------------------------------------
# 5. Add labels, title, and save
# ---------------------------------------------------------------------------
ax.set_xlabel("X (e.g., Study Hours)")
ax.set_ylabel("Y (e.g., Exam Score)")
ax.set_title("Scatter Plot of Correlated Variables")
ax.grid(True, alpha=0.3)

# Add a trend line for visualization
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
x_line = np.linspace(x.min(), x.max(), 100)
ax.plot(x_line, p(x_line), color="red", linestyle="--", linewidth=1.5, label="Trend line")
ax.legend()

plt.tight_layout()
plt.savefig("lesson-05-data-visualization/easy/solutions/scatter_correlated.png", dpi=150, bbox_inches="tight")
print(f"Pearson correlation coefficient: {correlation:.4f}")
print("Figure saved to: lesson-05-data-visualization/easy/solutions/scatter_correlated.png")
plt.show()
