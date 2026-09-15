# Lesson 04 — Intuition Checks

## Check 01: Series vs DataFrame
```python
df["col"]      # Series
df[["col"]]    # DataFrame
```
<details><summary>Answer</summary>
Single bracket = Series (1D). Double bracket = DataFrame (2D). Many bugs come from this confusion.
</details>

## Check 02: loc vs iloc
```python
df.loc[0]    # label-based
df.iloc[0]   # position-based
```
<details><summary>Answer</summary>
loc uses index LABELS (could be strings, non-sequential). iloc uses POSITIONS (always 0-based). When index is default (0,1,2...), they're similar.
</details>

## Check 03: groupby
```python
df.groupby("city")["population"].sum()
```
<details><summary>Answer</summary>
Groups rows by city, sums population within each group. Returns Series indexed by city.
</details>

## Check 04: merge types
```python
pd.merge(a, b, how="inner")  # A
pd.merge(a, b, how="left")   # B
pd.merge(a, b, how="outer")  # C
```
<details><summary>Answer</summary>
inner — only matching keys. left — all from a, matching from b. outer — all from both. Like SQL joins.
</details>

## Check 05: apply vs vectorized
```python
df["x"].apply(lambda x: x * 2)  # A
df["x"] * 2                     # B
```
<details><summary>Answer</summary>
B is 100x faster — vectorized. Avoid apply when vectorized operation exists.
</details>
