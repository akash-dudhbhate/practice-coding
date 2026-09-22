"""
LEVEL 07 — Unsupervised Learning
HARD P01 — Customer Segmentation
========================================

CONCEPT:
  The classic business use of clustering: group customers by
  behavior. Cluster stats (mean per group) reveal segments:
    "young big-spenders" vs "old small-spenders" etc.

  Pipeline: scale → KMeans → groupby means → interpret.

PROBLEM:
  Write `segment()` that:
    1. Creates DataFrame (200 rows, seed=42):
       age 18-70, income 20k-100k, spending 1-100
    2. StandardScaler → KMeans(5, seed=42, n_init=10)
    3. Adds 'cluster' column to df
    4. Returns (df_with_cluster, cluster_means_df)

TRY THIS INPUT:
  ```python
  df, means = segment()
  print(df.shape)     # (200, 4)
  print(means.shape)  # (5, 3)
  ```

EXPECTED OUTPUT:
  ```
  (200, 4)
  (5, 3)
  ```
  means shows e.g. cluster 0: young + high income + low spending

HINT:
  df['cluster'] = km.labels_
  means = df.groupby('cluster')[['age','income','spending']].mean()

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# df, means = segment()
# print(means)
