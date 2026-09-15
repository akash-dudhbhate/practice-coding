# Lesson 04 — Pandas for ML

## What you'll learn
- How to use DataFrames for loading, inspecting, and cleaning tabular data.
- How to filter rows with boolean conditions and select subsets.
- How to aggregate data with groupby for per-category statistics.
- How to merge multiple DataFrames (like SQL joins).
- How to extract features from existing columns (dates, strings, computed columns).

## Lesson

### Why pandas for ML?
ML models need clean, numeric, tabular data. Real data comes as CSV files with mixed types, missing values, and text labels. Pandas is the tool that takes you from raw CSV to model-ready features. It's the first thing you use in every ML project.

### The pandas workflow for ML
1. **Load**: `pd.read_csv("data.csv")` → DataFrame
2. **Inspect**: `df.head()`, `df.info()`, `df.describe()` → understand the data
3. **Clean**: handle missing values, fix types, remove duplicates
4. **Filter**: select relevant rows and columns
5. **Aggregate**: compute group statistics for feature engineering
6. **Merge**: join with other tables to enrich features
7. **Extract**: create new features from dates, strings, and computed columns
8. **Convert**: `df.values` or `df.to_numpy()` → NumPy array for sklearn

### Key vocabulary
- **Series**: a single column (1D).
- **DataFrame**: a table with multiple columns (2D).
- **Index**: row labels (can be numbers, dates, or strings).
- **dtypes**: data type of each column (int64, float64, object, datetime64).

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Write your complete solution from scratch in each file.

### Easy (start here)
1. `easy/p01-solve.py` — **Load and inspect a DataFrame**: Create a DataFrame from a dictionary with 5 rows and columns: name, age, salary, department. Print shape, column names, dtypes, and summary statistics. Return the DataFrame.
2. `easy/p02-solve.py` — **Filter rows**: Given a DataFrame of employees, filter to: (a) employees with salary > 60000, (b) employees in "Engineering" department, (c) employees with salary > 60000 AND in "Engineering". Return all three filtered DataFrames.
3. `easy/p03-solve.py` — **Handle missing values**: Given a DataFrame with NaN values in numeric and categorical columns, fill numeric NaN with the column median and categorical NaN with "Unknown". Return the cleaned DataFrame and the count of NaN values that were filled per column.

### Medium
4. `medium/p01-solve.py` — **GroupBy aggregations**: Given a DataFrame of sales (columns: date, product, region, quantity, price), compute: (a) total revenue per product, (b) average quantity per region, (c) number of transactions per product per region. Return all three results.
5. `medium/p02-solve.py` — **Merge two DataFrames**: Given an employees DataFrame (emp_id, name, dept_id) and a departments DataFrame (dept_id, dept_name), perform a left join to get employee names with their department names. Handle employees with no matching department (fill with "Unassigned"). Return the merged DataFrame.
6. `medium/p03-solve.py` — **Feature extraction from dates**: Given a DataFrame with a date column (as strings), convert to datetime, then extract: year, month, day_of_week, is_weekend (boolean), and quarter. Return the DataFrame with the new columns added.

### Hard
7. `hard/p01-solve.py` — **Customer analytics pipeline**: Given a transactions DataFrame (transaction_id, customer_id, date, amount), compute per-customer features: total_spent, num_transactions, avg_transaction, first_purchase_date, days_since_last_purchase. Return a DataFrame with one row per customer.
8. `hard/p02-solve.py` — **Merge with aggregation for features**: Given a users DataFrame (user_id, signup_date, country) and a purchases DataFrame (user_id, purchase_date, amount), merge and compute per-user features: total_purchases, avg_purchase_amount, purchase_frequency (purchases per month since signup). Return the enriched users DataFrame.
9. `hard/p03-solve.py` — **Pivot table and crosstab analysis**: Given a sales DataFrame (date, product, region, sales), create: (a) a pivot table of total sales by month (rows) and product (columns), (b) a crosstab of product vs region showing average sales, (c) identify the best-selling product per region. Return all three results.

### How to work
- Open a problem file, read the problem description in the docstring header.
- Write your complete solution from scratch (function signature + body).
- Remove the TODO line when done.
- Run `python <filename>` to test your solution.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
