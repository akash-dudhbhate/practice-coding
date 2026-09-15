"""
Lesson 05 - Easy P01
Line plot: plot sin(x) and cos(x) on the same figure with legend, labels,
title, and grid. Save the figure.

Solution:
  1. Generate x values and compute sin(x) and cos(x).
  2. Plot both curves on the same axes.
  3. Add legend, axis labels, title, and grid.
  4. Save the figure to a PNG file.
"""

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 1. Generate data
# ---------------------------------------------------------------------------
x = np.linspace(-np.pi, np.pi, 200)
y_sin = np.sin(x)
y_cos = np.cos(x)

# ---------------------------------------------------------------------------
# 2. Create the plot
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(x, y_sin, label="sin(x)", color="blue", linewidth=2)
ax.plot(x, y_cos, label="cos(x)", color="red", linewidth=2, linestyle="--")

# ---------------------------------------------------------------------------
# 3. Add labels, title, legend, and grid
# ---------------------------------------------------------------------------
ax.set_xlabel("x (radians)")
ax.set_ylabel("y")
ax.set_title("Sine and Cosine Functions")
ax.legend(loc="upper right")
ax.grid(True, alpha=0.3)
ax.axhline(y=0, color="black", linewidth=0.5)  # x-axis line

# ---------------------------------------------------------------------------
# 4. Save and show
# ---------------------------------------------------------------------------
plt.tight_layout()
plt.savefig("lesson-05-data-visualization/easy/solutions/sin_cos_plot.png", dpi=150, bbox_inches="tight")
print("Figure saved to: lesson-05-data-visualization/easy/solutions/sin_cos_plot.png")
plt.show()
