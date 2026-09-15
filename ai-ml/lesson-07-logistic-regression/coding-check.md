# Lesson 07 — Coding Check

## Easy

### p01-solve.py — Sigmoid from scratch
- [ ] `sigmoid(z)` function defined
- [ ] sigmoid(0) → 0.5
- [ ] sigmoid(5) → ~0.993
- [ ] sigmoid(-5) → ~0.007
- [ ] All outputs between 0 and 1
- [ ] No sklearn used

### p02-solve.py — sklearn logistic regression
- [ ] `make_classification` used to create data
- [ ] `LogisticRegression` trained
- [ ] Accuracy printed
- [ ] Precision printed
- [ ] Recall printed
- [ ] F1-score printed

### p03-solve.py — Confusion matrix from scratch
- [ ] 2x2 matrix calculated manually
- [ ] TP, TN, FP, FN identified
- [ ] Result matches `sklearn.metrics.confusion_matrix`
- [ ] No sklearn used for the calculation

## Medium

### p01-solve.py — Spam classifier
- [ ] Synthetic email features created
- [ ] Logistic regression trained
- [ ] Confusion matrix printed
- [ ] Precision and recall printed
- [ ] Results interpreted (e.g., "high precision = few false alarms")

### p02-solve.py — Decision boundary plot
- [ ] 2D synthetic data created
- [ ] `meshgrid` used for the grid
- [ ] `contourf` used to plot boundary
- [ ] Data points overlaid with `scatter`
- [ ] Boundary is visible and separates classes

### p03-solve.py — Multiclass on Iris
- [ ] Iris dataset loaded (3 classes)
- [ ] Multinomial logistic regression trained
- [ ] Accuracy printed
- [ ] Confusion matrix printed (3x3)
- [ ] `classification_report` used for per-class metrics
- [ ] Per-class precision and recall shown

## Hard

### p01-solve.py — C parameter comparison
- [ ] Breast Cancer dataset loaded
- [ ] Features scaled
- [ ] C values: 0.01, 1, 100 tested
- [ ] For each C: precision, recall, F1 printed
- [ ] Effect of C plotted (line chart)
- [ ] Interpretation: high C = overfitting, low C = underfitting

### p02-solve.py — Logistic regression from scratch
- [ ] Sigmoid function implemented
- [ ] Log-loss cost function implemented
- [ ] Gradient descent implemented
- [ ] Trained on synthetic data
- [ ] Loss curve plotted (decreasing)
- [ ] Decision boundary plotted
- [ ] No sklearn used for the model

### p03-solve.py — Threshold optimization
- [ ] Logistic regression trained
- [ ] `predict_proba` used for probabilities
- [ ] Thresholds from 0.1 to 0.9 swept
- [ ] For each: precision, recall, F1 calculated
- [ ] Precision-recall curve plotted
- [ ] Optimal F1 threshold identified
- [ ] Results printed and interpreted
