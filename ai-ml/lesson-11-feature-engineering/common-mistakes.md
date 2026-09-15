# Lesson 11 — Common Mistakes

## Mistake 01: Target leakage
```python
# WRONG — feature uses target
df["mean_target"] = df.groupby("x")["target"].transform("mean")
# CORRECT — compute on train, apply to test
```

## Mistake 02: Too many features
```python
# WRONG — more features than samples
# Use feature selection or PCA
```

## Mistake 03: Not using domain knowledge
```python
# WRONG — only use raw columns
# CORRECT — create meaningful features
# e.g., BMI = weight / height^2
```

## Mistake 04: One-hot encoding high cardinality
```python
# WRONG — 1000 columns for 1000 categories
pd.get_dummies(df["city"])  # too many columns
# CORRECT — target or frequency encoding
```

## Mistake 05: Not checking feature importance
```python
# After engineering, check which features matter
model.feature_importances_
# Remove useless features
```
