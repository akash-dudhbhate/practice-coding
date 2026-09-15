# Lesson 02 — Debug Exercises

## Debug 01 (Easy: Filling NaN with Mean Before Split
```python
df.fillna(df.mean(), inplace=True)
X_train, X_test = train_test_split(df)
```
<details><summary>Answer</summary>
**Bug:** Filling NaN with mean of ALL data — test data leaks into training.
**Fix:** Split first, fill with TRAIN mean only.
</details>

## Debug 02 (Medium): Encoding Categorical Before Split
```python
df_encoded = pd.get_dummies(df)
X_train, X_test = train_test_split(df_encoded)
```
<details><summary>Answer</summary>
**Bug:** Get dummies on all data — categories in test influence training columns.
**Fix:** Split first, fit encoder on train, transform test.
</details>

## Debug 03 (Hard): Not Handling Unseen Categories
```python
encoder = OneHotEncoder()
encoder.fit(X_train[["color"]])
encoder.transform(X_test[["color"]])
# X_test has "purple" which wasn't in train
```
<details><summary>Answer</summary>
**Bug:** Unseen category causes error or wrong encoding.
**Fix:** `OneHotEncoder(handle_unknown="ignore")`.
</details>
