"""Level 06 Advanced Ml — Medium P03 Solution"""

import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

def solve():
    iris = load_iris()
    X = iris.data
    pca = PCA()
    X_pca = pca.fit_transform(X)
    print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
    print(f"Cumulative: {np.cumsum(pca.explained_variance_ratio_)}")
    plt.figure(figsize=(10, 6))
    plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_)
    plt.xlabel('Principal Component')
    plt.ylabel('Explained Variance Ratio')
    plt.title('PCA Explained Variance')
    plt.savefig('pca_variance.png', dpi=150, bbox_inches='tight')
    plt.show()
    return pca.explained_variance_ratio_

if __name__ == "__main__":
    solve()