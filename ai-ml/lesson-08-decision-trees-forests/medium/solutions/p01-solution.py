"""
Random Forest on make_classification
====================================
Train a random forest on a synthetic dataset (1000 samples, 20 features).
Print accuracy, extract and plot feature importances, show top 5.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=1000, n_features=20, n_informative=8,
        n_redundant=4, n_repeated=0, random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train random forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("=== Random Forest Results ===\n")
    print(f"Test accuracy: {accuracy:.4f}")
    print(f"Number of trees: {rf.n_estimators}")

    # Feature importances
    importances = rf.feature_importances_
    indices = np.argsort(importances)[::-1]  # descending order

    print(f"\nTop 5 Most Important Features:")
    for rank, idx in enumerate(indices[:5], 1):
        print(f"  {rank}. Feature {idx:2d}: {importances[idx]:.4f}")

    # Plot all feature importances
    plt.figure(figsize=(10, 6))
    sorted_idx = np.argsort(importances)
    plt.barh(range(len(importances)), importances[sorted_idx], color="steelblue")
    plt.yticks(range(len(importances)), [f"Feature {i}" for i in sorted_idx])
    plt.xlabel("Importance")
    plt.title("Random Forest Feature Importances")
    plt.tight_layout()
    plt.savefig("rf_feature_importances.png", dpi=150)
    plt.show()
    print("Feature importance plot saved to rf_feature_importances.png")
