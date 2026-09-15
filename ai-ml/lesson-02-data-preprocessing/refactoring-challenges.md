# Lesson 02 — Refactoring Challenges

## Refactor 01 (Easy): Manual Scaling
### Before
```python
data = (data - data.min()) / (data.max() - data.min())
```
### After
```python
from sklearn.preprocessing import MinMaxScaler
data = MinMaxScaler().fit_transform(data)
```

## Refactor 02 (Medium): Manual Null Handling
### Before
```python
for col in df.columns:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mean())
```
### After
```python
df = df.fillna(df.mean())
```

## Refactor 03 (Hard): Repeated Preprocessing
### Before
```python
train = scaler.fit_transform(train)
test = scaler.transform(test)
model.fit(train, y_train)
preds = model.predict(test)
```
### After
```python
from sklearn.pipeline import Pipeline
pipe = Pipeline([("scaler", StandardScaler()), ("model", LogisticRegression())])
pipe.fit(train, y_train)
preds = pipe.predict(test)
```
