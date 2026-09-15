# Lesson 08 — Coding Check

## Easy

### p01-solve.py — Decision tree on Iris
- [ ] Iris dataset loaded
- [ ] `DecisionTreeClassifier` with `max_depth=3`
- [ ] Train/test split used
- [ ] Accuracy printed
- [ ] `plot_tree` used to visualize

### p02-solve.py — Gini from scratch
- [ ] Gini function implemented: 1 - sum(p²)
- [ ] Tested with [3, 2] → 0.48
- [ ] Tested with [5, 0] → 0.0 (pure)
- [ ] Tested with [2, 2] → 0.5 (max impurity)
- [ ] No sklearn used

### p03-solve.py — Overfitting demo
- [ ] Tree without max_depth trained
- [ ] Tree with max_depth=3 trained
- [ ] Training accuracy compared (unlimited = 100%)
- [ ] Test accuracy compared (limited is better)
- [ ] Overfitting demonstrated

## Medium

### p01-solve.py — Random forest + feature importance
- [ ] `make_classification` with 1000 samples, 20 features
- [ ] `RandomForestClassifier` trained
- [ ] Accuracy printed
- [ ] `feature_importances_` extracted
- [ ] Importances plotted (bar chart)
- [ ] Top 5 features identified

### p02-solve.py — Tree vs forest comparison
- [ ] Same dataset for both models
- [ ] Decision tree: train and test accuracy
- [ ] Random forest: train and test accuracy
- [ ] Random forest has better test accuracy
- [ ] Random forest has less overfitting (smaller train-test gap)
- [ ] Results printed in a comparison table

### p03-solve.py — Tune max_depth
- [ ] Depths: 1, 3, 5, 10, 20, None tested
- [ ] Train accuracy recorded for each
- [ ] Test accuracy recorded for each
- [ ] Both curves plotted on same graph
- [ ] Optimal depth identified
- [ ] Overfitting visible at high depths

## Hard

### p01-solve.py — Model comparison pipeline
- [ ] Breast Cancer dataset loaded
- [ ] Decision tree trained and evaluated
- [ ] Random forest trained and evaluated
- [ ] Gradient boosting trained and evaluated
- [ ] For each: accuracy, precision, recall, F1
- [ ] Comparison table created (printed or DataFrame)
- [ ] Best model identified

### p02-solve.py — Decision tree from scratch
- [ ] Gini impurity implemented
- [ ] Best split function implemented
- [ ] Recursive tree building implemented
- [ ] `predict` method implemented
- [ ] Trained on 2D dataset
- [ ] Decision boundary plotted
- [ ] No sklearn used for the tree

### p03-solve.py — Feature selection with importance
- [ ] Random forest trained on all features
- [ ] Feature importances extracted
- [ ] Top 5 features selected
- [ ] New model trained with only top 5
- [ ] Accuracy compared (all vs top 5)
- [ ] Documented: did accuracy drop? was it worth it?
- [ ] Trade-off analyzed (accuracy vs simplicity)
