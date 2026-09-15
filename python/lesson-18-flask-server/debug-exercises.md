# Lesson 18 — Debug Exercises

## Debug 01 (Easy): SettingWithCopyWarning
```python
df[df["age"] > 18]["name"] = "adult"
```
<details><summary>Answer</summary>
**Bug:** Chained indexing — may modify a copy, not the original.
**Fix:** `df.loc[df["age"] > 18, "name"] = "adult"`.
</details>

## Debug 02 (Medium): Wrong Merge
```python
result = pd.merge(df1, df2)
```
<details><summary>Answer</summary>
**Bug:** No `on` parameter — pandas guesses the join column. May pick the wrong one.
**Fix:** `pd.merge(df1, df2, on="id")`.
</details>

## Debug 03 (Hard): Groupby Aggregation Error
```python
df.groupby("category").mean()["price"]
```
<details><summary>Answer</summary>
**Bug:** `.mean()` on non-numeric columns raises a warning/error in newer pandas.
**Fix:** `df.groupby("category")["price"].mean()` — select column first.
</details>
