# Lesson 05 — Refactoring Challenges

## Refactor 01 (Easy): Default Plot
### Before
```python
plt.plot(x, y)
plt.show()
```
### After
```python
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Data")
plt.xlabel("X"); plt.ylabel("Y"); plt.title("My Plot")
plt.legend(); plt.show()
```

## Refactor 02 (Medium): Repeated Plot Code
### Before
```python
plt.subplot(1, 3, 1); plt.hist(a); plt.title("A")
plt.subplot(1, 3, 2); plt.hist(b); plt.title("B")
plt.subplot(1, 3, 3); plt.hist(c); plt.title("C")
```
### After
```python
fig, axes = plt.subplots(1, 3)
for ax, (data, title) in zip(axes, [(a, "A"), (b, "B"), (c, "C")]):
    ax.hist(data); ax.set_title(title)
```

## Refactor 03 (Hard): Matplotlib for Stats
### Before
```python
plt.hist(data, bins=20)
```
### After
```python
import seaborn as sns
sns.histplot(data, bins=20, kde=True)  # adds KDE curve automatically
```
