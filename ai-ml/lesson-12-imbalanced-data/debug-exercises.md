# Lesson 12 — Debug Exercises

## Debug 01 (Easy: Only Accuracy
```python
# 99% class 0, 1% class 1
model.score(X_test, y_test)  # 99% — looks great!
```
<details><summary>Answer</summary>
**Bug:** 99% accuracy is achieved by always predicting class 0. Useless.
**Fix:** Use F1, precision, recall, or balanced accuracy.
</details>

## Debug 02 (Medium: Oversampling Before Split
```python
X_resampled, y_resampled = oversample(X, y)
X_train, X_test = train_test_split(X_resampled)
```
<details><summary>Answer</summary>
**Bug:** Oversampling before split — duplicates can be in both train and test. Overfitting.
**Fix:** Split first, oversample train only.
</details>

## Debug 03 (Hard: Wrong Resampling Strategy
```python
# 1% positive class
oversampler = RandomOverSampler()
# Creates 99% copies of positive — overfits
```
<details><summary>Answer</summary>
**Bug:** Random oversampling duplicates minority — model memorizes them.
**Fix:** Use SMOTE (synthetic samples) or undersample majority.
</details>
