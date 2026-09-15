# Lesson 02 — Data Preprocessing

## What you'll learn
- How to clean real-world datasets (missing values, duplicates, wrong types).
- How to convert categorical text into numbers the model can use.
- How to scale and normalize features so no single feature dominates.
- How to build a preprocessing pipeline that prevents data leakage.

## Lesson

### Why preprocessing matters
Models learn from numbers. Real-world data is messy — it has gaps, text labels, mismatched units, outliers, and duplicates. If you feed raw messy data to a model, it either crashes (`ValueError: contains NaN`) or learns garbage patterns. Preprocessing is the bridge between raw data and a trainable dataset.

### The preprocessing checklist
1. **Handle missing values** — impute or drop `NaN`/`None`.
2. **Remove duplicates** — prevent over-weighting repeated rows.
3. **Fix data types** — convert strings to numbers, text to datetime.
4. **Encode categories** — one-hot for nominal, label for ordinal.
5. **Handle outliers** — detect and cap/remove extreme values.
6. **Scale features** — standardize or normalize to a common range.
7. **Split correctly** — fit preprocessing on train only, transform test.

### The golden rule: fit on train, transform on test
```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # learn mean/std from TRAIN
X_test_scaled = scaler.transform(X_test)         # apply SAME mean/std to test
```
Never fit on the full dataset. Never fit on test data. This prevents data leakage.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Write your complete solution from scratch in each file.

### Easy (start here)
1. `easy/p01-solve.py` — **Fill missing values**: Given a DataFrame with NaN values, impute missing numeric columns with the median and missing categorical columns with the most frequent value. Return the cleaned DataFrame.
2. `easy/p02-solve.py` — **One-hot encode a categorical column**: Given a DataFrame with a categorical column, apply one-hot encoding using `pd.get_dummies()` and return the resulting DataFrame with binary columns.
3. `easy/p03-solve.py` — **Standardize features**: Given a 2D NumPy array of features, fit a `StandardScaler` and return the scaled array. Verify the mean is ~0 and std is ~1 for each column.

### Medium
4. `medium/p01-solve.py` — **Full preprocessing pipeline**: Build a `sklearn Pipeline` that imputes missing values (mean strategy), scales features (StandardScaler), and trains a LogisticRegression model. Fit on training data, predict on test data, and return the accuracy score.
5. `medium/p02-solve.py` — **Detect and handle outliers with IQR**: Given a NumPy array, detect outliers using the IQR method (1.5 × IQR rule). Cap outliers to the boundary values (winsorization) and return the cleaned array along with the count of outliers found.
6. `medium/p03-solve.py` — **Mixed-type column preprocessing**: Given a DataFrame with numeric, categorical, and datetime-as-string columns: convert the date strings to datetime objects, label-encode the categorical column, and scale the numeric column. Return the fully processed DataFrame.

### Hard
7. `hard/p01-solve.py` — **Prevent data leakage in a full pipeline**: Given a raw DataFrame with missing values, categorical columns, and a target column, split into train/test FIRST, then fit all preprocessing (imputer, one-hot encoder, scaler) on training data only. Train a model and return both train and test accuracy to show no leakage occurred.
8. `hard/p02-solve.py` — **ColumnTransformer for mixed data types**: Use `sklearn.compose.ColumnTransformer` to apply different preprocessing to numeric columns (impute + scale) vs categorical columns (impute + one-hot) in a single transformer. Chain it with a RandomForestClassifier in a Pipeline. Fit, predict, and return the accuracy.
9. `hard/p03-solve.py` — **Stratified split with imbalanced data**: Create a synthetic imbalanced dataset (95% class 0, 5% class 1) using `make_classification`. Split with and without `stratify`. For each split, print the class distribution in train and test. Train a model on each and compare accuracy and recall to demonstrate why stratification matters for imbalanced data.

### How to work
- Open a problem file, read the problem description in the docstring header.
- Write your complete solution from scratch (function signature + body).
- Remove the TODO line when done.
- Run `python <filename>` to test your solution.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
