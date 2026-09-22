"""
LEVEL 03 — Data Visualization
HARD P03 — Publication-Quality Figure
========================================

CONCEPT:
  Publication figures need: serif fonts, no top/right spines,
  fill_between for shading, tight_layout, and 300 DPI export.

  matplotlib.rcParams['font.family'] = 'serif'
  ax.spines['top'].set_visible(False)
  plt.savefig('fig.png', dpi=300)

PROBLEM:
  Write `plot_publication()` that:
    1. Serif font, size 12
    2. x = linspace(0, 10, 100); plot sin(x) and cos(x)
    3. fill_between shading between curves
    4. No top/right spines, legend, grid
    5. Save 'publication_figure.png' at dpi=300, show, return x

TRY THIS INPUT:
  ```python
  x = plot_publication()
  import os
  print(os.path.exists('publication_figure.png'))  # True
  ```

EXPECTED OUTPUT:
  ```
  True
  ```
  (plus a high-res PNG)

HINT:
  ax.fill_between(x, np.sin(x), np.cos(x), alpha=0.2)

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# import os
# x = plot_publication()
# print(os.path.exists('publication_figure.png'))
