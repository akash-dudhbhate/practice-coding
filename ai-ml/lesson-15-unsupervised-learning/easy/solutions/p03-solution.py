# Lesson 15 — Easy P03: Isolation Forest for outlier detection
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Create dataset with injected outliers using the modern numpy.random.Generator API
rng = np.random.default_rng(42)
n_normal = 200
X_normal = rng.standard_normal((n_normal, 2)) * 1.5
# Inject 10 outliers far from the normal data
X_outliers = rng.uniform(low=8, high=12, size=(10, 2))
X = np.vstack([X_normal, X_outliers])

# Fit Isolation Forest
iso = IsolationForest(contamination=0.05, random_state=42)
predictions = iso.fit_predict(X)

outlier_mask = predictions == -1
normal_mask = predictions == 1

print(f"Total points: {len(X)}")
print(f"Normal points: {normal_mask.sum()}")
print(f"Outlier points: {outlier_mask.sum()}")
print(f"Outlier indices: {np.nonzero(outlier_mask)[0]}")

# Visualize
plt.figure(figsize=(8, 6))
plt.scatter(X[normal_mask, 0], X[normal_mask, 1], c="blue", label="Normal", alpha=0.6)
plt.scatter(X[outlier_mask, 0], X[outlier_mask, 1], c="red", label="Outlier", s=100, marker="X")
plt.title("Isolation Forest: Outlier Detection")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.tight_layout()
plt.savefig("isolation_forest.png", dpi=150)
print("Figure saved to isolation_forest.png")
