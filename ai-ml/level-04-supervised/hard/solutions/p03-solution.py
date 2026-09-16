"""Level 04 — Supervised Learning — Hard P03 Solution"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def select_features():
    X, y = make_classification(n_samples=200, n_features=10, n_informative=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rfe = RFE(estimator=RandomForestClassifier(random_state=42), n_features_to_select=5)
    rfe.fit(X_train, y_train)
    selected = rfe.support_
    rf = RandomForestClassifier(random_state=42)
    rf.fit(X_train[:, selected], y_train)
    acc = rf.score(X_test[:, selected], y_test)
    return np.where(selected)[0].tolist(), acc

if __name__ == "__main__":
    features, acc = select_features()
    print(f"Selected features: {features}")
    print(f"Accuracy: {acc:.4f}")
