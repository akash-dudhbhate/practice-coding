# Lesson 13 — Intuition Checks

## Check 01: SVM
How does SVM work?
<details><summary>Answer</summary>
Finds the hyperplane that maximizes the margin (distance to nearest points). Support vectors are the points closest to the boundary. Kernel trick maps data to higher dimensions for non-linear separation.
</details>

## Check 02: KNN
How does KNN work?
<details><summary>Answer</summary>
K-Nearest Neighbors — for a new point, find k nearest training points. Majority vote (classification) or average (regression). No training — just stores data. Lazy learner.
</details>

## Check 03: Kernels
```python
SVC(kernel="linear")  # A
SVC(kernel="rbf")     # B
SVC(kernel="poly")    # C
```
<details><summary>Answer</summary>
linear — straight line boundary. rbf — radial basis, handles non-linear (default, most versatile). poly — polynomial boundary. Start with rbf.
</details>

## Check 04: C parameter
```python
SVC(C=1.0)   # default
SVC(C=100)   # less regularization
SVC(C=0.01)  # more regularization
```
<details><summary>Answer</summary>
C = penalty for misclassification. Large C = strict (may overfit). Small C = tolerant (may underfit). Trade-off between smooth boundary and training accuracy.
</details>

## Check 05: KNN distance metrics
```python
KNeighborsClassifier(metric="euclidean")  # A
KNeighborsClassifier(metric="manhattan")  # B
```
<details><summary>Answer</summary>
Euclidean — straight line distance. Manhattan — grid distance (sum of absolute differences). Euclidean is default. Manhattan for grid-like data.
</details>
