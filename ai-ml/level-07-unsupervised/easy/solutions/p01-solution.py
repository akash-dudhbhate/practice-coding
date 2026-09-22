"""Level 07 — Unsupervised Learning — Easy P01 Solution"""

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

def cluster():
    X, _ = make_blobs(n_samples=300, centers=3, random_state=42)
    km = KMeans(n_clusters=3, random_state=42, n_init=10)
    km.fit(X)
    return km.labels_, km.cluster_centers_

if __name__ == "__main__":
    labels, centers = cluster()
    print(len(labels))
    print(len(centers))
    print(set(labels))
