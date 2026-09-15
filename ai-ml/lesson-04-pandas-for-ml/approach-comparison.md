# Lesson 04 — Approach Comparison

## Problem: Filter and Aggregate

### Approach 1: Multiple steps
```python
filtered = df[df["age"] > 18]
result = filtered.groupby("city")["income"].mean()
```

### Approach 2: Method chaining
```python
result = df.query("age > 18").groupby("city")["income"].mean()
```

**Winner:** Approach 2 — cleaner, no intermediate variables.

---

## Problem: Handle Missing Data

### Approach 1: Drop
```python
df.dropna()
```

### Approach 2: Fill
```python
df.fillna(df.median())
```

**Winner:** Drop if few NaN. Fill if many. Never ignore missing data.
