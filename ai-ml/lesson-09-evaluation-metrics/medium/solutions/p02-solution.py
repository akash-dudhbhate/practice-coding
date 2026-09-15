"""
Plot ROC Curve and Calculate AUC
================================
Train logistic regression, plot the ROC curve, calculate AUC,
add a random baseline line, and interpret AUC=0.9.
"""

import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=1000, n_features=10, n_informative=5,
        n_redundant=2, random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    # Get probabilities
    y_proba = model.predict_proba(X_test)[:, 1]

    # Calculate ROC curve
    fpr, tpr, thresholds = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)

    print(f"ROC AUC: {roc_auc:.4f}")

    # Plot ROC curve
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color="darkorange", lw=2, label=f"ROC curve (AUC = {roc_auc:.4f})")
    plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--", label="Random baseline (AUC = 0.5)")
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Receiver Operating Characteristic (ROC) Curve")
    plt.legend(loc="lower right")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("roc_curve.png", dpi=150)
    plt.show()
    print("ROC curve saved to roc_curve.png")

    print("\n=== Interpretation ===")
    print(f"AUC = {roc_auc:.4f}")
    print("AUC = 0.5: random guessing (diagonal line).")
    print("AUC = 1.0: perfect classifier.")
    print("AUC = 0.9: excellent classifier; 90% chance a random positive is ranked above a random negative.")
    print("The closer the curve is to the top-left corner, the better the model.")
