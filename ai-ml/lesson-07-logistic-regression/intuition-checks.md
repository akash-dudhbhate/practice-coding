# Lesson 07 — Intuition Checks

## Check 01: Logistic regression output
```python
model.predict_proba(X_test)  # [[0.3, 0.7], ...]
```
<details><summary>Answer</summary>
Returns probabilities for each class. `predict()` uses 0.5 threshold by default. `predict_proba()[:, 1]` gives probability of positive class.
</details>

## Check 02: Sigmoid
What does the sigmoid function do?
<details><summary>Answer</summary>
Squashes any value to 0-1 range: σ(x) = 1/(1+e^(-x)). Converts linear output to probability. At x=0, σ=0.5 (decision boundary).
</details>

## Check 03: Decision boundary
```python
model.predict(X_test)  # threshold at 0.5
```
<details><summary>Answer</summary>
Default threshold is 0.5. Can adjust: if prob > 0.3 → positive (more sensitive). If prob > 0.7 → positive (more specific). Trade-off between precision and recall.
</details>

## Check 04: Multiclass
```python
model = LogisticRegression(multi_class="multinomial")
```
<details><summary>Answer</summary>
Logistic regression is binary by default. For multiclass: "ovr" (one-vs-rest) or "multinomial" (softmax). Multinomial is usually better.
</details>

## Check 05: Regularization
```python
LogisticRegression(C=1.0)  # default
LogisticRegression(C=0.1)  # more regularization
```
<details><summary>Answer</summary>
C is inverse of regularization strength. Small C = strong regularization (simpler model, less overfitting). Large C = weak regularization (may overfit).
</details>
