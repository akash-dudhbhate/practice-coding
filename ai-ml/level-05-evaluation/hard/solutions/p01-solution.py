"""Level 05 Evaluation — Hard P01 Solution"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve

def solve():
    X, y = make_classification(n_samples=1000, n_features=10, weights=[0.9, 0.1], random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(random_state=42)
    model.fit(X_train, y_train)
    y_prob = model.predict_proba(X_test)[:, 1]
    precisions, recalls, thresholds = precision_recall_curve(y_test, y_prob)
    idx = np.argmin(np.abs(recalls - 0.8))
    threshold = thresholds[idx]
    precision = precisions[idx]
    print(f"Threshold for 80% recall: {threshold:.4f}")
    print(f"Precision at that threshold: {precision:.4f}")
    return threshold, precision

if __name__ == "__main__":
    solve()