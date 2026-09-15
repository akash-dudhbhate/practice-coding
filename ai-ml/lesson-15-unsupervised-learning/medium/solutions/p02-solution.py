# Lesson 15 — Medium P02: Compare K-Means and DBSCAN on make_moons
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler

# Generate non-spherical data (moons)
X, _ = make_moons(n_samples=300, noise=0.05, random_state=42)
X = StandardScaler().fit_transform(X)

# K-Means (K=2)
km = KMeans(n_clusters=2, random_state=42, n_init=10)
km_labels = km.fit_predict(X)

# DBSCAN
db = DBSCAN(eps=0.3, min_samples=5)
db_labels = db.fit_predict(X)

# Plot both
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.scatter(X[:, 0], X[:, 1], c=km_labels, cmap="Set1", edgecolors="k")
ax1.set_title("K-Means (K=2) — FAILS on moons")
ax1.set_xlabel("Feature 1")
ax1.set_ylabel("Feature 2")

ax2.scatter(X[:, 0], X[:, 1], c=db_labels, cmap="Set1", edgecolors="k")
ax2.set_title("DBSCAN — SUCCEEDS on moons")
ax2.set_xlabel("Feature 1")
ax2.set_ylabel("Feature 2")

plt.tight_layout()
plt.savefig("kmeans_vs_dbscan.png", dpi=150)
print("Figure saved to kmeans_vs_dbscan.png")

print("\n=== Comparison ===")
print("K-Means assumes spherical clusters, so it splits the moons incorrectly.")
print("It draws a linear boundary through the middle, assigning points from")
print("different moons to the same cluster.")
print()
print("DBSCAN finds density-connected regions, so it correctly identifies")
print("the two moon shapes as separate clusters.")
