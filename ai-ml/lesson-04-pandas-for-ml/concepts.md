# Lesson 04 — Concepts Explained (Pandas for ML)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## DataFrame Basics

**What:**
A DataFrame is a 2D table with labeled rows and columns — like a spreadsheet in Python. Each column can have a different data type (int, float, string, datetime).

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [50000, 70000, 90000]
})

# Inspect
df.head()          # first 5 rows
df.info()          # column types, non-null counts, memory usage
df.describe()      # statistics for numeric columns
df.shape           # (3, 3) — (rows, cols)
df.columns         # Index(["name", "age", "salary"])
df.dtypes          # data type of each column

# Select columns
df["age"]          # one column as a Series
df[["name", "age"]]  # multiple columns as a DataFrame

# Select rows
df.iloc[0]         # first row by position
df.loc[0]          # first row by label
```

**Why it exists:** NumPy arrays are fast but have no labels — columns are just indices 0, 1, 2. Real data has column names, mixed types, and missing values. DataFrames give you labeled, mixed-type, tabular data with powerful operations that would require complex NumPy code.

**Where it's used:**
- Loading CSV/Excel/SQL data — `pd.read_csv("data.csv")` is the starting point of most ML projects.
- Data exploration and cleaning before feeding to sklearn.
- Feature engineering — creating new columns from existing ones.
- Storing and manipulating any tabular dataset.

**What goes wrong without it:**
- Using NumPy arrays for tabular data → you lose column names → code is unreadable (`X[:, 3]` vs `df["salary"]`).
- Mixed data types in NumPy → everything upcasts to string/object → can't do numeric operations.
- No easy way to handle missing data in raw NumPy → you'd write custom logic for every dataset.
- `df["age"]` returns a Series (1D); `df[["age"]]` returns a DataFrame (2D) — confusing them causes shape errors in sklearn.

---

## Filtering and Boolean Indexing

**What:**
Filtering selects rows that meet a condition. You create a boolean Series (True/False per row) and use it to index the DataFrame.

```python
import pandas as pd

df = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 35], "city": ["NYC", "LA", "NYC"]})

# Single condition
df[df["age"] > 28]           # rows where age > 28
df[df["city"] == "NYC"]      # rows where city is NYC

# Multiple conditions (use & for AND, | for OR, with parentheses!)
df[(df["age"] > 28) & (df["city"] == "NYC")]  # age > 28 AND city is NYC
df[(df["age"] < 30) | (df["city"] == "LA")]   # age < 30 OR city is LA

# String methods
df[df["name"].str.startswith("A")]  # names starting with A

# isin — match multiple values
df[df["city"].isin(["NYC", "LA"])]  # city is NYC or LA

# Negation
df[~(df["city"] == "NYC")]   # city is NOT NYC
```

**Why it exists:** You constantly need subsets of data — "show me customers over 30 in Mumbai" or "filter out rows with invalid values." Pandas filtering makes this a one-liner instead of a loop.

**Where it's used:**
- Removing invalid rows: `df = df[df["price"] > 0]`.
- Selecting a subset for analysis: `df[df["category"] == "electronics"]`.
- Train/test filtering: `train = df[df["date"] < "2024-01-01"]`.
- Outlier removal: `df = df[df["value"] < df["value"].quantile(0.99)]`.

**What goes wrong without it:**
- Using `and`/`or` instead of `&`/`|` → `ValueError: The truth value of a Series is ambiguous` → crash. Pandas uses bitwise operators for element-wise comparison.
- Forgetting parentheses → `df["age"] > 28 & df["city"] == "NYC"` → operator precedence error → wrong results or crash.
- Chained indexing: `df[df["age"] > 30]["salary"] = 0` → `SettingWithCopyWarning` → assignment may not work (operates on a copy, not the original).
- `==` with NaN → `NaN == NaN` is `False`, not `True` → rows with NaN are excluded when you think they'd be included → use `df["col"].isna()` instead.

---

## GroupBy Operations

**What:**
`groupby` splits the data into groups by a column's values, applies a function to each group, and combines the results. This is the "split-apply-combine" pattern.

```python
import pandas as pd

df = pd.DataFrame({
    "department": ["Sales", "Sales", "Engineering", "Engineering", "HR"],
    "salary": [50000, 60000, 80000, 90000, 55000],
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"]
})

# Group by department and compute mean salary
df.groupby("department")["salary"].mean()
# Sales: 55000, Engineering: 85000, HR: 55000

# Multiple aggregations
df.groupby("department")["salary"].agg(["mean", "min", "max", "count"])
#         mean    min    max   count
# Sales  55000  50000  60000     2
# Eng    85000  80000  90000     2
# HR     55000  55000  55000     1

# Group by multiple columns
df.groupby(["department", "name"])["salary"].sum()

# Custom aggregation
df.groupby("department")["salary"].agg(lambda x: x.max() - x.min())  # range per group
```

**Why it exists:** You often need statistics per category — average salary per department, total sales per month, count of orders per customer. Without groupby, you'd write nested loops and dictionaries. Groupby makes it a single expression.

**Where it's used:**
- Feature engineering: `df["avg_salary_dept"] = df.groupby("department")["salary"].transform("mean")` — add department average as a feature.
- EDA: understanding how a metric varies across categories.
- Aggregation: total revenue per product, average rating per category.
- Time-series: `df.groupby(df["date"].dt.month)["sales"].sum()` — monthly totals.

**What goes wrong without it:**
- Manual loop with dictionaries → 20 lines of code instead of 1 → slow and error-prone.
- `groupby` without selecting a column → returns a DataFrameGroupBy object, not data → you must apply an aggregation function.
- `agg("mean")` on a column with strings → `TypeError` → can't average text → must select only numeric columns.
- `transform` vs `agg`: `agg` reduces to one row per group; `transform` keeps the original shape (broadcasts group values back to each row) → using the wrong one gives wrong shapes.

---

## Merge and Join

**What:**
Merge combines two DataFrames based on common columns (like SQL JOIN). You specify how to match rows and what type of join (inner, left, right, outer).

```python
import pandas as pd

employees = pd.DataFrame({"emp_id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
salaries = pd.DataFrame({"emp_id": [1, 2, 4], "salary": [50000, 70000, 90000]})

# Inner join — only rows with matching emp_id in both
pd.merge(employees, salaries, on="emp_id", how="inner")
# emp_id  name   salary
#   1     Alice  50000
#   2     Bob    70000

# Left join — all rows from left, NaN for unmatched right
pd.merge(employees, salaries, on="emp_id", how="left")
# emp_id  name     salary
#   1     Alice    50000
#   2     Bob      70000
#   3     Charlie  NaN

# Outer join — all rows from both, NaN for unmatched
pd.merge(employees, salaries, on="emp_id", how="outer")

# Different column names
pd.merge(employees, salaries, left_on="emp_id", right_on="emp_id", how="inner")
```

**Why it exists:** Real data is spread across multiple tables — users in one table, transactions in another, products in a third. You need to join them to create a complete feature set for ML. Merge is the pandas equivalent of SQL JOIN.

**Where it's used:**
- Combining user profile data with transaction history.
- Joining product catalog with sales data.
- Adding lookup tables (e.g., city → coordinates).
- Time-series: merging actuals with forecasts by date.

**What goes wrong without it:**
- Merge on wrong column → every row matches every row (cartesian product) → DataFrame explodes from 1000 rows to 1,000,000 → memory crash.
- Forgetting `how="left"` → inner join drops rows that don't have a match → you lose data you needed.
- Column name conflicts → pandas adds `_x` and `_y` suffixes → confusing column names → wrong feature selected downstream.
- Merge keys with different types (int vs string) → no matches → empty DataFrame → silent failure.
- Duplicate keys in the right table → one-to-many join → duplicated rows in the result → inflated training data.

---

## Handling Missing Data in Pandas

**What:**
Pandas provides tools to detect, fill, and drop missing values (represented as `NaN` — Not a Number, or `None`).

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({"A": [1, 2, np.nan, 4], "B": ["x", None, "z", "w"], "C": [1.0, 2.0, 3.0, np.nan]})

# Detect
df.isnull()           # boolean DataFrame — True where NaN
df.isnull().sum()     # count of NaN per column
df.isnull().sum().sum()  # total NaN count

# Drop
df.dropna()           # drop rows with ANY NaN
df.dropna(how="all")  # drop rows where ALL values are NaN
df.dropna(subset=["A"])  # drop rows where column A is NaN
df.dropna(axis=1)     # drop columns with any NaN

# Fill
df.fillna(0)                          # fill all NaN with 0
df["A"].fillna(df["A"].mean())        # fill column A with its mean
df["B"].fillna("Unknown")             # fill categorical with a constant
df.fillna(method="ffill")             # forward fill (propagate last valid value)
df.fillna(method="bfill")             # backward fill
```

**Why it exists:** Missing data is universal in real datasets. You need flexible tools to handle it — sometimes you drop, sometimes you fill, sometimes you interpolate. The choice depends on the data and the problem.

**Where it's used:**
- Cleaning survey data where respondents skipped questions.
- Time-series gaps — forward-fill stock prices for non-trading days.
- Medical data where not all tests were ordered for all patients.
- Feature engineering — filling with a meaningful default before model training.

**What goes wrong without it:**
- Not checking for NaN → model crashes with `ValueError: Input contains NaN`.
- `df.dropna()` on a dataset where every row has at least one NaN → empty DataFrame → everything breaks.
- `fillna(df.mean())` before train/test split → data leakage (mean includes test data) → inflated scores.
- `fillna(method="ffill")` on unsorted data → fills with the wrong previous value → garbage data. Always sort by time before forward-filling.
- `np.nan == np.nan` is `False` → filtering `df[df["A"] == np.nan]` returns nothing → use `df["A"].isna()` instead.

---

## Feature Extraction with Pandas

**What:**
Feature extraction is creating new columns from existing data — extracting date parts, splitting strings, computing ratios, binning continuous values.

```python
import pandas as pd

df = pd.DataFrame({
    "date": pd.to_datetime(["2024-01-15", "2024-03-20", "2024-07-04"]),
    "price": [100, 250, 50],
    "quantity": [2, 5, 1],
    "email": ["alice@gmail.com", "bob@yahoo.com", "charlie@gmail.com"]
})

# Date features
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day_of_week"] = df["date"].dt.dayofweek  # 0=Monday
df["is_weekend"] = df["date"].dt.dayofweek >= 5

# Computed features
df["total"] = df["price"] * df["quantity"]
df["price_per_unit"] = df["price"] / df["quantity"]

# String extraction
df["email_domain"] = df["email"].str.split("@").str[1]  # gmail.com, yahoo.com
df["email_provider"] = df["email_domain"].str.split(".").str[0]  # gmail, yahoo

# Binning
df["price_category"] = pd.cut(df["price"], bins=[0, 50, 200, 1000], labels=["cheap", "medium", "expensive"])
df["quantity_bin"] = pd.qcut(df["quantity"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])  # quantile bins
```

**Why it exists:** Raw data rarely has the features the model needs. The model doesn't know that "day_of_week=5" means "weekend" — you have to create that feature. Good feature extraction is the difference between a 70% and 90% accurate model.

**Where it's used:**
- Time-series: extracting month, day, hour, is_holiday from timestamps.
- Text: extracting domain from email, word count from reviews.
- E-commerce: price per unit, discount percentage, total order value.
- User behavior: days since last purchase, average order value.

**What goes wrong without it:**
- Feeding raw dates as strings → model can't use them → loses all temporal patterns.
- `pd.cut` with wrong bin edges → values outside the range become NaN → missing data introduced accidentally.
- `.str` accessor on a column with NaN → some operations return NaN for those rows → must handle explicitly.
- Creating features after train/test split → leakage (if feature uses test data statistics like quantiles) → always extract features before splitting, but compute aggregations (like mean) on train only.
- String operations on non-string columns → `AttributeError: Can only use .str accessor with string values` → convert with `.astype(str)` first.

---

## Apply and Lambda Functions

**What:**
`apply` runs a function on each row or column of a DataFrame. Combined with `lambda`, it lets you define custom transformations inline.

```python
import pandas as pd

df = pd.DataFrame({"price": [100, 200, 300], "quantity": [2, 5, 1]})

# Apply a function to a column
df["price_log"] = df["price"].apply(lambda x: np.log(x))

# Apply to each row (axis=1)
df["total"] = df.apply(lambda row: row["price"] * row["quantity"], axis=1)

# Apply with multiple conditions
df["category"] = df["price"].apply(lambda x: "expensive" if x > 150 else "cheap")

# Apply a named function
def discount_price(row):
    if row["quantity"] > 3:
        return row["price"] * 0.9  # 10% discount for bulk
    return row["price"]

df["discounted"] = df.apply(discount_price, axis=1)
```

**Why it exists:** Vectorized operations cover most cases, but some transformations are too complex for a simple expression. `apply` gives you the flexibility to run any Python function on your data while still working within the pandas framework.

**Where it's used:**
- Custom feature logic that can't be expressed with simple arithmetic.
- Text processing: `df["review"].apply(lambda x: len(x.split()))` — word count.
- Conditional logic across multiple columns.
- Applying a pre-trained model to each row for inference.

**What goes wrong without it:**
- Using `apply` for something that could be vectorized → 10-100x slower than `df["price"] * df["quantity"]` → performance bottleneck on large datasets.
- `apply` with `axis=1` (row-wise) is much slower than `axis=0` (column-wise) → prefer column-wise operations.
- Lambda capturing a variable that changes → all rows get the final value → use the variable correctly or pass as argument.
- `apply` modifying the DataFrame in-place → unexpected side effects → always assign the result.
- Using `apply` on a large DataFrame when a vectorized `.str` method exists → unnecessary slowness.

---

## Pivot Tables and Crosstabs

**What:**
Pivot tables reshape data — summarizing values by two dimensions (rows and columns). Crosstabs compute frequency tables between two categorical columns.

```python
import pandas as pd

df = pd.DataFrame({
    "date": ["2024-01", "2024-01", "2024-02", "2024-02", "2024-01"],
    "product": ["A", "B", "A", "B", "A"],
    "sales": [100, 200, 150, 250, 120]
})

# Pivot table — sales by month (rows) and product (columns)
df.pivot_table(values="sales", index="date", columns="product", aggfunc="sum")
# product    A    B
# date
# 2024-01  220  200
# 2024-02  150  250

# Crosstab — count of occurrences
pd.crosstab(df["date"], df["product"])
# product   A  B
# date
# 2024-01   2  1
# 2024-02   1  1

# Pivot table with multiple aggregations
df.pivot_table(values="sales", index="date", columns="product", aggfunc=["sum", "mean"])
```

**Why it exists:** Sometimes you need data in a wide format (months as columns) instead of long format (months as rows). Pivot tables restructure data for reporting, visualization, or as features for specific model types.

**Where it's used:**
- Creating time-series features: sales per month per product as columns.
- EDA: understanding the relationship between two categorical variables.
- Reporting: monthly summary tables for dashboards.
- Feature engineering: converting transaction logs to user-product matrices (recommendation systems).

**What goes wrong without it:**
- `pivot_table` with duplicate index-column combinations and no `aggfunc` → `ValueError: Data must be 1-dimensional` → must specify `aggfunc` to handle duplicates.
- `pivot` (without `_table`) on duplicate entries → error. Use `pivot_table` which handles duplicates via aggregation.
- Crosstab on continuous variables → huge matrix with mostly zeros → memory explosion → bin continuous variables first.
- Pivoting and then feeding directly to sklearn → the pivot index becomes a column → unexpected shape → reset index and handle properly.
