"""
Confusion Matrix from Scratch (2x2)
===================================
Implement a 2x2 confusion matrix manually: calculate TP, TN, FP, FN.
Verify against sklearn's confusion_matrix.
"""

import numpy as np
from sklearn.metrics import confusion_matrix


def confusion_matrix_from_scratch(y_true, y_pred):
    """Build a 2x2 confusion matrix from scratch.

    Returns (TP, TN, FP, FN) where positive class = 1.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    tp = np.sum((y_true == 1) & (y_pred == 1))
    tn = np.sum((y_true == 0) & (y_pred == 0))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))

    return tp, tn, fp, fn


if __name__ == "__main__":
    y_true = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0]
    y_pred = [0, 1, 1, 1, 0, 0, 1, 0, 1, 1]

    tp, tn, fp, fn = confusion_matrix_from_scratch(y_true, y_pred)

    print("=== Confusion Matrix from Scratch ===\n")
    print(f"{'':>15} {'Pred 0':>10} {'Pred 1':>10}")
    print(f"{'Actual 0':>15} {tn:>10} {fp:>10}")
    print(f"{'Actual 1':>15} {fn:>10} {tp:>10}")

    print(f"\nTP (True Positive):  {tp}")
    print(f"TN (True Negative):  {tn}")
    print(f"FP (False Positive): {fp}")
    print(f"FN (False Negative): {fn}")

    # Derived metrics
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    print(f"\nAccuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1 Score:  {f1:.4f}")

    # Verify against sklearn
    sk_cm = confusion_matrix(y_true, y_pred)
    print(f"\n=== sklearn Confusion Matrix ===")
    print(sk_cm)
    print(f"\nMatch: {np.array_equal(np.array([[tn, fp], [fn, tp]]), sk_cm)}")
