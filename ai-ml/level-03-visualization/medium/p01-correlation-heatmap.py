"""
LEVEL 03 — Data Visualization
MEDIUM P01 — Correlation Heatmap
========================================

CONCEPT:
  Correlation = how much two variables move together (-1 to +1).
  df.corr() → correlation matrix.
  sns.heatmap(matrix, annot=True, cmap='coolwarm', center=0)
    — color-coded grid; red=positive, blue=negative.

PROBLEM:
  Write `plot_corr()` that:
    1. np.random.seed(42); DataFrame with 5 columns
       (feature_a..feature_d, target) of 100 random normals
    2. Computes corr matrix
    3. sns.heatmap with annot=True, coolwarm, fmt='.2f'
    4. Save 'correlation_heatmap.png', show, return corr matrix

TRY THIS INPUT:
  ```python
  corr = plot_corr()
  print(corr.shape)           # (5, 5)
  print(corr.loc['feature_a','feature_a'])  # 1.0 (self-corr)
  ```

EXPECTED OUTPUT:
  ```
  (5, 5)
  1.0
  ```

HINT:
  import seaborn as sns
  corr = df.corr()

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# c = plot_corr()
# print(c.shape)
