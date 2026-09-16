"""
LEVEL 03 — Data Visualization
EASY P03 — Histogram with Mean/Median Lines
========================================

CONCEPT:
  plt.hist(data, bins=20) — distribution of values.
  plt.axvline(x, ...) — vertical reference line.
  np.mean / np.median — summary stats.
  np.clip(data, 0, 100) — keep in range.

PROBLEM:
  Write `plot_histogram()` that:
    1. np.random.seed(42); scores = normal(75, 15, 200), clipped 0-100
    2. Histogram with 20 bins, edgecolor, alpha
    3. Red dashed mean line, green dashed median line (with labels)
    4. Save 'histogram.png', show, return scores array

TRY THIS INPUT:
  ```python
  scores = plot_histogram()
  print(len(scores))          # 200
  print(f"{scores.mean():.1f}")   # ~74
  print(scores.min(), scores.max())  # within 0-100
  ```

EXPECTED OUTPUT:
  ```
  200
  74.5
  ```

HINT:
  plt.axvline(np.mean(scores), color='red', linestyle='--', label='Mean')

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# s = plot_histogram()
# print(len(s), s.mean())
