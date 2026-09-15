# Lesson 02 — Intuition Checks

## Check 01: Why preprocess?
<details><summary>Answer</summary>
ML models need: numerical data, similar scales, no missing values, consistent formats. Raw data is messy. Preprocessing transforms it into model-friendly format.
</details>

## Check 02: Scaling
```python
# Feature A: 0-1
# Feature B: 0-1000000
```
<details><summary>Answer</summary>
Without scaling, feature B dominates. Models like SVM, KNN, neural networks are scale-sensitive. Tree-based models don't need scaling.
</details>

## Check 03: StandardScaler vs MinMaxScaler
```python
StandardScaler: mean=0, std=1
MinMaxScaler: 0 to 1
```
<details><summary>Answer</summary>
Standard — for normally distributed data, robust to outliers. MinMax — for bounded data, sensitive to outliers. Use Standard for most cases.
</details>

## Check 04: Encoding
```python
# "red", "blue", "green" → ?
```
<details><summary>Answer</summary>
Don't use 0, 1, 2 (implies order). Use one-hot encoding: red=[1,0,0], blue=[0,1,0], green=[0,0,1]. For high cardinality, use target encoding.
</details>

## Check 05: Missing data
```python
df.isnull().sum()
```
<details><summary>Answer</summary>
Options: drop rows (if few), drop columns (if mostly missing), impute (fill with mean/median/mode/predicted). Median is robust to outliers.
</details>
