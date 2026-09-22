"""
LEVEL 03 PROJECT — Auto EDA Dashboard
========================================

Build `make_dashboard(df)` that produces a 4-panel PNG summary
of ANY numeric dataframe — the kind of first-look report a data
scientist generates before modeling.

DATA: seaborn's built-in "tips" dataset (no download needed).

DASHBOARD LAYOUT (2×2 subplots, saved to 'dashboard.png'):
  [0,0] histogram of total_bill
  [0,1] scatter: total_bill vs tip (colored by sex)
  [1,0] boxplot: tip by day
  [1,1] correlation heatmap of numeric columns

CONTRACT:
  make_dashboard(df) -> dict with keys:
      "shape": df.shape,
      "numeric_cols": list of numeric column names,
      "top_corr": (col_a, col_b, corr) — strongest off-diagonal pair,
      "saved_to": "dashboard.png"

RUN:
  ```python
  import seaborn as sns
  stats = make_dashboard(sns.load_dataset("tips"))
  print(stats["top_corr"])
  ```

EXPECTED OUTPUT:
  ```
  ('total_bill', 'tip', ~0.68)
  dashboard.png written (2x2 figure, no GUI window)
  ```

RULES:
  - matplotlib.use("Agg") BEFORE pyplot import — headless safe
  - plt.savefig(...); plt.close() — never plt.show()
  - Return the stats dict so checkers can verify you

HINT: df.corr(numeric_only=True) → mask diagonal → idxmax
"""

# === WRITE YOUR CODE BELOW ===

def make_dashboard(df):
    # TODO: 4-panel figure + stats dict
    pass


if __name__ == "__main__":
    import matplotlib
    matplotlib.use("Agg")
    import seaborn as sns
    stats = make_dashboard(sns.load_dataset("tips"))
    print(stats)
