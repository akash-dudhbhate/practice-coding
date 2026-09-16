"""Level 04 Supervised — Easy P03 Solution"""

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def solve():
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    tree = DecisionTreeClassifier(max_depth=3, random_state=42)
    tree.fit(X_train, y_train)
    accuracy = tree.score(X_test, y_test)
    print(f"Accuracy: {accuracy:.4f}")
    plt.figure(figsize=(14, 8))
    plot_tree(tree, feature_names=iris.feature_names,
              class_names=iris.target_names, filled=True, rounded=True)
    plt.savefig('decision_tree.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("Tree saved to decision_tree.png")
    return accuracy

if __name__ == "__main__":
    solve()