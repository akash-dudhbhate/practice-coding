"""Level 07 Unsupervised — Hard P02 Solution"""

import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

def solve():
    np.random.seed(42)
    normal = np.random.randn(100, 2)
    anomalies = np.random.uniform(-4, 4, (10, 2))
    X = np.vstack([normal, anomalies])
    iso = IsolationForest(contamination=0.1, random_state=42)
    labels = iso.fit_predict(X)
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    plt.title('Anomaly Detection (Isolation Forest)')
    plt.savefig('anomalies.png', dpi=150, bbox_inches='tight')
    plt.show()
    print(f"Anomalies detected: {sum(labels == -1)}")
    return labels

if __name__ == "__main__":
    solve()