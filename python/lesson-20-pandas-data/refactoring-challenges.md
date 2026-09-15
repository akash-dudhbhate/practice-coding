# Lesson 20 — Refactoring Challenges

## Refactor 01 (Easy): Iterrows for Transformation
### Before
```python
for idx, row in df.iterrows():
    df.loc[idx, "double"] = row["value"] * 2
```
### After
```python
df["double"] = df["value"] * 2
```

## Refactor 02 (Medium): Chained Indexing
### Before
```python
df[df["age"] > 18]["category"] = "adult"
```
### After
```python
df.loc[df["age"] > 18, "category"] = "adult"
```

## Refactor 03 (Hard): Multiple Intermediate Variables
### Before
```python
filtered = df[df["age"] > 18]
filtered = filtered[filtered["income"] > 50000]
filtered["tax"] = filtered["income"] * 0.2
result = filtered.groupby("city")["tax"].mean()
```
### After
```python
result = (df
    .query("age > 18 and income > 50000")
    .assign(tax=lambda x: x["income"] * 0.2)
    .groupby("city")["tax"]
    .mean()
)
```
