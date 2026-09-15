# Lesson 11 — Feature Engineering

## What you'll learn
- What feature engineering is (and why it matters most)
- Handling categorical variables (label, one-hot, ordinal encoding)
- Scaling and normalization (Standard, MinMax, Robust)
- Handling missing data (drop, fill, impute)
- Binning (discretization of continuous values)
- Feature interactions (combining features)
- Text features (TF-IDF, word counts)
- Feature selection (keeping the best features)

## Lesson

### Encoding
```python
df = pd.get_dummies(df, columns=['category'])
```

### Scaling
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)
```

### Missing data
```python
df['age'].fillna(df['age'].median(), inplace=True)
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Create a DataFrame with a categorical column (color: red/blue/green). Apply one-hot encoding using `pd.get_dummies`. Print before and after.
2. `easy/p02-solve.py` — Create a DataFrame with two columns of different scales (age: 20-80, income: 20000-200000). Apply `StandardScaler`. Print before and after. Verify mean=0, std=1.
3. `easy/p03-solve.py` — Create a DataFrame with missing values. Fill numerical columns with median, categorical with mode. Print before and after.

### Medium
4. `medium/p01-solve.py` — Create a date column and engineer features: year, month, day of week, is_weekend, quarter. Use pandas datetime methods. Print the engineered DataFrame.
5. `medium/p02-solve.py` — Create a house dataset (sqft, bedrooms, price). Engineer: price_per_sqft, total_rooms, bedrooms_per_sqft. Train a model with and without engineered features. Compare R².
6. `medium/p03-solve.py` — Create a text dataset (10+ sentences). Extract features: text length, word count, has_url, has_question_mark. Then apply TF-IDF vectorization. Combine all features.

### Hard
7. `hard/p01-solve.py` — Build a complete feature engineering pipeline: load a real dataset (e.g., Titanic from seaborn), handle missing data, encode categoricals, scale numericals, create interaction features, and select top 10 features. Train a model and compare with raw data.
8. `hard/p02-solve.py` — Build a feature engineering comparison: take a dataset, train a model with (a) raw features, (b) scaled features, (c) scaled + encoded, (d) scaled + encoded + interactions. Compare accuracy for each stage. Show the improvement at each step.
9. `hard/p03-solve.py` — Build a text classification pipeline: create a synthetic text dataset (20+ documents, 2 categories), extract TF-IDF features, add custom features (length, word count, sentiment words), train a classifier, and evaluate. Show which features are most important.

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
