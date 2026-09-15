# Lesson 06 — Coding Check

## Easy

### p01-solve.py — Linear regression from scratch
- [ ] Slope (m) calculated using formula
- [ ] Intercept (b) calculated using formula
- [ ] Works with a small dataset (5+ points)
- [ ] Predictions match the line equation
- [ ] No sklearn used (pure numpy)

### p02-solve.py — sklearn linear regression
- [ ] `make_regression` used to create dataset
- [ ] `LinearRegression` fitted
- [ ] Coefficient printed
- [ ] Intercept printed
- [ ] R² score printed

### p03-solve.py — MSE from scratch
- [ ] MSE formula implemented: (1/n) * sum((y_true - y_pred)²)
- [ ] Works with any two arrays
- [ ] Result matches `sklearn.metrics.mean_squared_error`
- [ ] No sklearn used for the calculation

## Medium

### p01-solve.py — House price predictor
- [ ] Synthetic dataset with 3 features (size, bedrooms, age)
- [ ] Prices generated with a known relationship
- [ ] Multiple linear regression trained
- [ ] All 3 coefficients printed
- [ ] Intercept printed
- [ ] Interpretation: "each sq ft adds $X"

### p02-solve.py — Gradient descent
- [ ] m and b initialized to 0
- [ ] Learning rate set (e.g., 0.01)
- [ ] Gradients calculated correctly
- [ ] 1000 iterations run
- [ ] MSE tracked and decreasing
- [ ] Loss curve plotted

### p03-solve.py — Simple vs multiple regression
- [ ] Same dataset used for both
- [ ] Simple regression with 1 feature
- [ ] Multiple regression with 3 features
- [ ] R² compared for both
- [ ] MSE compared for both
- [ ] Documentation: which is better and why

## Hard

### p01-solve.py — Complete regression pipeline
- [ ] California Housing dataset loaded
- [ ] Features scaled (StandardScaler)
- [ ] Train/test split (80/20)
- [ ] Model trained
- [ ] MSE and R² on test set
- [ ] Actual vs predicted plot
- [ ] Pipeline is reproducible (random_state)

### p02-solve.py — Polynomial regression
- [ ] Non-linear dataset created (e.g., y = x² + noise)
- [ ] Linear fit attempted (poor fit)
- [ ] Polynomial features added (degree 2, 3)
- [ ] Both fits plotted on same graph
- [ ] R² compared for each degree
- [ ] Overfitting identified at high degree

### p03-solve.py — Assumption checking
- [ ] Linear regression fitted
- [ ] Linearity: scatter plot of X vs y
- [ ] Homoscedasticity: residual plot (predictions vs residuals)
- [ ] Normality: histogram of residuals
- [ ] Each assumption evaluated (holds/violated)
- [ ] Summary report generated
