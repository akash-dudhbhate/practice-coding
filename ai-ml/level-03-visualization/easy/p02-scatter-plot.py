"""
LEVEL 03 — Data Visualization
EASY P02 — Scatter Plot with Categories
========================================

CONCEPT:
  plt.scatter(x, y, c=colors, label=...) — points, not lines.
  Color by category = plot each group separately with a label.
  np.random.normal(mean, std, n) — realistic data.
  np.random.choice([...], n) — random categories.

PROBLEM:
  Write `plot_scatter()` that:
    1. np.random.seed(42)
    2. height = normal(170, 10, 100); weight = height*0.6 + normal(0,5,100)
    3. gender = choice(['M','F'], 100)
    4. Scatter M in blue, F in red, with labels + legend + title
    5. Save to 'scatter_plot.png', show, return (height, weight, gender)

TRY THIS INPUT:
  ```python
  h, w, g = plot_scatter()
  print(len(h), len(w), len(g))   # 100 100 100
  print(f"{h.mean():.1f}")         # ~170.0
  ```

EXPECTED OUTPUT:
  ```
  100 100 100
  170.3
  ```

HINT:
  mask = gender == 'M'; plt.scatter(height[mask], weight[mask], c='blue', label='M')

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# h, w, g = plot_scatter()
# print(h.mean())
