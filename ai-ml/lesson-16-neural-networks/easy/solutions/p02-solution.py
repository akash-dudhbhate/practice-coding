"""
Train sklearn MLPClassifier on Iris (scaled)
=============================================
Train a Multi-Layer Perceptron on the Iris dataset with feature scaling.
Print accuracy and compare with logistic regression.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


if __name__ == "__main__":
    # Load Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split into train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scale features — critical for MLP convergence (gradient descent sensitive to scale)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train MLPClassifier
    mlp = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=500, random_state=42)
    mlp.fit(X_train_scaled, y_train)
    mlp_pred = mlp.predict(X_test_scaled)
    mlp_acc = accuracy_score(y_test, mlp_pred)

    # Train Logistic Regression for comparison
    logreg = LogisticRegression(max_iter=500, random_state=42)
    logreg.fit(X_train_scaled, y_train)
    logreg_pred = logreg.predict(X_test_scaled)
    logreg_acc = accuracy_score(y_test, logreg_pred)

    # Print results
    print("--- MLPClassifier ---")
    print(f"Hidden layers: (16, 8)")
    print(f"Test accuracy: {mlp_acc:.4f}")

    print("\n--- Logistic Regression ---")
    print(f"Test accuracy: {logreg_acc:.4f}")

    print("\n--- Comparison ---")
    print(f"MLP accuracy:        {mlp_acc:.4f}")
    print(f"LogReg accuracy:     {logreg_acc:.4f}")
    print(f"Difference (MLP-LR): {mlp_acc - logreg_acc:+.4f}")
    if mlp_acc > logreg_acc:
        print("MLP outperforms Logistic Regression.")
    elif mlp_acc < logreg_acc:
        print("Logistic Regression outperforms MLP.")
    else:
        print("Both models perform equally.")
