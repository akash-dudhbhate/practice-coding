"""
KNN on Iris (Scaled vs Unscaled)
================================
Train KNN (K=5) on the Iris dataset. Show that scaling features improves
accuracy, because KNN relies on distance calculations.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


if __name__ == "__main__":
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # --- Unscaled ---
    knn_unscaled = KNeighborsClassifier(n_neighbors=5)
    knn_unscaled.fit(X_train, y_train)
    acc_unscaled = accuracy_score(y_test, knn_unscaled.predict(X_test))

    # --- Scaled ---
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    knn_scaled = KNeighborsClassifier(n_neighbors=5)
    knn_scaled.fit(X_train_scaled, y_train)
    acc_scaled = accuracy_score(y_test, knn_scaled.predict(X_test_scaled))

    print("=== KNN (K=5) on Iris ===")
    print(f"Unscaled accuracy: {acc_unscaled:.4f}")
    print(f"Scaled accuracy:   {acc_scaled:.4f}")
    print()
    print("Key takeaway: KNN uses distance-based voting. Features with larger")
    print("scales dominate the distance computation. Scaling ensures all")
    print("features contribute equally, often improving accuracy.")
