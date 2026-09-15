# Lesson 05 — Common Mistakes

## Mistake 01: Wrong chart type
```python
# WRONG — line for categories
plt.plot(categories, values)
# CORRECT — bar for categories
plt.bar(categories, values)
```

## Mistake 02: No labels
```python
# WRONG — no context
plt.plot(x, y)
# CORRECT
plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Sales")
plt.title("Sales Over Time")
```

## Mistake 03: Too many colors
```python
# WRONG — rainbow palette
# CORRECT — use consistent, meaningful colors
```

## Mistake 04: 3D charts
```python
# AVOID — hard to read, misleading
# Use 2D with color/size for extra dimensions
```

## Mistake 05: Not saving figure
```python
plt.savefig("chart.png", dpi=150, bbox_inches="tight")
```
