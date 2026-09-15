# Lesson 02 — Coding Check

Use this to verify your solutions before asking for review. Run each file and check the outputs against these criteria.

## Easy

### p01-solve.py — Fill missing values
- [ ] Input: DataFrame with NaN in numeric and categorical columns.
- [ ] Numeric columns imputed with median (not mean — median is robust to outliers).
- [ ] Categorical columns imputed with most_frequent (mode).
- [ ] No NaN values remain in the output — `df.isnull().sum().sum() == 0`.
- [ ] Test: input `{"age": [25, None, 35], "city": ["NYC", None, "LA"]}` → age column has median 30.0 in place of NaN, city column has "NYC" (most frequent) in place of NaN.
- [ ] Test: output shape matches input shape (no rows dropped).

### p02-solve.py — One-hot encode
- [ ] Uses `pd.get_dummies()` or `OneHotEncoder` to create binary columns.
- [ ] Original categorical column is removed and replaced with binary columns.
- [ ] Test: input `{"color": ["red", "blue", "green", "red"]}` → output has 3 columns (color_blue, color_green, color_red), each 0 or 1.
- [ ] Test: first row (red) → color_red=1, color_blue=0, color_green=0.
- [ ] Test: `drop_first=True` optionally used to avoid multicollinearity → 2 columns instead of 3.

### p03-solve.py — Standardize features
- [ ] Uses `StandardScaler` from sklearn.
- [ ] Returns a 2D array with same shape as input.
- [ ] Test: input `[[1, 10], [2, 20], [3, 30]]` → column 0 mean ≈ 0.0, std ≈ 1.0; column 1 mean ≈ 0.0, std ≈ 1.0.
- [ ] Test: `np.mean(scaled, axis=0)` returns values close to `[0.0, 0.0]` (within 1e-10).
- [ ] Test: `np.std(scaled, axis=0)` returns values close to `[1.0, 1.0]` (within 1e-10).

## Medium

### p01-solve.py — Full preprocessing pipeline
- [ ] Uses `sklearn.pipeline.Pipeline` with at least 2 preprocessing steps + model.
- [ ] Pipeline steps: SimpleImputer → StandardScaler → LogisticRegression (or similar).
- [ ] `fit` is called on `(X_train, y_train)` only.
- [ ] `predict` is called on `X_test` only.
- [ ] Test: with `make_classification` data (1000 samples, 20 features, some NaN injected), accuracy > 0.70.
- [ ] Test: pipeline has `named_steps` attribute with 3 steps.

### p02-solve.py — IQR outlier detection
- [ ] Computes Q1 (25th percentile) and Q3 (75th percentile).
- [ ] IQR = Q3 - Q1; bounds = [Q1 - 1.5*IQR, Q3 + 1.5*IQR].
- [ ] Values below lower bound are capped to lower bound; above upper bound capped to upper bound.
- [ ] Returns both the cleaned array and the count of outliers found.
- [ ] Test: input `[1, 2, 3, 4, 5, 100]` → 100 is an outlier → capped to Q3 + 1.5*IQR ≈ 12.5 → outlier count = 1.
- [ ] Test: input `[1, 2, 3, 4, 5]` → no outliers → count = 0, array unchanged.

### p03-solve.py — Mixed-type preprocessing
- [ ] Date string column converted with `pd.to_datetime()`.
- [ ] Categorical column encoded with `LabelEncoder` or `OrdinalEncoder`.
- [ ] Numeric column scaled with `StandardScaler` or `MinMaxScaler`.
- [ ] Test: input `{"date": ["2024-01-01"], "category": ["A", "B", "A"], "value": [100, 200, 300]}` → date column dtype is `datetime64`, category column is numeric (0/1), value column is scaled.
- [ ] Test: no string/object columns remain in the output (except possibly the datetime column).

## Hard

### p01-solve.py — Prevent data leakage
- [ ] `train_test_split` is called BEFORE any fitting of imputer/encoder/scaler.
- [ ] Imputer, encoder, and scaler are fit on `X_train` only (`fit_transform`).
- [ ] `X_test` is only `transform`ed (never `fit`).
- [ ] Returns both train accuracy and test accuracy.
- [ ] Test: train accuracy and test accuracy should be within ~10% of each other (no leakage → realistic gap).
- [ ] Test: if you compare to a leaky version (fit on all data), the leaky version's test accuracy is suspiciously higher → demonstrates the leakage problem.

### p02-solve.py — ColumnTransformer
- [ ] Uses `ColumnTransformer` to apply different preprocessing to different column subsets.
- [ ] Numeric columns: `SimpleImputer(strategy="median")` + `StandardScaler()`.
- [ ] Categorical columns: `SimpleImputer(strategy="most_frequent")` + `OneHotEncoder(handle_unknown="ignore")`.
- [ ] ColumnTransformer is chained with a classifier in a `Pipeline`.
- [ ] Test: with a mixed DataFrame (2 numeric, 2 categorical columns, some NaN), pipeline runs without error.
- [ ] Test: accuracy > 0.70 on `make_classification`-style data with categorical features added.
- [ ] Test: `handle_unknown="ignore"` in OneHotEncoder prevents crash on unseen categories in test set.

### p03-solve.py — Stratified split with imbalanced data
- [ ] Creates imbalanced dataset with `make_classification(weights=[0.95, 0.05])` or similar.
- [ ] Splits data twice: once with `stratify=y`, once without.
- [ ] Prints class distribution (value_counts) for train and test in both splits.
- [ ] Trains a model (e.g., LogisticRegression) on each split.
- [ ] Test: stratified split → test set has ~5% class 1 (matches original ratio).
- [ ] Test: non-stratified split → test set class 1 ratio may deviate significantly (could be 0% or 10%+).
- [ ] Test: recall for class 1 is reported for both — stratified version should have more reliable recall.
- [ ] Test: demonstrates that without stratify, the minority class may be underrepresented or absent in test set.

## How to verify

Run each file to test your solution:
```bash
python easy/p01-solve.py
python medium/p01-solve.py
python hard/p01-solve.py
```
