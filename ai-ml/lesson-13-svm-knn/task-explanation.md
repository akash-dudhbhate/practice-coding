# Lesson 13 — SVM & KNN

## What you'll learn
- K-Nearest Neighbors (KNN) basics
- Choosing K (bias-variance tradeoff)
- Distance metrics (Euclidean, Manhattan, Cosine)
- Support Vector Machines (SVM) and margins
- SVM kernels (linear, RBF, polynomial)
- SVM parameters (C and gamma)
- SVM vs KNN vs other models
- Support vectors (the points that matter)

## Lesson

### KNN
```python
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_scaled, y_train)
```

### SVM
```python
from sklearn.svm import SVC
model = SVC(kernel='rbf', C=1.0, gamma='scale')
model.fit(X_scaled, y_train)
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Train KNN (K=5) on the Iris dataset (scaled). Print accuracy. Show that unscaled data gives worse results.
2. `easy/p02-solve.py` — Train SVM with linear kernel on a linearly separable dataset (`make_classification`). Print accuracy and the number of support vectors.
3. `easy/p03-solve.py` — Compare KNN with K=1, K=5, K=20 on the same dataset. Print train and test accuracy for each. Show that K=1 overfits (100% train, lower test).

### Medium
4. `medium/p01-solve.py` — Tune K for KNN: try K from 1 to 50 (odd values). Use 5-fold CV. Plot accuracy vs K. Identify the optimal K. Use scaled data.
5. `medium/p02-solve.py` — Compare SVM kernels (linear, RBF, poly) on a non-linear dataset (`make_circles` or `make_moons`). Print accuracy for each. Plot decision boundaries for all three.
6. `medium/p03-solve.py` — Grid search SVM parameters: C [0.1, 1, 10, 100] and gamma [0.001, 0.01, 0.1, 1]. Use RBF kernel. Print best params and best score. Use scaled data.

### Hard
7. `hard/p01-solve.py` — Build a model comparison: KNN, SVM (linear), SVM (RBF), Random Forest on the same dataset. For each: tune the key hyperparameter with CV, print best score, and create a comparison table. Identify the best model.
8. `hard/p02-solve.py` — Build a KNN from scratch: implement Euclidean distance, find K nearest neighbors, majority vote. Train on a 2D dataset. Plot the decision boundary. Compare with sklearn's KNN.
9. `hard/p03-solve.py` — Build an SVM from scratch using gradient descent (linear SVM with hinge loss). Implement the loss function and gradient. Train on a 2D dataset. Plot the decision boundary and margin. Compare with sklearn's SVC.

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
