# Level 07 Unsupervised — Unsupervised Learning

## What You'll Learn
- K-Means clustering
- Hierarchical clustering
- DBSCAN
- Dimensionality reduction
- Anomaly detection
- Association rules

## Prerequisites
- Previous levels completed
- Python basics

## How This Level Works

Each problem has:
1. **CONCEPT** — the idea you need to understand
2. **PROBLEM** — what to build
3. **TRY THIS INPUT** — test code to verify your solution
4. **EXPECTED OUTPUT** — what it should print
5. **AUTO-CHECK** — run `check.py` to verify automatically

Start with `easy/` problems, then `medium/`, then `hard/`, then the project.

---

## Problems

### Easy
1. `easy/p01-kmeans-basic.py` — Apply K-Means to a dataset. Print cluster centers and labels...
2. `easy/p02-elbow-method.py` — Use the elbow method to find optimal K. Plot inertias....
3. `easy/p03-pca-basic.py` — Apply PCA to reduce 4D data to 2D. Plot the result....

### Medium
4. `medium/p01-silhouette-score.py` — Use silhouette score to evaluate clustering quality....
5. `medium/p02-dbscan-vs-kmeans.py` — Compare K-Means and DBSCAN on non-spherical data....
6. `medium/p03-hierarchical.py` — Apply hierarchical clustering. Plot dendrogram....

### Hard
7. `hard/p01-customer-segmentation.py` — Build a customer segmentation pipeline with profiling....
8. `hard/p02-anomaly-detection.py` — Detect anomalies using isolation forest or LOF....
9. `hard/p03-topic-modeling.py` — Apply LDA to discover topics in text data....

### Project
`project/` — Build a customer segmentation engine with cluster profiling and visualization.

---

## Verify Your Work

```bash
# Run a problem
python3 easy/p01-kmeans-basic.py

# Check your answer
python3 check.py easy/p01
```

When `check.py` says "PASS", add `# DONE` to the first line and move on.
