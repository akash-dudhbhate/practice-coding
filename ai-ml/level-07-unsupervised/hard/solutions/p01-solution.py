"""Level 07 Unsupervised — Hard P01 Solution"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def solve():
    np.random.seed(42)
    data = pd.DataFrame({
        'age': np.random.randint(18, 70, 300),
        'income': np.random.randn(300) * 20000 + 60000,
        'spending': np.random.uniform(1, 100, 300)
    })
    X = StandardScaler().fit_transform(data)
    # Find optimal K
    sil_scores = []
    for k in range(2, 8):
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = km.fit_predict(X)
        from sklearn.metrics import silhouette_score
        sil_scores.append(silhouette_score(X, labels))
    best_k = np.argmax(sil_scores) + 2
    km = KMeans(n_clusters=best_k, random_state=42, n_init=10)
    labels = km.fit_predict(X)
    data['cluster'] = labels
    # Profile clusters
    print(data.groupby('cluster').mean())
    # Visualize
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis')
    plt.title('Customer Segments')
    plt.savefig('segments.png', dpi=150, bbox_inches='tight')
    plt.show()
    return data

if __name__ == "__main__":
    solve()