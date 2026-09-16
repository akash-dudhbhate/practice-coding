"""Level 07 Unsupervised — Easy P03 Solution"""

import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def solve():
    iris = load_iris()
    X = iris.data
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target, cmap='viridis')
    plt.xlabel('First Principal Component')
    plt.ylabel('Second Principal Component')
    plt.title('PCA of Iris Dataset')
    plt.colorbar(scatter)
    plt.savefig('pca.png', dpi=150, bbox_inches='tight')
    plt.show()
    print(f"Explained variance: {pca.explained_variance_ratio_}")
    return X_pca

if __name__ == "__main__":
    solve()