# Lesson 04 — Refactoring Challenges

## Refactor 01 (Easy): Iterrows
### Before
```python
for idx, row in df.iterrows():
    df.loc[idx, "total"] = row["a"] + row["b"]
```
### After
```python
df["total"] = df["a"] + df["b"]
```

## Refactor 02 (Medium): Chained Indexing
### Before
```python
df[df["age"] > 18]["status"] = "adult"  # SettingWithCopyWarning
```
### After
```python
df.loc[df["age"] > 18, "status"] = "adult"
```

## Refactor 03 (Hard): Multiple Intermediate DataFrames
### Before
```python
df1 = df[df["x"] > 0]
df2 = df1.groupby("cat")["val"].mean().reset_index()
df3 = df2.sort_values("val", ascending=False)
```
### After
```python
result = (df.query("x > 0")
  .groupby("cat")["val"].mean()
  .reset_index()
  .sort_values("val", ascending=False))
```
