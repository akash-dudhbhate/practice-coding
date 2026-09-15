"""
Decision Tree on Iris with Visualization
========================================
Train a decision tree on the Iris dataset with max_depth=3.
Print accuracy and visualize the tree using plot_tree.
"""

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score


if __name__ == "__main__":
    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train decision tree with max_depth=3
    tree = DecisionTreeClassifier(max_depth=3, random_state=42)
    tree.fit(X_train, y_train)

    y_pred = tree.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("=== Decision Tree on Iris (max_depth=3) ===\n")
    print(f"Train accuracy: {tree.score(X_train, y_train):.4f}")
    print(f"Test accuracy:  {accuracy:.4f}")

    # Visualize the tree
    plt.figure(figsize=(14, 8))
    plot_tree(tree, feature_names=iris.feature_names,
              class_names=iris.target_names, filled=True, rounded=True,
              fontsize=10)
    plt.title("Decision Tree - Iris Dataset (max_depth=3)")
    plt.tight_layout()
    plt.savefig("decision_tree_iris.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Tree visualization saved to decision_tree_iris.png")
