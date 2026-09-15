"""
Spam Classifier with Logistic Regression
========================================
Create synthetic email features (word counts, links, caps ratio).
Train logistic regression to classify spam vs not-spam.
Print confusion matrix, precision, and recall.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (confusion_matrix, precision_score,
                             recall_score, f1_score, accuracy_score)


def generate_email_data(n=1000, seed=42):
    """Generate synthetic email features for spam classification.

    Features:
      - suspicious_words: count of suspicious keywords
      - num_links: number of links in email
      - caps_ratio: ratio of uppercase characters
    """
    rng = np.random.RandomState(seed)
    n_spam = n // 5  # 20% spam

    # Spam emails: higher word counts, links, caps
    spam_words = rng.poisson(8, n_spam)
    spam_links = rng.poisson(5, n_spam)
    spam_caps = rng.uniform(0.3, 0.8, n_spam)

    # Not-spam emails: lower values
    ham_words = rng.poisson(2, n - n_spam)
    ham_links = rng.poisson(1, n - n_spam)
    ham_caps = rng.uniform(0.0, 0.2, n - n_spam)

    X = np.column_stack([
        np.concatenate([spam_words, ham_words]),
        np.concatenate([spam_links, ham_links]),
        np.concatenate([spam_caps, ham_caps]),
    ])
    y = np.concatenate([np.ones(n_spam), np.zeros(n - n_spam)])

    # Shuffle
    idx = rng.permutation(n)
    return X[idx], y[idx]


if __name__ == "__main__":
    X, y = generate_email_data()
    feature_names = ["Suspicious Words", "Num Links", "Caps Ratio"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    cm = confusion_matrix(y_test, y_pred)
    print("=== Spam Classifier Results ===\n")
    print("Confusion Matrix:")
    print(f"  {'':>15} {'Pred Not Spam':>15} {'Pred Spam':>10}")
    print(f"  {'Actual Not Spam':>15} {cm[0, 0]:>15} {cm[0, 1]:>10}")
    print(f"  {'Actual Spam':>15} {cm[1, 0]:>15} {cm[1, 1]:>10}")

    print(f"\nAccuracy:  {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall:    {recall_score(y_test, y_pred):.4f}")
    print(f"F1 Score:  {f1_score(y_test, y_pred):.4f}")

    print("\nFeature Coefficients:")
    for name, coef in zip(feature_names, model.coef_[0]):
        print(f"  {name:20s}: {coef:+.4f}")

    print("\n=== Interpretation ===")
    print("Positive coefficients increase spam probability.")
    print("Higher suspicious word count and more links strongly predict spam.")
