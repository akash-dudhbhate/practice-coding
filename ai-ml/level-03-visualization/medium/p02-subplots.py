"""
LEVEL 03 — Data Visualization
MEDIUM P02 — 2×2 Subplot Dashboard
========================================

CONCEPT:
  fig, axes = plt.subplots(2, 2, figsize=(12, 10))
  axes[0,0] is top-left, axes[1,1] is bottom-right.
  Each axes works like plt: axes[0,0].plot(...), .hist(...), .bar(...)

PROBLEM:
  Write `plot_dashboard()` that builds a 2×2 grid:
    [0,0] line plot: sin(x) over 0-10
    [0,1] scatter: 50 random points
    [1,0] histogram: 200 random normals
    [1,1] bar chart: categories A-D, values [23,45,56,78]
  np.random.seed(42) first. Save 'dashboard.png', show, return fig.

TRY THIS INPUT:
  ```python
  fig = plot_dashboard()
  print(len(fig.axes))   # 4
  ```

EXPECTED OUTPUT:
  ```
  4
  ```
  (plus a saved PNG with all four plots)

HINT:
  fig, axes = plt.subplots(2, 2)
  axes[0, 0].plot(x, np.sin(x))

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# fig = plot_dashboard()
# print(len(fig.axes))
