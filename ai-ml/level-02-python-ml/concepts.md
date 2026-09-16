# Level 02 — Concepts Reference

## Easy

### NumPy Arrays
- `np.random.seed(42)` → reproducible randomness
- `np.random.randint(0, 100, (4, 5))` → 4×5 ints
- `arr.shape`, `arr.dtype`, `arr.ndim`, `arr.size`
- `arr.mean(axis=0)` → mean of each column

### DataFrames
- `pd.DataFrame({'col': [values]})` → build a table
- `df.head()`, `df.shape`, `df.dtypes`

### Missing Values
- `NaN` = missing. Models can't use it.
- Numeric → `df['col'].fillna(df['col'].median())`
- Category → `df['col'].fillna(df['col'].mode()[0])`

## Medium

### Pipelines
- `Pipeline([('imputer', SimpleImputer()), ('scaler', StandardScaler()), ('model', LogisticRegression())])`
- Steps run in order, fit on train only → no leakage.

### Outliers (IQR)
- `Q1, Q3 = np.percentile(data, [25, 75])`
- `IQR = Q3 - Q1`; bounds = Q1 − 1.5·IQR, Q3 + 1.5·IQR
- `np.clip(data, lower, upper)` caps outliers.

### Mixed Types
- `pd.to_datetime(df['date'])` → datetime
- `LabelEncoder().fit_transform(df['cat'])` → ints
- `StandardScaler().fit_transform(df[['num']])` → mean 0, std 1

## Hard

### Data Leakage
- Fitting preprocessing on ALL data before splitting = leakage.
- Fix: `train_test_split` FIRST, then Pipeline handles the rest.

### ColumnTransformer
- Different transforms per column group:
  `ColumnTransformer([('num', num_pipe, num_cols), ('cat', cat_pipe, cat_cols)])`

### Stratified Split
- `train_test_split(..., stratify=y)` keeps class ratios in both splits.
- Critical for imbalanced data.
