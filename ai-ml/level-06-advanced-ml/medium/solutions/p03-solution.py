"""Level 06 — Advanced ML — Medium P03 Solution"""

from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def reduce_pca():
    X, _ = make_classification(n_samples=200, n_features=10, n_informative=5, random_state=42)
    X_scaled = StandardScaler().fit_transform(X)
    pca = PCA(n_components=3)
    X_reduced = pca.fit_transform(X_scaled)
    return X_reduced, pca.explained_variance_ratio_

if __name__ == "__main__":
    Xr, ev = reduce_pca()
    print(Xr.shape)
    print(f"{ev.sum():.4f}")
