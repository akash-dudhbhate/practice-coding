"""
Lesson 01 - Hard P02
Calculate TP, FP, TN, FN and accuracy from a given scenario.

Scenario:
  A medical test for a disease produced the following results on 100 patients:
    - 40 patients actually have the disease.
    - 60 patients do not have the disease.
  The test predicted:
    - 35 of the sick patients as positive (correct).
    - 5  of the sick patients as negative (missed).
    - 50 of the healthy patients as negative (correct).
    - 10 of the healthy patients as positive (false alarm).

Solution:
  TP = 35, FP = 10, TN = 50, FN = 5
  Accuracy = (TP + TN) / Total = (35 + 50) / 100 = 0.85
"""

# ---------------------------------------------------------------------------
# Confusion matrix components
# ---------------------------------------------------------------------------
TP = 35  # True Positives:  sick and predicted positive
FP = 10  # False Positives: healthy but predicted positive
TN = 50  # True Negatives:  healthy and predicted negative
FN = 5   # False Negatives: sick but predicted negative

total = TP + FP + TN + FN

# ---------------------------------------------------------------------------
# Derived metrics
# ---------------------------------------------------------------------------
accuracy = (TP + TN) / total
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1_score = 2 * precision * recall / (precision + recall)

# ---------------------------------------------------------------------------
# Print results
# ---------------------------------------------------------------------------
print("Confusion Matrix Components")
print(f"  TP (True Positive)  = {TP}")
print(f"  FP (False Positive) = {FP}")
print(f"  TN (True Negative)  = {TN}")
print(f"  FN (False Negative) = {FN}")
print(f"  Total               = {total}")
print()

print("Derived Metrics")
print(f"  Accuracy  = (TP + TN) / Total = ({TP} + {TN}) / {total} = {accuracy:.4f}")
print(f"  Precision = TP / (TP + FP)    = {TP} / ({TP} + {FP})    = {precision:.4f}")
print(f"  Recall    = TP / (TP + FN)    = {TP} / ({TP} + {FN})    = {recall:.4f}")
print(f"  F1 Score  = 2 * P * R / (P + R) = {f1_score:.4f}")
print()

# ---------------------------------------------------------------------------
# Interpretation
# ---------------------------------------------------------------------------
print("Interpretation")
print(f"  The model correctly classified {accuracy:.1%} of all patients.")
print(f"  Of all predicted positives, {precision:.1%} were truly sick (precision).")
print(f"  Of all truly sick patients, {recall:.1%} were detected (recall).")
print(f"  The {FN} false negatives are the most dangerous errors in a medical test")
print(f"  because they represent sick patients who were missed.")
