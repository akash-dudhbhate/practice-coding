# Lesson 15 — Concepts Explained (Unsupervised Learning)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is Unsupervised Learning?

**What:** Learning patterns from data WITHOUT labels. No y — just X.

```python
# Supervised: X → y (features → label)
#   "This email is spam" (labeled)
# Unsupervised: X only (features, no labels)
#   "Group these customers into segments" (no predefined segments)
```

**Why it exists:** Most real-world data is unlabeled. Labeling is expensive and time-consuming. Unsupervised learning finds structure in unlabeled data → clustering, dimensionality reduction, anomaly detection.

**Where it's used:** Customer segmentation, anomaly detection, topic modeling, data compression, exploratory data analysis.

**What goes wrong without it:**
- Expecting specific cluster labels → unsupervised learning assigns arbitrary labels (0, 1, 2) → you must interpret them.
- No ground truth → can't calculate accuracy. Use silhouette score or domain knowledge.
- Not scaling → distance-based algorithms (K-means, DBSCAN) fail on unscaled data.

---

## K-Means Clustering

**What:** Partition data into K clusters by minimizing within-cluster variance.

```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = model.fit_predict(X)

# K-means algorithm:
# 1. Pick K random centroids
# 2. Assign each point to nearest centroid
# 3. Update centroids to cluster mean
# 4. Repeat 2-3 until centroids stabilize
```

**Why it exists:** K-means is the simplest clustering algorithm — fast, interpretable, works well when clusters are spherical and similar size. Good baseline for clustering tasks.

**Where it's used:** Customer segmentation, image compression, document clustering, any task with roughly spherical clusters.

**What goes wrong without it:**
- Wrong K → too few clusters merge distinct groups, too many split one group. Use the elbow method or silhouette score.
- Non-spherical clusters → K-means fails (it assumes circular clusters). Use DBSCAN or spectral clustering.
- Not scaling → features with large ranges dominate the distance → wrong clusters. Always scale.
- `n_init=10` → runs 10 times with different initial centroids → picks the best. Default changed in newer sklearn.

---

## Choosing K (Elbow Method)

**What:** Plot inertia (within-cluster sum of squares) vs K → look for the "elbow."

```python
import matplotlib.pyplot as plt

inertias = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

plt.plot(range(1, 11), inertias, 'bo-')
plt.xlabel('K')
plt.ylabel('Inertia')
plt.title('Elbow Method')
# Look for the "elbow" — where inertia stops decreasing rapidly
```

**Why it exists:** Without a method to choose K, you guess → might pick the wrong number. The elbow method provides a data-driven way to choose K → the point where adding more clusters doesn't help much.

**Where it's used:** Every K-means clustering task.

**What goes wrong without it:**
- Elbow is not always clear → subjective. Use silhouette score as a complement.
- Inertia always decreases with K → can't just pick the minimum. The elbow is the "knee" in the curve.
- K=1 always has the highest inertia → don't pick K=1 unless there's truly one cluster.

---

## Silhouette Score

**What:** Measures how similar a point is to its own cluster vs other clusters. Range: -1 to 1.

```python
from sklearn.metrics import silhouette_score

for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, clusters)
    print(f"K={k}: silhouette={score:.3f}")

# silhouette = 1 → perfect clustering (point is in the right cluster)
# silhouette = 0 → overlapping clusters
# silhouette = -1 → wrong cluster (point is closer to another cluster)
```

**Why it exists:** The elbow method is subjective. Silhouette score is quantitative → higher is better → pick K with the highest score. Also works when the elbow is unclear.

**Where it's used:** Choosing K, evaluating clustering quality, comparing clustering algorithms.

**What goes wrong without it:**
- Silhouette score favors convex (spherical) clusters → DBSCAN (non-convex) might score low even when clustering is good.
- Silhouette is O(n²) → slow for large datasets. Use a sample: `silhouette_score(X, clusters, sample_size=10000)`.
- High silhouette doesn't mean the clusters are meaningful → you still need domain interpretation.

---

## DBSCAN

**What:** Density-based clustering — groups points that are close together, marks isolated points as noise.

```python
from sklearn.cluster import DBSCAN

model = DBSCAN(eps=0.5, min_samples=5)
clusters = model.fit_predict(X_scaled)

# eps: maximum distance between points in the same cluster
# min_samples: minimum points to form a cluster
# Cluster -1 = noise (outlier)

# Advantages over K-means:
# - Doesn't need K (finds clusters automatically)
# - Handles non-spherical clusters
# - Detects outliers (noise)
```

**Why it exists:** K-means needs K and assumes spherical clusters. DBSCAN finds clusters of any shape and detects outliers → better for real-world data with irregular clusters.

**Where it's used:** Anomaly detection, spatial data, non-spherical clusters, outlier detection.

**What goes wrong without it:**
- `eps` too small → every point is noise. `eps` too large → all points in one cluster. Use k-distance plot to choose eps.
- `min_samples` too low → noise becomes clusters. Rule of thumb: min_samples = 2 * n_features.
- DBSCAN struggles with varying densities → some clusters are dense, some sparse → use HDBSCAN.

---

## Hierarchical Clustering

**What:** Builds a tree of clusters (dendrogram) → cut at a level to get K clusters.

```python
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch

# Plot dendrogram
dendrogram = sch.dendrogram(sch.linkage(X_scaled, method='ward'))

# Cut at a level to get clusters
model = AgglomerativeClustering(n_clusters=3, linkage='ward')
clusters = model.fit_predict(X_scaled)
```

**Why it exists:** K-means needs K upfront. Hierarchical clustering shows ALL possible clusterings in a dendrogram → you can choose K after seeing the structure → more informative.

**Where it's used:** Bioinformatics (phylogenetic trees), taxonomy, any domain where cluster hierarchy is meaningful.

**What goes wrong without it:**
- `linkage='ward'` → minimizes variance (like K-means). `single` → chains (long clusters). `complete` → compact clusters. Choose based on expected cluster shape.
- O(n³) → slow for large datasets. Use K-means or DBSCAN for n > 10,000.
- Dendrogram is unreadable for large datasets → only useful for small data.

---

## PCA (Dimensionality Reduction)

**What:** Principal Component Analysis reduces dimensions while preserving variance.

```python
from sklearn.decomposition import PCA

# Reduce to 2 dimensions for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"Explained variance: {pca.explained_variance_ratio_}")
# [0.72, 0.23] → first component explains 72%, second 23%
# Total: 95% of variance preserved
```

**Why it exists:** High-dimensional data is hard to visualize and can cause the curse of dimensionality. PCA reduces dimensions while keeping most of the information → visualization, faster training, less noise.

**Where it's used:** Visualization (2D/3D), preprocessing before ML, noise reduction, feature compression.

**What goes wrong without it:**
- Not scaling before PCA → features with large variance dominate the first component → meaningless. Always scale.
- Too few components → lose too much information. Check `explained_variance_ratio_` → keep enough to explain 90-95%.
- Interpreting components → PC1 is a linear combination of all features → hard to interpret. Look at `pca.components_` for feature weights.

---

## Anomaly Detection

**What:** Identify outliers — points that are very different from the rest.

```python
from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.05, random_state=42)
# contamination: expected fraction of outliers
outliers = model.fit_predict(X)
# -1 = outlier, 1 = normal

# Other methods:
# - DBSCAN: points not in any cluster are noise
# - Local Outlier Factor: points with low local density
# - One-class SVM: learns the boundary of normal data
```

**Why it exists:** Anomalies can indicate fraud, defects, errors, or rare events. Detecting them is valuable → fraud detection, manufacturing quality, medical anomalies.

**Where it's used:** Fraud detection, network intrusion, manufacturing defects, medical anomalies.

**What goes wrong without it:**
- `contamination` too high → normal points flagged as anomalies. Too low → real anomalies missed.
- Not scaling → Isolation Forest is tree-based → OK, but LOF and One-class SVM need scaling.
- No ground truth → can't evaluate anomaly detection easily. Use synthetic anomalies or domain expert review.
