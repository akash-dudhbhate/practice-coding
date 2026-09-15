"""
Fraud Detection Simulation
==========================
Simulate credit card transactions (amount, merchant, time, is_fraud).
Apply SMOTE, train a model, plot the PR curve, find the threshold for
80% recall, and report the precision at that threshold.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_score, recall_score, precision_recall_curve, average_precision_score
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline

np.random.seed(42)


if __name__ == "__main__":
    # --- Generate synthetic transactions ---
    n = 5000
    amount = np.random.exponential(scale=50, size=n)
    merchant = np.random.choice(["Amazon", "Walmart", "Target", "BestBuy", "Other"], n)
    hour = np.random.randint(0, 24, n)
    distance = np.random.exponential(scale=100, size=n)

    # Fraud is more likely: high amount, late night, far distance
    fraud_prob = 1 / (1 + np.exp(-(0.02 * amount + 0.3 * (hour < 6) + 0.005 * distance - 5)))
    is_fraud = (np.random.rand(n) < fraud_prob).astype(int)

    df = pd.DataFrame({
        "amount": amount, "merchant": merchant, "hour": hour,
        "distance": distance, "is_fraud": is_fraud,
    })

    print(f"Class distribution: {dict(zip(*np.unique(is_fraud, return_counts=True)))}")
    print(f"Fraud rate: {is_fraud.mean():.2%}\n")

    # Encode merchant
    le = LabelEncoder()
    df["merchant_enc"] = le.fit_transform(df["merchant"])

    X = df[["amount", "merchant_enc", "hour", "distance"]]
    y = df["is_fraud"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # --- Pipeline with SMOTE ---
    pipe = Pipeline([
        ("smote", SMOTE(random_state=42, k_neighbors=3)),
        ("clf", RandomForestClassifier(random_state=42, n_estimators=100)),
    ])
    pipe.fit(X_train, y_train)
    y_proba = pipe.predict_proba(X_test)[:, 1]

    # --- PR Curve ---
    precision, recall, thresholds = precision_recall_curve(y_test, y_proba)
    pr_auc = average_precision_score(y_test, y_proba)

    plt.figure(figsize=(8, 5))
    plt.plot(recall, precision, label=f"PR Curve (AP={pr_auc:.3f})")
    plt.axvline(x=0.80, color="r", linestyle="--", label="80% recall target")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision-Recall Curve — Fraud Detection")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("fraud_pr_curve.png", dpi=150)
    print("PR curve saved to fraud_pr_curve.png")

    # --- Find threshold for 80% recall ---
    # precision_recall_curve returns thresholds with len = len(precision) - 1
    # Find the threshold where recall >= 0.80
    target_recall = 0.80
    best_threshold = None
    best_precision = None
    for i in range(len(thresholds)):
        if recall[i] >= target_recall:
            best_threshold = thresholds[i]
            best_precision = precision[i]
            break

    if best_threshold is not None:
        print(f"\nThreshold for >= {target_recall:.0%} recall: {best_threshold:.4f}")
        print(f"Precision at that threshold: {best_precision:.4f}")

        # Verify with actual predictions
        y_pred_thresh = (y_proba >= best_threshold).astype(int)
        print(f"Actual recall:    {recall_score(y_test, y_pred_thresh):.4f}")
        print(f"Actual precision: {precision_score(y_test, y_pred_thresh, zero_division=0):.4f}")
    else:
        print("Could not achieve 80% recall at any threshold.")

    print(f"\nPR-AUC (average precision): {pr_auc:.4f}")
