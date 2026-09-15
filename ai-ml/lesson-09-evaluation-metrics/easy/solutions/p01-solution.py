"""
Implement Accuracy, Precision, Recall, F1 from Scratch
=====================================================
Implement all four classification metrics manually.
Test with y_true=[0,0,1,1,1], y_pred=[0,1,1,1,0].
Verify against sklearn.
"""

import numpy as np
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score)


def accuracy(y_true, y_pred):
    """Accuracy = (TP + TN) / total."""
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    return np.mean(y_true == y_pred)


def precision(y_true, y_pred):
    """Precision = TP / (TP + FP)."""
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    return tp / (tp + fp) if (tp + fp) > 0 else 0.0


def recall(y_true, y_pred):
    """Recall = TP / (TP + FN)."""
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    return tp / (tp + fn) if (tp + fn) > 0 else 0.0


def f1(y_true, y_pred):
    """F1 = 2 * (precision * recall) / (precision + recall)."""
    p = precision(y_true, y_pred)
    r = recall(y_true, y_pred)
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0


if __name__ == "__main__":
    y_true = [0, 0, 1, 1, 1]
    y_pred = [0, 1, 1, 1, 0]

    print("=== Metrics from Scratch ===\n")
    print(f"y_true: {y_true}")
    print(f"y_pred: {y_pred}\n")

    my_acc = accuracy(y_true, y_pred)
    my_prec = precision(y_true, y_pred)
    my_rec = recall(y_true, y_pred)
    my_f1 = f1(y_true, y_pred)

    sk_acc = accuracy_score(y_true, y_pred)
    sk_prec = precision_score(y_true, y_pred)
    sk_rec = recall_score(y_true, y_pred)
    sk_f1 = f1_score(y_true, y_pred)

    print(f"{'Metric':<12} {'From Scratch':<15} {'sklearn':<15} {'Match':<8}")
    print("-" * 50)
    print(f"{'Accuracy':<12} {my_acc:<15.4f} {sk_acc:<15.4f} {str(np.isclose(my_acc, sk_acc)):<8}")
    print(f"{'Precision':<12} {my_prec:<15.4f} {sk_prec:<15.4f} {str(np.isclose(my_prec, sk_prec)):<8}")
    print(f"{'Recall':<12} {my_rec:<15.4f} {sk_rec:<15.4f} {str(np.isclose(my_rec, sk_rec)):<8}")
    print(f"{'F1':<12} {my_f1:<15.4f} {sk_f1:<15.4f} {str(np.isclose(my_f1, sk_f1)):<8}")

    print("\n=== Interpretation ===")
    print(f"Accuracy:  {my_acc:.2%} of all predictions are correct.")
    print(f"Precision: {my_prec:.2%} of predicted positives are actually positive.")
    print(f"Recall:    {my_rec:.2%} of actual positives were correctly predicted.")
    print(f"F1:        Harmonic mean of precision and recall.")
