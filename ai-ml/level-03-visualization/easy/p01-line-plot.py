"""
LEVEL 03 — Data Visualization
EASY P01 — Line Plot of Trig Functions
========================================

CONCEPT:
  matplotlib is the core plotting library.
    plt.plot(x, y, label=...) — line plot
    plt.xlabel / ylabel / title — labels
    plt.legend() — show labels
    plt.grid(True) — grid lines
    plt.savefig('file.png') — save figure

PROBLEM:
  Write `plot_trig()` that:
    1. Creates x = np.linspace(0, 10, 100)
    2. Plots sin(x) and cos(x) on the same figure
    3. Adds labels, title, legend, grid
    4. Saves to 'trig_plot.png' and shows it
    5. Returns the x array (so check.py can verify)

TRY THIS INPUT:
  ```python
  x = plot_trig()
  print(len(x))       # 100
  print(x[0], x[-1])  # 0.0 10.0
  ```

EXPECTED OUTPUT:
  ```
  100
  0.0 10.0
  ```
  (plus a saved PNG with both curves)

HINT:
  import matplotlib.pyplot as plt
  plt.plot(x, np.sin(x), label='sin(x)')

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# x = plot_trig()
# print(len(x))
