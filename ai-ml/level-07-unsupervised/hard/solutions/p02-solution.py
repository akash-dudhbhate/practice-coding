"""Level 07 — Unsupervised Learning — Hard P02 Solution"""

import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies():
    np.random.seed(42)
    normal = np.random.normal(0, 0.5, (100, 2))
    outliers = np.random.uniform(-5, 5, (10, 2))
    X = np.vstack([normal, outliers])
    iso = IsolationForest(contamination=0.1, random_state=42)
    preds = iso.fit_predict(X)
    n_anomalies = (preds == -1).sum()
    return preds, n_anomalies

if __name__ == "__main__":
    preds, n = detect_anomalies()
    print(len(preds))
    print(f"Anomalies detected: {n}")
