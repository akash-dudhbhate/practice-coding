# Lesson 13 — Debug Exercises

## Debug 01 (Easy: Not Scaling for SVM
```python
model = SVC()
model.fit(X_train, y_train)  # features not scaled
```
<details><summary>Answer</summary>
**Bug:** SVM is distance-based — unscaled features distort distances.
**Fix:** Scale features: `StandardScaler().fit_transform(X_train)`.
</details>

## Debug 02 (Medium: KNN with k=1
```python
model = KNeighborsClassifier(n_neighbors=1)
```
<details><summary>Answer</summary>
**Bug:** k=1 overfits — sensitive to noise. One outlier changes prediction.
**Fix:** Use k=5 or 7. Use GridSearchCV to find optimal k.
</details>

## Debug 03 (Hard: Wrong Kernel
```python
model = SVC(kernel="linear")
# Data is not linearly separable
```
<details><summary>Answer</summary>
**Bug:** Linear kernel can't separate non-linear data.
**Fix:** Try `kernel="rbf"` (default) or `kernel="poly"`.
</details>
