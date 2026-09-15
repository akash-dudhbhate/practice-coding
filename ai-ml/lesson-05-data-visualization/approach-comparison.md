# Lesson 05 — Approach Comparison

## Problem: Explore Data

### Approach 1: matplotlib
```python
plt.figure(figsize=(10, 6))
plt.scatter(df["x"], df["y"])
plt.xlabel("X")
```

### Approach 2: seaborn
```python
sns.scatterplot(data=df, x="x", y="y", hue="category")
```

**Winner:** Approach 2 — less code, better defaults, handles legends automatically.

---

## Problem: Multiple Plots

### Approach 1: Subplots
```python
fig, axes = plt.subplots(1, 2)
axes[0].hist(df["a"])
axes[1].hist(df["b"])
```

### Approach 2: seaborn pairplot
```python
sns.pairplot(df)
```

**Winner:** Approach 2 for quick EDA. Approach 1 for custom layouts.
