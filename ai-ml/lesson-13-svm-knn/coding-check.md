# Lesson 13 — Coding Check

## Easy

### p01-solve.py — KNN on Iris
- [ ] Iris dataset loaded
- [ ] Data scaled with StandardScaler
- [ ] KNN with K=5 trained
- [ ] Accuracy printed (scaled)
- [ ] Accuracy printed (unscaled, lower)
- [ ] Scaling makes a difference

### p02-solve.py — SVM linear
- [ ] Linearly separable dataset created
- [ ] `SVC(kernel='linear')` trained
- [ ] Accuracy printed
- [ ] `n_support_` printed (number of support vectors)
- [ ] Data scaled

### p03-solve.py — K comparison
- [ ] K=1, K=5, K=20 tested
- [ ] Train accuracy printed for each
- [ ] Test accuracy printed for each
- [ ] K=1: train=100%, test lower (overfitting)
- [ ] K=20: train < 100%, test similar (less overfitting)
- [ ] Trade-off demonstrated

## Medium

### p01-solve.py — Tune K
- [ ] K values 1 to 50 (odd) tested
- [ ] 5-fold CV used
- [ ] Accuracy recorded for each K
- [ ] Accuracy vs K plotted
- [ ] Optimal K identified
- [ ] Data scaled

### p02-solve.py — SVM kernels
- [ ] Non-linear dataset created (make_moons or make_circles)
- [ ] Linear kernel tested
- [ ] RBF kernel tested
- [ ] Poly kernel tested
- [ ] Accuracy printed for each
- [ ] Decision boundaries plotted for all three
- [ ] RBF/poly perform better on non-linear data

### p03-solve.py — SVM grid search
- [ ] C [0.1, 1, 10, 100] in grid
- [ ] gamma [0.001, 0.01, 0.1, 1] in grid
- [ ] RBF kernel used
- [ ] `GridSearchCV` with cv=5
- [ ] Best params printed
- [ ] Best score printed
- [ ] Data scaled

## Hard

### p01-solve.py — Model comparison
- [ ] KNN tuned (optimal K)
- [ ] SVM linear tuned (optimal C)
- [ ] SVM RBF tuned (optimal C, gamma)
- [ ] Random Forest tuned (n_estimators, max_depth)
- [ ] Best score for each printed
- [ ] Comparison table created
- [ ] Best model identified
- [ ] All models use scaled data (except RF)

### p02-solve.py — KNN from scratch
- [ ] Euclidean distance implemented
- [ ] K nearest neighbors found
- [ ] Majority vote implemented
- [ ] `predict` method works
- [ ] Trained on 2D dataset
- [ ] Decision boundary plotted
- [ ] Results match sklearn's KNN
- [ ] No sklearn used for KNN

### p03-solve.py — SVM from scratch
- [ ] Hinge loss implemented
- [ ] Gradient of hinge loss implemented
- [ ] Gradient descent training loop
- [ ] Weights and bias learned
- [ ] `predict` method works
- [ ] Decision boundary plotted
- [ ] Margin visualized
- [ ] Results compared with sklearn's SVC
