# Level 04 — Concepts Reference

## Easy

### Linear Regression (closed form)
- `m = Σ((x-x̄)(y-ȳ)) / Σ((x-x̄)²)`; `b = ȳ - m·x̄`
- Finds the single best-fit line in one shot.

### Logistic Regression (from scratch)
- `sigmoid(z) = 1/(1+e^-z)` — squash to probability 0-1
- Train: gradient descent on w and b to minimize log-loss

### Decision Trees
- `DecisionTreeClassifier(max_depth=3)` — limits overfitting
- `plot_tree(tree, feature_names=..., filled=True)` — visualize

## Medium

### Gradient Descent
- Iterative: `w -= lr * gradient` until loss plateaus
- `MSE = mean((y - ŷ)²)`; gradients: `dm = -2·mean(x·(y-ŷ))`

### Random Forest
- Many trees trained on random data/feature subsets, vote together
- `rf.feature_importances_` — which features matter most (sums to 1)

### SVM vs KNN
- SVM: best-margin boundary. KNN: neighbor majority vote.
- Compare both — different biases, different results.

## Hard

### Regularization
- L1 (Lasso): `alpha·|w|` penalty → some coefs become exactly 0
- L2 (Ridge): `alpha·w²` penalty → all coefs shrink smoothly

### Ensembles
- Single tree overfits; forest averages it away; boosting corrects errors
- Compare train vs test gap to spot overfitting

### RFE (Feature Selection)
- `RFE(estimator, n_features_to_select=5)` — recursively drops weakest
- `rfe.support_` → boolean mask of kept features
