# Lesson 18 — Approach Comparison

## Problem: Filter and Transform

### Approach 1: Multiple steps
```python
filtered = df[df["age"] > 18]
filtered["category"] = filtered["age"].apply(classify)
result = filtered.groupby("category").mean()
```

### Approach 2: Method chaining
```python
result = (df
    .query("age > 18")
    .assign(category=lambda x: x["age"].apply(classify))
    .groupby("category")
    .mean()
)
```

**Winner:** Approach 2 — chaining is more readable, no intermediate variables.

---

## Problem: Handle Missing Data

### Approach 1: Drop
```python
df = df.dropna()
```
**Cons:** Loses data. Bad if many rows have some NaN.

### Approach 2: Fill
```python
df = df.fillna(df.mean())
```
**Pros:** Keeps all rows. **Cons:** May introduce bias.

### Approach 3: Impute (sklearn)
```python
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="median")
df[["age"]] = imputer.fit_transform(df[["age"]])
```

**Winner:** Depends on data. Drop if few NaN. Fill/impute if many.
