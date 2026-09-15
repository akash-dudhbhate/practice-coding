# Lesson 09 — Debug Exercises

## Debug 01 (Easy: Only Accuracy
```python
# 99% class 0, 1% class 1
model.score(X_test, y_test)  # 99% accuracy!
```
<details><summary>Answer</summary>
**Bug:** 99% accuracy on imbalanced data is meaningless — model just predicts majority class.
**Fix:** Use precision, recall, F1, or balanced accuracy.
</details>

## Debug 02 (Medium: Confusion Matrix Wrong
```python
cm = confusion_matrix(y_pred, y_test)  # arguments swapped
```
<details><summary>Answer</summary>
**Bug:** Arguments in wrong order. sklearn expects (y_true, y_pred).
**Fix:** `confusion_matrix(y_test, y_pred)`.
</details>

## Debug 03 (Hard: Threshold Not Considered
```python
# Model has 90% recall, 50% precision
# Is this good?
```
<details><summary>Answer</summary>
Depends on use case. High recall, low precision = many false positives. Good for: cancer screening (don't miss any). Bad for: spam filter (too many false alarms).
</details>
