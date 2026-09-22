"""Level 06 — Advanced ML — Medium P01 Solution"""

import numpy as np

def oversample(X, y):
    np.random.seed(42)
    classes, counts = np.unique(y, return_counts=True)
    majority = classes[np.argmax(counts)]
    minority = classes[np.argmin(counts)]
    minority_idx = np.where(y == minority)[0]
    needed = counts.max() - len(minority_idx)
    extra_idx = np.random.choice(minority_idx, size=needed, replace=True)
    X_balanced = np.vstack([X, X[extra_idx]])
    y_balanced = np.concatenate([y, y[extra_idx]])
    return X_balanced, y_balanced

if __name__ == "__main__":
    X = np.arange(100).reshape(-1, 1)
    y = np.array([0]*95 + [1]*5)
    Xb, yb = oversample(X, y)
    print(np.bincount(yb))
