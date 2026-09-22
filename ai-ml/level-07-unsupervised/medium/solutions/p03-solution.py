"""Level 07 — Unsupervised Learning — Medium P03 Solution"""

from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering

def hierarchical():
    X, _ = make_blobs(n_samples=50, centers=3, random_state=42)
    labels = AgglomerativeClustering(n_clusters=3).fit_predict(X)
    return labels

if __name__ == "__main__":
    labels = hierarchical()
    print(len(labels))
    print(set(labels))
