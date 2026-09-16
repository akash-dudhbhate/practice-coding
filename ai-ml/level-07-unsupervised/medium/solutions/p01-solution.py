"""Level 07 — Unsupervised Learning — Medium P01 Solution"""

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

def best_k():
    X, _ = make_blobs(n_samples=300, centers=3, random_state=42)
    scores = {}
    for k in range(2, 8):
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = km.fit_predict(X)
        scores[k] = silhouette_score(X, labels)
    best = max(scores, key=scores.get)
    return best, scores[best], scores

if __name__ == "__main__":
    k, s, all_s = best_k()
    print(f"Best K: {k} (silhouette={s:.4f})")
    for kk, ss in all_s.items():
        print(f"  K={kk}: {ss:.4f}")
