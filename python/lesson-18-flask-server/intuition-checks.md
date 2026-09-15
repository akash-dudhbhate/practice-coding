# Lesson 18 — Intuition Checks

## Check 01: DataFrame vs Series
```python
df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
print(type(df["a"]))
print(type(df[["a"]]))
```
<details><summary>Answer</summary>
`<class 'pandas.core.series.Series'>`, `<class 'pandas.core.frame.DataFrame'>` — single bracket = Series, double bracket = DataFrame.
</details>

## Check 02: loc vs iloc
```python
df = pd.DataFrame({"x": [10, 20, 30]}, index=["a", "b", "c"])
print(df.loc["b"])
print(df.iloc[1])
```
<details><summary>Answer</summary>
Both return the row with x=20. `loc` uses LABELS, `iloc` uses POSITIONS.
</details>

## Check 03: Missing Values
```python
df = pd.DataFrame({"a": [1, None, 3]})
print(df["a"].isna().sum())
```
<details><summary>Answer</summary>
`1` — one missing value. `isna()` returns boolean mask, `.sum()` counts True values.
</details>

## Check 04: groupby
```python
df = pd.DataFrame({"cat": ["a", "a", "b"], "val": [1, 2, 3]})
print(df.groupby("cat")["val"].sum())
```
<details><summary>Answer</summary>
```
cat
a    3
b    3
```
Groups by "cat" and sums "val" within each group.
</details>

## Check 05: apply vs vectorized
```python
# Which is faster?
df["x"].apply(lambda x: x * 2)  # A
df["x"] * 2                     # B
```
<details><summary>Answer</summary>
**B** — vectorized operations are 100-1000x faster than `apply`. Avoid `apply` when a vectorized operation exists.
</details>
