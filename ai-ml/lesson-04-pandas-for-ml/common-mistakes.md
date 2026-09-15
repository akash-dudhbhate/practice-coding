# Lesson 04 — Common Mistakes

## Mistake 01: Chained indexing
```python
# WRONG
df[mask]["col"] = value
# CORRECT
df.loc[mask, "col"] = value
```

## Mistake 02: apply when vectorized works
```python
# SLOW
df["y"] = df["x"].apply(lambda x: x ** 2)
# FAST
df["y"] = df["x"] ** 2
```

## Mistake 03: Not specifying merge column
```python
# AMBIGUOUS
pd.merge(df1, df2)
# EXPLICIT
pd.merge(df1, df2, on="id", how="left")
```

## Mistake 04: Modifying while iterating
```python
# WRONG
for idx, row in df.iterrows():
    df.loc[idx, "x"] = row["y"] * 2
# CORRECT — vectorized
df["x"] = df["y"] * 2
```

## Mistake 05: Not handling NaN
```python
# NaN propagates through operations
df["total"] = df["a"] + df["b"]  # NaN if either is NaN
```
