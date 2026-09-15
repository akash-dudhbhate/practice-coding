"""
Compare KNN: K=1, K=5, K=20
============================
Train KNN with different K values. Print train and test accuracy for each.
Show that K=1 overfits (perfect train accuracy, lower test accuracy).
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

np.random.seed(42)


if __name__ == "__main__":
    X, y = make_classification(n_samples=500, n_features=10, n_informative=5, n_redundant=2,
                               n_clusters_per_class=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    k_values = [1, 5, 20]
    print(f"{'K':>5} {'Train Acc':>12} {'Test Acc':>12} {'Gap':>8}")
    print("-" * 39)

    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        train_acc = accuracy_score(y_train, knn.predict(X_train))
        test_acc = accuracy_score(y_test, knn.predict(X_test))
        gap = train_acc - test_acc
        print(f"{k:>5} {train_acc:>12.4f} {test_acc:>12.4f} {gap:>8.4f}")

    print()
    print("Key takeaway: K=1 gives perfect training accuracy (each point is its")
    print("own nearest neighbor) but overfits -- test accuracy is lower. K=20")
    print("underfits (too much smoothing). K=5 is a good balance.")
