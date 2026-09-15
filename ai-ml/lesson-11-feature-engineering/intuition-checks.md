# Lesson 11 — Intuition Checks

## Check 01: Why feature engineering?
<details><summary>Answer</summary>
Models can only learn from patterns in features. Better features = better models, regardless of algorithm. "Better data beats fancier algorithms."
</details>

## Check 02: Interaction features
```python
df["area_per_room"] = df["area"] / df["rooms"]
```
<details><summary>Answer</summary>
Combines two features into a more meaningful one. Models can't easily learn divisions/multiplications. Manual feature engineering captures domain knowledge.
</details>

## Check 03: Binning
```python
df["age_group"] = pd.cut(df["age"], bins=[0, 18, 65, 100], labels=["child", "adult", "senior"])
```
<details><summary>Answer</summary>
Converts continuous to categorical. Useful when relationship is non-linear (e.g., very young and very old both have high medical costs).
</details>

## Check 04: Date features
```python
df["day_of_week"] = df["date"].dt.dayofweek
df["is_weekend"] = df["day_of_week"] >= 5
df["month"] = df["date"].dt.month
```
<details><summary>Answer</summary>
Extract useful info from dates. Day of week, month, is_weekend, is_holiday. Raw dates aren't useful to models.
</details>

## Check 05: Encoding choice
When to use one-hot vs label vs target encoding?
<details><summary>Answer</summary>
One-hot — low cardinality (<10 categories). Label — ordinal data (low/medium/high). Target — high cardinality (cities, zip codes). Frequency — when frequency matters.
</details>
