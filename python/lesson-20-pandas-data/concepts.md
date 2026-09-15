# Lesson 20 — Concepts Explained (Data Processing with Pandas)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## DataFrame

**What:** A DataFrame is a 2D table — like a spreadsheet or SQL table. It has rows (indexed) and columns (named).

```python
import pandas as pd

data = {
    "name": ["Akash", "Bob", "Carol"],
    "age": [25, 30, 28],
    "city": ["Mumbai", "London", "NYC"]
}
df = pd.DataFrame(data)

#    name  age    city
# 0  Akash   25  Mumbai
# 1    Bob   30  London
# 2  Carol   28     NYC

df.head()        # first 5 rows
df.shape         # (3, 3) — rows, columns
df.columns       # Index(['name', 'age', 'city'])
df.dtypes        # data types of each column
```

**Why it exists:** Without DataFrames, you'd process tabular data with lists of dicts — no filtering, no aggregation, no joining. DataFrames provide spreadsheet-like operations in code.

**Where it's used:** Data analysis, ML preprocessing, financial analysis, reporting, ETL pipelines. Pandas is the #1 data analysis library in Python.

**What goes wrong without it:**
- Using lists of dicts → filtering requires loops, aggregation requires manual counting → 50 lines instead of 1.
- Large data in pure Python → slow. Pandas uses NumPy under the hood → 100x faster.
- Confusing index and columns: `df[0]` tries to access a COLUMN named 0, not the first row. Rows are accessed with `.iloc`.

---

## read_csv

**What:** Load data from a CSV file into a DataFrame.

```python
df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", sep=",", header=0, index_col=0)
df = pd.read_csv("data.csv", usecols=["name", "age"])    # only specific columns
df = pd.read_csv("data.csv", nrows=100)                   # only first 100 rows
df = pd.read_csv("data.csv", dtype={"age": int})          # specify types
```

**Why it exists:** CSV is the most common data format. Without `read_csv`, you'd parse CSV manually (split by comma, handle quotes, handle newlines) → error-prone. `read_csv` handles all of this.

**Where it's used:** Loading any CSV data — datasets, exports, logs, configs.

**What goes wrong without it:**
- Wrong separator: `sep=";"` for European CSVs (they use semicolons). Default is `,`.
- No header: `header=None` if the CSV has no column names. Otherwise first row becomes column names.
- Encoding issues: `encoding="utf-8"` vs `encoding="latin-1"`. Wrong encoding → `UnicodeDecodeError`.
- Large files: `read_csv` loads everything into memory. For huge files, use `chunksize=10000`.

---

## Selecting Data

**What:** Select rows, columns, or cells from a DataFrame.

```python
# Select column
df["name"]              # returns a Series (one column)
df[["name", "age"]]     # returns a DataFrame (multiple columns)

# Select rows by position
df.iloc[0]              # first row
df.iloc[0:3]            # first 3 rows
df.iloc[0, 1]           # row 0, column 1 (cell value)

# Select rows by label/index
df.loc[0]               # row with index 0
df.loc[0:2, "name"]     # rows 0-2, column "name"

# Boolean indexing (filtering)
df[df["age"] > 25]                       # rows where age > 25
df[(df["age"] > 25) & (df["city"] == "Mumbai")]  # multiple conditions
```

**Why it exists:** Without selection, you can't filter or extract data. `df[df["age"] > 25]` is one line; in pure Python, it's a loop with an if condition.

**Where it's used:** Every data analysis task — filtering, subsetting, extracting specific data.

**What goes wrong without it:**
- `df["age"]` returns a Series; `df[["age"]]` returns a DataFrame. Different types → different methods available.
- `&` vs `and`: pandas requires `&` for element-wise AND, not `and`. `and` → ValueError. Also need parentheses: `(df["a"] > 0) & (df["b"] > 0)`.
- `iloc` (position-based) vs `loc` (label-based): `df.loc[3]` gets row with INDEX 3, not the 3rd row. If index is 0-based, they're the same. If index is custom, they differ.

---

## Filtering

**What:** Select rows that match a condition.

```python
# Single condition
young = df[df["age"] < 30]

# Multiple conditions (& = AND, | = OR, ~ = NOT)
mumbai_young = df[(df["city"] == "Mumbai") & (df["age"] < 30)]
not_mumbai = df[~(df["city"] == "Mumbai")]    # NOT Mumbai

# .isin() for multiple values
indian_cities = df[df["city"].isin(["Mumbai", "Delhi", "Bangalore"])]

# .str methods for string filtering
starts_with_a = df[df["name"].str.startswith("A")]
contains_ak = df[df["name"].str.contains("ak", case=False)]
```

**Why it exists:** Without filtering, you process all data even when you need a subset. Filtering lets you focus on relevant rows — critical for large datasets.

**Where it's used:** Data cleaning, analysis, reporting — "show me all active users from Mumbai over 25".

**What goes wrong without it:**
- `df["age"] > 30` returns a boolean Series, not filtered data. You need `df[df["age"] > 30]` to get the rows.
- Chaining: `df[df["age"] > 30]["city"]` works but may warn about chained indexing. Use `.loc` instead: `df.loc[df["age"] > 30, "city"]`.
- NaN in conditions: `df[df["age"] > 30]` excludes NaN rows. Use `df["age"].notna()` to include them explicitly.

---

## groupby

**What:** Group rows by a column's value, then apply an aggregation (sum, mean, count, etc.).

```python
# Group by city, calculate average age
df.groupby("city")["age"].mean()
# city
# London    30.0
# Mumbai    25.0
# NYC       28.0

# Group by city, multiple aggregations
df.groupby("city").agg({
    "age": ["mean", "min", "max"],
    "name": "count"
})

# Group by multiple columns
df.groupby(["city", "age"]).size()
```

**Why it exists:** Without groupby, you'd loop through all rows, maintain dicts of sums and counts, then compute averages — 20 lines of code. `groupby` does it in one line.

**Where it's used:** Reporting (sales by region, users by signup month), analytics (average rating by product), data summarization.

**What goes wrong without it:**
- Forgetting to aggregate: `df.groupby("city")` → returns a GroupBy object, not data. Must apply `.mean()`, `.sum()`, `.count()`, etc.
- `groupby` returns a Series with the group column as index. Use `.reset_index()` to get it back as a column.
- Multiple aggregations produce multi-index columns → confusing. Use `.agg()` with named aggregations for cleaner output.

---

## merge (JOIN)

**What:** Combine two DataFrames based on a common column — like SQL JOIN.

```python
users = pd.DataFrame({"user_id": [1, 2, 3], "name": ["Akash", "Bob", "Carol"]})
orders = pd.DataFrame({"user_id": [1, 1, 2], "product": ["A", "B", "A"]})

merged = pd.merge(users, orders, on="user_id")
#    user_id   name product
# 0        1  Akash       A
# 1        1  Akash       B
# 2        2    Bob       A
# Carol has no orders → not in result (inner join by default)

# Left join (keep all users)
pd.merge(users, orders, on="user_id", how="left")
# Carol appears with NaN for product
```

**Why it exists:** Without merge, you'd loop through both DataFrames, match rows manually → slow and error-prone. `merge` handles all join types (inner, left, right, outer) efficiently.

**Where it's used:** Combining data from multiple sources — users + orders, products + categories, students + courses.

**What goes wrong without it:**
- Column name mismatch: `on="user_id"` requires both DataFrames to have `user_id`. If one has `id`, use `left_on="user_id", right_on="id"`.
- Duplicate columns: both DataFrames have "name" → merged has "name_x" and "name_y". Rename before merging or use `suffixes=`.
- Wrong join type: inner (default) drops unmatched rows. If you need all rows, use `how="left"` or `how="outer"`.

---

## Handling Missing Data

**What:** Real-world data has missing values (NaN). Pandas provides tools to handle them.

```python
# Check for missing values
df.isnull().sum()              # count NaN per column
df.isna().any()                # which columns have NaN

# Drop missing values
df.dropna()                    # drop rows with any NaN
df.dropna(subset=["age"])      # drop rows where age is NaN
df.dropna(how="all")           # drop rows where ALL values are NaN

# Fill missing values
df.fillna(0)                   # replace NaN with 0
df["age"].fillna(df["age"].mean())  # replace with mean
df["city"].fillna("Unknown")   # replace with a string
df.ffill()                     # forward fill (use previous value)
```

**Why it exists:** Without handling, NaN values cause errors in calculations (`mean()` returns NaN if any value is NaN) and break ML models. You must decide: drop, fill, or impute.

**Where it's used:** Every data cleaning pipeline. Missing data is the #1 issue in real-world datasets.

**What goes wrong without it:**
- `df["age"].mean()` with NaN values → returns NaN (not the mean of non-NaN values). Use `skipna=True` (default) or `df["age"].dropna().mean()`.
- `fillna()` returns a new DataFrame — doesn't modify in place. Use `inplace=True` or reassign.
- Dropping too many rows → losing data. Check how many rows you're dropping before doing it.

---

## apply

**What:** Apply a function to each element, row, or column.

```python
# Apply to a column (element-wise)
df["age_squared"] = df["age"].apply(lambda x: x ** 2)

# Apply to rows
df["full_name"] = df.apply(lambda row: f"{row['first']} {row['last']}", axis=1)

# Apply with multiple arguments
def categorize(age, threshold=30):
    return "young" if age < threshold else "old"

df["category"] = df["age"].apply(categorize, threshold=25)
```

**Why it exists:** Without `apply`, you'd loop through rows and build a new column manually → slow. `apply` vectorizes the operation (faster) and is more readable.

**Where it's used:** Creating derived columns, transforming data, applying custom logic to each row.

**What goes wrong without it:**
- `apply` with `axis=1` (row-wise) is slow for large DataFrames. Use vectorized operations when possible: `df["age"] * 2` is faster than `df["age"].apply(lambda x: x * 2)`.
- Modifying data inside `apply` → doesn't modify the original DataFrame. Must assign the result.
- `apply` with complex functions → hard to debug. Use simple, pure functions.

---

## Export Data

**What:** Save a DataFrame to a file (CSV, Excel, JSON, etc.).

```python
df.to_csv("output.csv", index=False)           # CSV without index column
df.to_csv("output.csv", index=False, sep=";")  # with custom separator
df.to_excel("output.xlsx", sheet_name="data")  # Excel
df.to_json("output.json", orient="records")    # JSON
```

**Why it exists:** Without export, your processed data stays in memory → lost when the program exits. Export saves results for sharing, reporting, or further processing.

**Where it's used:** Saving cleaned data, generating reports, exporting for ML pipelines, sharing results.

**What goes wrong without it:**
- `index=True` (default) → saves the index as an extra column → when you read it back, you have an unnamed column. Use `index=False`.
- Excel requires `openpyxl` installed → `pip install openpyxl`. Without it → `ModuleNotFoundError`.
- Large DataFrames to Excel → Excel has a 1M row limit. Use CSV for large data.

---

## Pivot Tables

**What:** Reshape data — like Excel pivot tables. Summarize by two dimensions.

```python
df = pd.DataFrame({
    "city": ["Mumbai", "Mumbai", "London", "London"],
    "year": [2023, 2024, 2023, 2024],
    "sales": [100, 150, 200, 250]
})

pivot = df.pivot_table(values="sales", index="city", columns="year", aggfunc="sum")
# year     2023  2024
# city
# London    200   250
# Mumbai    100   150
```

**Why it exists:** Without pivot tables, reshaping data requires complex groupby + unstack operations. Pivot tables are the standard way to summarize data across two dimensions.

**Where it's used:** Reporting, dashboards, cross-tabulation, data summarization for presentations.

**What goes wrong without it:**
- Duplicate index-column combinations → `aggfunc` must be specified (default is `mean`). Without it → error if duplicates exist.
- NaN in pivot → combinations that don't exist in the data → fill with `fill_value=0`.
- Pivot vs pivot_table: `pivot` doesn't aggregate (fails on duplicates), `pivot_table` does. Use `pivot_table` for real data.
