# lesson-18-flask-server — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

## Mistake 01: Chained indexing
```python
# WRONG — SettingWithCopyWarning
df[df["x"] > 0]["y"] = 1

# CORRECT
df.loc[df["x"] > 0, "y"] = 1
```

## Mistake 02: Using apply when vectorized works
```python
# SLOW
df["y"] = df["x"].apply(lambda x: x ** 2)

# FAST
df["y"] = df["x"] ** 2
```

## Mistake 03: Not handling NaN
```python
# WRONG — NaN propagates
df["total"] = df["a"] + df["b"]  # NaN if either is NaN

# CORRECT — fill or skip
df["total"] = df["a"].fillna(0) + df["b"].fillna(0)
```

## Mistake 04: Modifying while iterating
```python
# WRONG — unpredictable
for idx, row in df.iterrows():
    df.loc[idx, "x"] = row["y"] * 2

# CORRECT — vectorized
df["x"] = df["y"] * 2
```

## Mistake 05: Not specifying merge column
```python
# AMBIGUOUS
pd.merge(df1, df2)

# EXPLICIT
pd.merge(df1, df2, on="id", how="left")
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Inline Route Logic
### Before
```python
@app.route("/users")
def users():
    users = db.query("SELECT * FROM users")
    return json.dumps(users)
```
### After
```python
@app.route("/users")
def users():
    users = db.query("SELECT * FROM users")
    return jsonify(users)
```

## Refactor 02 (Medium): No Error Handler
### Before
```python
@app.route("/users/<id>")
def get_user(id):
    user = db.get(id)
    if not user:
        return "Not found", 404
    return jsonify(user)
```
### After
```python
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

@app.route("/users/<id>")
def get_user(id):
    user = db.get_or_404(id)
    return jsonify(user)
```

## Refactor 03 (Hard): Global State
### Before
```python
db = None
@app.before_first_request
def setup():
    global db
    db = connect_db()
```
### After
```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
# No global state, managed by extension
```

---

## Approach Comparison — different ways to solve it

## Problem: Filter and Transform

### Approach 1: Multiple steps
```python
filtered = df[df["age"] > 18]
filtered["category"] = filtered["age"].apply(classify)
result = filtered.groupby("category").mean()
```

### Approach 2: Method chaining
```python
result = (df
    .query("age > 18")
    .assign(category=lambda x: x["age"].apply(classify))
    .groupby("category")
    .mean()
)
```

**Winner:** Approach 2 — chaining is more readable, no intermediate variables.

---

## Problem: Handle Missing Data

### Approach 1: Drop
```python
df = df.dropna()
```
**Cons:** Loses data. Bad if many rows have some NaN.

### Approach 2: Fill
```python
df = df.fillna(df.mean())
```
**Pros:** Keeps all rows. **Cons:** May introduce bias.

### Approach 3: Impute (sklearn)
```python
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="median")
df[["age"]] = imputer.fit_transform(df[["age"]])
```

**Winner:** Depends on data. Drop if few NaN. Fill/impute if many.
