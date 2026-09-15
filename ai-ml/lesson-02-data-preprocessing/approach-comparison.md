# Lesson 02 — Approach Comparison

## Problem: Handle Missing Data

### Approach 1: Drop
```python
df.dropna()
```
**Cons:** Loses data.

### Approach 2: Fill with mean/median
```python
df.fillna(df.median())
```

### Approach 3: Predict missing values
```python
# Use other features to predict missing ones
```

**Winner:** Approach 2 for most cases. Approach 3 for important features.

---

## Problem: Encode Categories

### Approach 1: Label encoding
```python
# red=0, blue=1, green=2
```
**Cons:** Implies order where none exists.

### Approach 2: One-hot encoding
```python
pd.get_dummies(df, columns=["color"])
```

**Winner:** Approach 2 — no false ordering. Use for nominal categories.
