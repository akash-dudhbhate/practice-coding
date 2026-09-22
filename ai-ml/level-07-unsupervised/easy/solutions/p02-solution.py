"""Level 07 — Unsupervised Learning — Easy P02 Solution"""

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

def elbow():
    X, _ = make_blobs(n_samples=300, centers=3, random_state=42)
    inertias = []
    for k in range(1, 11):
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        km.fit(X)
        inertias.append(km.inertia_)
    return inertias

if __name__ == "__main__":
    ins = elbow()
    print(len(ins))
    print(f"{ins[0]:.0f}")
    print(f"{ins[2]:.0f}")
