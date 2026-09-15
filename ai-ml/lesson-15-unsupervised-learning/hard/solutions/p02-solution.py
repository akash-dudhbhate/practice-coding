# Lesson 15 — Hard P02: Anomaly detection pipeline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import StandardScaler

# Create dataset with 5% anomalies
np.random.seed(42)
n_normal = 380
n_anomaly = 20
X_normal = np.random.randn(n_normal, 2) * 2
X_anomaly = np.random.uniform(-10, 10, size=(n_anomaly, 2))
X = np.vstack([X_normal, X_anomaly])
y_true = np.array([0] * n_normal + [1] * n_anomaly)  # 0=normal, 1=anomaly

X_scaled = StandardScaler().fit_transform(X)

# Method 1: Isolation Forest
iso = IsolationForest(contamination=0.05, random_state=42)
iso_pred = (iso.fit_predict(X_scaled) == -1).astype(int)

# Method 2: DBSCAN (noise points = anomalies)
db = DBSCAN(eps=0.8, min_samples=5)
db_labels = db.fit_predict(X_scaled)
db_pred = (db_labels == -1).astype(int)

# Method 3: Local Outlier Factor
lof = LocalOutlierFactor(contamination=0.05)
lof_pred = (lof.fit_predict(X_scaled) == -1).astype(int)

# Calculate detection rate
def detection_rate(pred, true):
    detected = ((pred == 1) & (true == 1)).sum()
    total = (true == 1).sum()
    return detected / total

results = pd.DataFrame({
    "Method": ["Isolation Forest", "DBSCAN", "Local Outlier Factor"],
    "Detected Anomalies": [iso_pred.sum(), db_pred.sum(), lof_pred.sum()],
    "True Anomalies": [n_anomaly] * 3,
    "Detection Rate": [detection_rate(iso_pred, y_true), detection_rate(db_pred, y_true), detection_rate(lof_pred, y_true)],
})
print(results.to_string(index=False))

# Visualize
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for ax, pred, name in zip(axes, [iso_pred, db_pred, lof_pred], ["Isolation Forest", "DBSCAN", "LOF"]):
    normal = pred == 0
    anomaly = pred == 1
    ax.scatter(X_scaled[normal, 0], X_scaled[normal, 1], c="blue", alpha=0.5, label="Normal")
    ax.scatter(X_scaled[anomaly, 0], X_scaled[anomaly, 1], c="red", marker="X", s=80, label="Anomaly")
    ax.set_title(name)
    ax.legend()

plt.tight_layout()
plt.savefig("anomaly_detection.png", dpi=150)
print("\nFigure saved to anomaly_detection.png")
