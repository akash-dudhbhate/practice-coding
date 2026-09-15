"""
Demonstrate overfitting and L2 regularization
=============================================
Train a large MLP (100,100,100) on a small dataset to show overfitting
(train=100%, test low). Then add alpha=0.1 (L2 regularization) and show improvement.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


if __name__ == "__main__":
    # Small dataset to encourage overfitting
    X, y = make_classification(
        n_samples=200, n_features=20, n_informative=5, n_redundant=5,
        n_classes=2, random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")
    print(f"Features: {X.shape[1]}\n")

    # --- Overfitting model: large network, no regularization ---
    print("--- Overfitting Model (alpha=0, hidden=(100,100,100)) ---")
    mlp_overfit = MLPClassifier(
        hidden_layer_sizes=(100, 100, 100), alpha=0.0,
        max_iter=1000, random_state=42
    )
    mlp_overfit.fit(X_train_s, y_train)
    train_acc_of = accuracy_score(y_train, mlp_overfit.predict(X_train_s))
    test_acc_of = accuracy_score(y_test, mlp_overfit.predict(X_test_s))
    print(f"Train accuracy: {train_acc_of:.4f}")
    print(f"Test  accuracy: {test_acc_of:.4f}")
    print(f"Gap (train-test): {train_acc_of - test_acc_of:.4f}  <- large gap = overfitting")

    # --- Regularized model: same network, alpha=0.1 (L2) ---
    print("\n--- Regularized Model (alpha=0.1, hidden=(100,100,100)) ---")
    mlp_reg = MLPClassifier(
        hidden_layer_sizes=(100, 100, 100), alpha=0.1,
        max_iter=1000, random_state=42
    )
    mlp_reg.fit(X_train_s, y_train)
    train_acc_reg = accuracy_score(y_train, mlp_reg.predict(X_train_s))
    test_acc_reg = accuracy_score(y_test, mlp_reg.predict(X_test_s))
    print(f"Train accuracy: {train_acc_reg:.4f}")
    print(f"Test  accuracy: {test_acc_reg:.4f}")
    print(f"Gap (train-test): {train_acc_reg - test_acc_reg:.4f}")

    # --- Comparison ---
    print("\n--- Comparison ---")
    print(f"{'Model':<25} {'Train':<10} {'Test':<10} {'Gap':<10}")
    print("-" * 55)
    print(f"{'Overfit (alpha=0)':<25} {train_acc_of:<10.4f} {test_acc_of:<10.4f} {train_acc_of - test_acc_of:<10.4f}")
    print(f"{'Regularized (alpha=0.1)':<25} {train_acc_reg:<10.4f} {test_acc_reg:<10.4f} {train_acc_reg - test_acc_reg:<10.4f}")
    print(f"\nTest accuracy improvement: {test_acc_reg - test_acc_of:+.4f}")
    print(f"L2 regularization shrinks weights, reducing memorization and improving generalization.")
