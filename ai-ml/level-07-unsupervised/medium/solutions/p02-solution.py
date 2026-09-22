"""Level 07 — Unsupervised Learning — Medium P02 Solution"""

from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, DBSCAN

def compare_algorithms():
    X, _ = make_moons(n_samples=300, noise=0.05, random_state=42)
    km_labels = KMeans(n_clusters=2, random_state=42, n_init=10).fit_predict(X)
    db_labels = DBSCAN(eps=0.3, min_samples=5).fit_predict(X)
    return km_labels, db_labels

if __name__ == "__main__":
    km, db = compare_algorithms()
    print(f"KMeans clusters: {len(set(km))}")
    print(f"DBSCAN clusters: {len(set(db))}")
