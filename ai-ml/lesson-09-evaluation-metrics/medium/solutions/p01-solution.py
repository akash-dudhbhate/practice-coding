"""
Imbalanced Dataset: Accuracy vs Recall
======================================
Create a 95:5 imbalanced dataset, train a model, and show that
accuracy is high but recall for the minority class is low.
Print the classification report.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


if __name__ == "__main__":
    # Create imbalanced dataset: 95% class 0, 5% class 1
    X, y = make_classification(
        n_samples=2000, n_features=10, n_informative=5,
        n_redundant=2, weights=[0.95], flip_y=0.01,
        random_state=42
    )

    print(f"Class distribution: {dict(zip(*np.unique(y, return_counts=True)))}")
    print(f"Class 1 (minority): {np.mean(y == 1)*100:.1f}%\n")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("=== Classification Report (Imbalanced Data) ===\n")
    print(classification_report(y_test, y_pred, target_names=["Class 0 (majority)", "Class 1 (minority)"]))

    print("Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    print(f"  {'':>22} {'Pred 0':>10} {'Pred 1':>10}")
    print(f"  {'Actual 0':>22} {cm[0, 0]:>10} {cm[0, 1]:>10}")
    print(f"  {'Actual 1':>22} {cm[1, 0]:>10} {cm[1, 1]:>10}")

    print("\n=== Key Insight ===")
    acc = (cm[0, 0] + cm[1, 1]) / cm.sum()
    recall_minority = cm[1, 1] / (cm[1, 0] + cm[1, 1]) if (cm[1, 0] + cm[1, 1]) > 0 else 0
    print(f"Overall accuracy: {acc:.4f} (looks good!)")
    print(f"Recall for minority class: {recall_minority:.4f} (often poor!)")
    print("\nAccuracy is misleading on imbalanced data.")
    print("A model that always predicts class 0 gets 95% accuracy but 0% recall for class 1.")
    print("Always look at per-class metrics (precision, recall, F1) for imbalanced datasets.")
