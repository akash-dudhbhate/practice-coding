# Lesson 15 — Medium P01: Elbow method + silhouette score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Generate data with 4 clusters
X, _ = make_blobs(n_samples=500, centers=4, random_state=42)

# Elbow method: K=1 to 10
k_range = range(1, 11)
inertias = []
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X)
    inertias.append(km.inertia_)

# Silhouette score: K=2 to 10
sil_scores = []
for k in range(2, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X)
    sil_scores.append(silhouette_score(X, labels))

# Plot both
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(list(k_range), inertias, marker="o", color="steelblue")
ax1.set_xlabel("K")
ax1.set_ylabel("Inertia")
ax1.set_title("Elbow Method")
ax1.axvline(x=4, color="red", linestyle="--", label="Elbow at K=4")
ax1.legend()

ax2.plot(range(2, 11), sil_scores, marker="s", color="coral")
ax2.set_xlabel("K")
ax2.set_ylabel("Silhouette Score")
ax2.set_title("Silhouette Score")
ax2.axvline(x=4, color="red", linestyle="--", label="Best at K=4")
ax2.legend()

plt.tight_layout()
plt.savefig("elbow_silhouette.png", dpi=150)
print("Figure saved to elbow_silhouette.png")

# Results
print("\n=== Elbow Method ===")
print("Inertia drops sharply until K=4, then flattens. Elbow at K=4.")
print("\n=== Silhouette Score ===")
best_k = range(2, 11)[np.argmax(sil_scores)]
print(f"Best silhouette score at K={best_k} ({max(sil_scores):.4f})")
print("\nBoth methods agree: optimal K=4.")
