"""Level 07 — Unsupervised Learning — Hard P01 Solution"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def segment():
    np.random.seed(42)
    df = pd.DataFrame({
        'age': np.random.randint(18, 70, 200),
        'income': np.random.randint(20000, 100000, 200),
        'spending': np.random.randint(1, 100, 200),
    })
    X = StandardScaler().fit_transform(df)
    km = KMeans(n_clusters=5, random_state=42, n_init=10)
    df['cluster'] = km.fit_predict(X)
    means = df.groupby('cluster')[['age', 'income', 'spending']].mean()
    return df, means

if __name__ == "__main__":
    df, means = segment()
    print(df.shape)
    print(means.shape)
    print(means.round(1))
