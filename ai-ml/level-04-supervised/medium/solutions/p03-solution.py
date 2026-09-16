"""Level 04 — Supervised Learning — Medium P03 Solution"""

from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def compare_models():
    X, y = make_classification(n_samples=200, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    svm = SVC(random_state=42).fit(X_train, y_train)
    knn = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
    return svm.score(X_test, y_test), knn.score(X_test, y_test)

if __name__ == "__main__":
    svm_acc, knn_acc = compare_models()
    print(f"SVM: {svm_acc:.4f}")
    print(f"KNN: {knn_acc:.4f}")
