"""
Decision Tree from Scratch
==========================
Implement a simple decision tree from scratch with:
- Gini impurity calculation
- Best split finding
- Recursive tree building
Train on 2D data and plot the decision boundary.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification


def gini_impurity(y):
    """Calculate Gini impurity for labels y."""
    if len(y) == 0:
        return 0.0
    classes, counts = np.unique(y, return_counts=True)
    proportions = counts / len(y)
    return 1.0 - np.sum(proportions ** 2)


def best_split(X, y):
    """Find the best feature and threshold to split on (minimize weighted Gini)."""
    n_samples, n_features = X.shape
    best_gini = float("inf")
    best_feature = None
    best_threshold = None

    for feature in range(n_features):
        thresholds = np.unique(X[:, feature])
        for threshold in thresholds:
            left_mask = X[:, feature] <= threshold
            right_mask = ~left_mask

            if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
                continue

            n_left = np.sum(left_mask)
            n_right = np.sum(right_mask)
            gini_left = gini_impurity(y[left_mask])
            gini_right = gini_impurity(y[right_mask])

            weighted_gini = (n_left * gini_left + n_right * gini_right) / n_samples

            if weighted_gini < best_gini:
                best_gini = weighted_gini
                best_feature = feature
                best_threshold = threshold

    return best_feature, best_threshold, best_gini


def build_tree(X, y, depth=0, max_depth=5):
    """Recursively build a decision tree."""
    node = {"depth": depth}

    # Stopping conditions
    if depth >= max_depth or len(np.unique(y)) == 1 or len(y) < 2:
        classes, counts = np.unique(y, return_counts=True)
        node["prediction"] = classes[np.argmax(counts)]
        node["leaf"] = True
        return node

    feature, threshold, gini = best_split(X, y)

    if feature is None:
        classes, counts = np.unique(y, return_counts=True)
        node["prediction"] = classes[np.argmax(counts)]
        node["leaf"] = True
        return node

    left_mask = X[:, feature] <= threshold
    right_mask = ~left_mask

    node["feature"] = feature
    node["threshold"] = threshold
    node["gini"] = gini
    node["leaf"] = False
    node["left"] = build_tree(X[left_mask], y[left_mask], depth + 1, max_depth)
    node["right"] = build_tree(X[right_mask], y[right_mask], depth + 1, max_depth)
    return node


def predict_one(x, tree):
    """Predict a single sample."""
    if tree["leaf"]:
        return tree["prediction"]
    if x[tree["feature"]] <= tree["threshold"]:
        return predict_one(x, tree["left"])
    else:
        return predict_one(x, tree["right"])


def predict(X, tree):
    """Predict multiple samples."""
    return np.array([predict_one(x, tree) for x in X])


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=200, n_features=2, n_informative=2, n_redundant=0,
        n_clusters_per_class=1, random_state=42
    )

    tree = build_tree(X, y, max_depth=4)
    y_pred = predict(X, tree)
    accuracy = np.mean(y_pred == y)

    print("=== Decision Tree from Scratch ===\n")
    print(f"Training accuracy: {accuracy:.4f}")
    print(f"Max depth: 4")

    # Plot decision boundary
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.05),
                         np.arange(y_min, y_max, 0.05))
    Z = predict(np.c_[xx.ravel(), yy.ravel()], tree).reshape(xx.shape)

    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.RdYlBu)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdYlBu,
                edgecolors="black", s=30)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.title("Decision Tree from Scratch - Decision Boundary")
    plt.tight_layout()
    plt.savefig("decision_tree_scratch.png", dpi=150)
    plt.show()
    print("Decision boundary saved to decision_tree_scratch.png")
