"""Level 07 — Unsupervised Learning — Easy P03 Solution"""

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def pca_2d():
    iris = load_iris()
    X = StandardScaler().fit_transform(iris.data)
    pca = PCA(n_components=2)
    X_2d = pca.fit_transform(X)
    return X_2d, pca.explained_variance_ratio_

if __name__ == "__main__":
    X2, ev = pca_2d()
    print(X2.shape)
    print(f"{ev[0]:.4f}")
    print(f"{ev.sum():.4f}")
