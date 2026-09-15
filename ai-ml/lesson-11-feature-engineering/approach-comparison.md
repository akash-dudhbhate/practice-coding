# Lesson 11 — Approach Comparison

## Problem: Encode Categories

### Approach 1: One-hot
```python
pd.get_dummies(df, columns=["color"])
```
**Pros:** No order implied. **Cons:** Many columns for high cardinality.

### Approach 2: Target encoding
```python
means = df.groupby("city")["target"].mean()
df["city_encoded"] = df["city"].map(means)
```

**Winner:** One-hot for <10 categories. Target encoding for high cardinality.

---

## Problem: Create Features

### Approach 1: Manual
```python
df["bmi"] = df["weight"] / df["height"] ** 2
```

### Approach 2: Automated (featuretools)
```python
import featuretools as ft
# Automatically generates features
```

**Winner:** Manual for domain-specific. Automated for exploration.
