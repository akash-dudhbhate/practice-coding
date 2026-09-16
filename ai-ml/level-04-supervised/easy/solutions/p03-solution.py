"""Level 04 — Supervised Learning — Easy P03 Solution"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def train_tree():
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    tree = DecisionTreeClassifier(max_depth=3, random_state=42)
    tree.fit(X_train, y_train)
    acc = tree.score(X_test, y_test)
    plt.figure(figsize=(14, 8))
    plot_tree(tree, feature_names=iris.feature_names,
              class_names=iris.target_names, filled=True, rounded=True)
    plt.savefig('decision_tree.png', dpi=150, bbox_inches='tight')
    plt.close()
    return acc, tree

if __name__ == "__main__":
    acc, _ = train_tree()
    print(f"Accuracy: {acc:.4f}")
