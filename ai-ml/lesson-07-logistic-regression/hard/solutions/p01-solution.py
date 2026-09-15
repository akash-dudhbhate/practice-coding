"""
Binary Classification Pipeline: Breast Cancer
=============================================
Load the Breast Cancer dataset, scale features, train logistic regression
with different C values [0.01, 1, 100], and compare precision/recall/F1.
Plot the effect of C on the metrics.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score


if __name__ == "__main__":
    data = load_breast_cancer()
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    C_values = [0.01, 1, 100]
    results = {"C": [], "accuracy": [], "precision": [], "recall": [], "f1": []}

    print("=== Effect of C on Logistic Regression ===\n")
    print(f"{'C':<8} {'Accuracy':<12} {'Precision':<12} {'Recall':<12} {'F1':<12}")
    print("-" * 56)

    for C in C_values:
        model = LogisticRegression(C=C, max_iter=1000, random_state=42)
        model.fit(X_train_s, y_train)
        y_pred = model.predict(X_test_s)

        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        results["C"].append(C)
        results["accuracy"].append(acc)
        results["precision"].append(prec)
        results["recall"].append(rec)
        results["f1"].append(f1)

        print(f"{C:<8} {acc:<12.4f} {prec:<12.4f} {rec:<12.4f} {f1:<12.4f}")

    # Plot effect of C
    plt.figure(figsize=(8, 5))
    x_pos = range(len(C_values))
    plt.plot(x_pos, results["accuracy"], "o-", label="Accuracy")
    plt.plot(x_pos, results["precision"], "s-", label="Precision")
    plt.plot(x_pos, results["recall"], "^-", label="Recall")
    plt.plot(x_pos, results["f1"], "D-", label="F1")
    plt.xticks(x_pos, [str(c) for c in C_values])
    plt.xlabel("C (regularization strength)")
    plt.ylabel("Score")
    plt.title("Effect of C on Classification Metrics")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("effect_of_C.png", dpi=150)
    plt.show()
    print("\nPlot saved to effect_of_C.png")

    print("\n=== Interpretation ===")
    print("Small C = strong regularization (simpler model, may underfit).")
    print("Large C = weak regularization (complex model, may overfit).")
    print("C=1 often provides a good balance.")
