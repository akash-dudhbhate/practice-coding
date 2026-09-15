# Lesson 11 — Debug Exercises

## Debug 01 (Easy: Creating Feature After Split
```python
X_train, X_test = train_test_split(df)
X_train["ratio"] = X_train["a"] / X_train["b"]
X_test["ratio"] = X_test["a"] / X_test["b"]
```
<details><summary>Answer</summary>
OK in this case (ratio is deterministic). But if feature uses aggregation (mean), must compute on train only.
</details>

## Debug 02 (Medium: Target Leakage
```python
df["target_mean"] = df.groupby("city")["target"].transform("mean")
X = df.drop("target", axis=1)
model.fit(X, df["target"])
```
<details><summary>Answer</summary>
**Bug:** Feature uses target — leakage. Model sees the answer during training.
**Fix:** Compute target encoding on train only, or use cross-validated encoding.
</details>

## Debug 03 (Hard: Too Many Features
```python
# 100 samples, 50 features after engineering
model.fit(X, y)  # overfits
```
<details><summary>Answer</summary>
**Bug:** More features than samples/n → overfitting (curse of dimensionality).
**Fix:** Feature selection (SelectKBest, Lasso) or dimensionality reduction (PCA).
</details>
