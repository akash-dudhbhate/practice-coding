"""
Tune max_depth for Decision Tree
================================
Test different max_depth values [1, 3, 5, 10, 20, None].
Record train and test accuracy. Plot both curves and identify optimal depth.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=800, n_features=15, n_informative=8,
        n_redundant=3, random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    depths = [1, 3, 5, 10, 20, None]
    depth_labels = [str(d) if d is not None else "None" for d in depths]

    train_accs = []
    test_accs = []

    print(f"{'Depth':<10} {'Train Acc':<15} {'Test Acc':<15}")
    print("-" * 40)

    for depth in depths:
        tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
        tree.fit(X_train, y_train)

        tr_acc = tree.score(X_train, y_train)
        te_acc = tree.score(X_test, y_test)
        train_accs.append(tr_acc)
        test_accs.append(te_acc)

        label = str(depth) if depth is not None else "None"
        print(f"{label:<10} {tr_acc:<15.4f} {te_acc:<15.4f}")

    # Find optimal depth (highest test accuracy)
    best_idx = np.argmax(test_accs)
    print(f"\nOptimal depth: {depth_labels[best_idx]} (test acc = {test_accs[best_idx]:.4f})")

    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(range(len(depths)), train_accs, "o-", label="Train Accuracy", color="blue")
    plt.plot(range(len(depths)), test_accs, "s-", label="Test Accuracy", color="red")
    plt.xticks(range(len(depths)), depth_labels)
    plt.xlabel("max_depth")
    plt.ylabel("Accuracy")
    plt.title("Decision Tree: Train vs Test Accuracy by max_depth")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("depth_tuning.png", dpi=150)
    plt.show()
    print("Plot saved to depth_tuning.png")

    print("\n=== Interpretation ===")
    print("Depth=1: underfitting (both train and test low).")
    print("Depth=None: overfitting (train=1.0, test drops).")
    print("Optimal depth balances complexity and generalization.")
