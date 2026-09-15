# Lesson 02 — Common Mistakes

## Mistake 01: Preprocessing before split
```python
# WRONG — data leakage
scaler.fit_transform(X)
train_test_split(X)
# CORRECT
train_test_split(X)
scaler.fit(X_train)
scaler.transform(X_test)
```

## Mistake 02: Label encoding for nominal data
```python
# WRONG — implies order
LabelEncoder()  # red=0, blue=1, green=2
# CORRECT — no order implied
OneHotEncoder()  # separate columns
```

## Mistake 03: Dropping all NaN
```python
# WRONG — loses too much data
df.dropna()
# CORRECT — impute if possible
df.fillna(df.median())
```

## Mistake 04: Not fitting on train only
```python
# WRONG — test data influences preprocessing
scaler.fit(X_train)
scaler.fit(X_test)  # refits!
# CORRECT
scaler.fit(X_train)
scaler.transform(X_test)  # transform only
```

## Mistake 05: Ignoring outliers
```python
# Check for outliers before scaling
# MinMaxScaler is very sensitive to outliers
# Use RobustScaler or clip extreme values
```
