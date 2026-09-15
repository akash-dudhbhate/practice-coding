"""
Train MLPClassifier with different architectures
=================================================
Compare MLP architectures: (8,), (16,8), (32,16,8).
Report accuracy and training time for each. Identify the best.
"""

import time
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


if __name__ == "__main__":
    # Load and prepare data
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    # Architectures to compare
    architectures = [(8,), (16, 8), (32, 16, 8)]

    results = []
    print("--- Architecture Comparison ---\n")
    print(f"{'Architecture':<20} {'Accuracy':<12} {'Train Time (s)':<16}")
    print("-" * 48)

    for arch in architectures:
        mlp = MLPClassifier(hidden_layer_sizes=arch, max_iter=500, random_state=42)

        start = time.time()
        mlp.fit(X_train_s, y_train)
        train_time = time.time() - start

        y_pred = mlp.predict(X_test_s)
        acc = accuracy_score(y_test, y_pred)

        results.append((arch, acc, train_time))
        print(f"{str(arch):<20} {acc:<12.4f} {train_time:<16.4f}")

    # Identify best by accuracy
    best = max(results, key=lambda r: r[1])
    fastest = min(results, key=lambda r: r[2])
    print(f"\nBest accuracy:    {best[0]} -> {best[1]:.4f}")
    print(f"Fastest training: {fastest[0]} -> {fastest[2]:.4f}s")
    print(f"\nNote: On Iris (small, simple), all architectures may achieve similar")
    print(f"accuracy. Larger networks train slower with no accuracy gain — a classic")
    print(f"illustration that bigger is not always better.")
