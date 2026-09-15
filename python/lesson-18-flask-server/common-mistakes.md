# Lesson 18 — Common Mistakes

## Mistake 01: Chained indexing
```python
# WRONG — SettingWithCopyWarning
df[df["x"] > 0]["y"] = 1

# CORRECT
df.loc[df["x"] > 0, "y"] = 1
```

## Mistake 02: Using apply when vectorized works
```python
# SLOW
df["y"] = df["x"].apply(lambda x: x ** 2)

# FAST
df["y"] = df["x"] ** 2
```

## Mistake 03: Not handling NaN
```python
# WRONG — NaN propagates
df["total"] = df["a"] + df["b"]  # NaN if either is NaN

# CORRECT — fill or skip
df["total"] = df["a"].fillna(0) + df["b"].fillna(0)
```

## Mistake 04: Modifying while iterating
```python
# WRONG — unpredictable
for idx, row in df.iterrows():
    df.loc[idx, "x"] = row["y"] * 2

# CORRECT — vectorized
df["x"] = df["y"] * 2
```

## Mistake 05: Not specifying merge column
```python
# AMBIGUOUS
pd.merge(df1, df2)

# EXPLICIT
pd.merge(df1, df2, on="id", how="left")
```
