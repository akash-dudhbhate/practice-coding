"""Level 04 Supervised — Medium P03 Solution"""

from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def solve():
    X, y = make_classification(n_samples=200, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    svm = SVC(random_state=42)
    svm.fit(X_train, y_train)
    svm_acc = svm.score(X_test, y_test)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    knn_acc = knn.score(X_test, y_test)
    print(f"SVM Accuracy: {svm_acc:.4f}")
    print(f"KNN Accuracy: {knn_acc:.4f}")
    return svm_acc, knn_acc

if __name__ == "__main__":
    solve()