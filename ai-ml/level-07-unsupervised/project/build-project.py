"""
LEVEL 07 PROJECT — Customer Segmenter
========================================

A retail client wants to target customers differently.
Segment them — no labels exist, that's the point of clustering.

DATA: synthetic customers — generate with the code in __main__
(age, annual_income_k, spending_score) — 300 customers.

BUILD `segment_customers(df)`:
  1. StandardScaler on the 3 features
  2. Try K=2..6 with KMeans; pick best by silhouette_score
  3. Attach labels to df; compute per-cluster means
  4. PRINT a human-readable profile per segment, e.g.:
     "Segment 0: age~25, income~$30k, spend~high → young big-spenders"
  5. Return (best_k, labels, segment_profiles_dict)

EXPECTED OUTPUT SHAPE:
  ```
  Best K: 4 (silhouette=0.xx)
  Segment 0: n=78, age=xx, income=xx, spend=xx
  ...
  ```

REAL-WORLD NOTE: segments only matter if a human can describe them.
  "Cluster 2" means nothing to a marketing team — a NAME does.
  Auto-name each segment from its means (e.g. high spend + low
  income → "aspirational").

HINT: df.groupby('cluster').mean()
"""

import numpy as np
import pandas as pd


def make_customers():
    rng = np.random.RandomState(42)
    n = 300
    return pd.DataFrame({
        "age": rng.normal(40, 12, n).clip(18, 70).round(),
        "income_k": rng.normal(60, 25, n).clip(15, 150).round(),
        "spend_score": rng.normal(50, 25, n).clip(1, 100).round(),
    })


def segment_customers(df):
    # TODO
    pass


if __name__ == "__main__":
    df = make_customers()
    segment_customers(df)
