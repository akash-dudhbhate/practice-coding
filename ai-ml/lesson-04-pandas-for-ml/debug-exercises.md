# Lesson 04 — Debug Exercises

## Debug 01 (Easy: SettingWithCopyWarning
```python
df[df["age"] > 18]["name"] = "adult"
```
<details><summary>Answer</summary>
**Bug:** Chained indexing — may modify a copy, not original.
**Fix:** `df.loc[df["age"] > 18, "name"] = "adult"`.
</details>

## Debug 02 (Medium: Merge on Wrong Column
```python
pd.merge(df1, df2)  # no "on" specified
```
<details><summary>Answer</summary>
**Bug:** Pandas guesses the join column. May pick wrong one.
**Fix:** `pd.merge(df1, df2, on="id")`.
</details>

## Debug 03 (Hard: Groupby Mean on Non-Numeric
```python
df.groupby("category").mean()
```
<details><summary>Answer</summary>
**Bug:** In newer pandas, mean on non-numeric columns raises error.
**Fix:** `df.groupby("category")["numeric_col"].mean()` — select numeric first.
</details>
