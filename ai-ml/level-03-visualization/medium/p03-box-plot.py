"""
LEVEL 03 — Data Visualization
MEDIUM P03 — Box Plot with Swarm Overlay
========================================

CONCEPT:
  sns.boxplot — shows median, quartiles, outliers per group.
  sns.swarmplot — shows every data point on top.
  Together: shape of distribution AND raw points.

PROBLEM:
  Write `plot_box()` that:
    1. np.random.seed(42)
    2. DataFrame: category A/B/C/D (50 rows each),
       values = normal(50,10), normal(60,15), normal(55,12), normal(70,8)
    3. sns.boxplot + sns.swarmplot overlay
    4. Save 'boxplot.png', show, return the DataFrame

TRY THIS INPUT:
  ```python
  df = plot_box()
  print(df.shape)                        # (200, 2)
  print(df.groupby('category')['value'].mean())
  ```

EXPECTED OUTPUT:
  ```
  (200, 2)
  category
  A    ~50
  B    ~60
  C    ~55
  D    ~70
  ```

HINT:
  np.repeat(['A','B','C','D'], 50) for categories.
  np.concatenate([...]) for the four value groups.

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# df = plot_box()
# print(df.groupby('category')['value'].mean())
