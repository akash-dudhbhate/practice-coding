# Lesson 11 — Refactoring Challenges

## Refactor 01 (Easy): Manual Feature Creation
### Before
```python
df["total"] = df["a"] + df["b"] + df["c"]
df["avg"] = (df["a"] + df["b"] + df["c"]) / 3
```
### After
```python
df["total"] = df[["a", "b", "c"]].sum(axis=1)
df["avg"] = df[["a", "b", "c"]].mean(axis=1)
```

## Refactor 02 (Medium): Manual One-Hot
### Before
```python
for cat in df["color"].unique():
    df[f"color_{cat}"] = (df["color"] == cat).astype(int)
df = df.drop("color", axis=1)
```
### After
```python
df = pd.get_dummies(df, columns=["color"], prefix="color")
```

## Refactor 03 (Hard): Manual Feature Pipeline
### Before
```python
df["log_income"] = np.log1p(df["income"])
df = pd.get_dummies(df, columns=["city"])
df["age_bucket"] = pd.cut(df["age"], bins=[0, 18, 35, 60, 100])
```
### After
```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer
preprocessor = ColumnTransformer([
    ("log", FunctionTransformer(np.log1p), ["income"]),
    ("ohe", OneHotEncoder(), ["city"]),
])
```
