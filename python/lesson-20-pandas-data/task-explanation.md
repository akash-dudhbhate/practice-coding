# Lesson 20 — Data Processing with Pandas

## What you'll learn
- DataFrame creation and inspection
- read_csv for loading data
- Selecting and filtering data
- groupby for aggregation
- merge (JOIN) for combining DataFrames
- Handling missing data
- apply for custom transformations
- Exporting data (to_csv, to_excel, to_json)
- Pivot tables

## Lesson

### Create DataFrame
```python
import pandas as pd
df = pd.DataFrame({"name": ["Akash", "Bob"], "age": [25, 30]})
```

### Load and filter
```python
df = pd.read_csv("data.csv")
young = df[df["age"] < 30]
mumbai = df[df["city"] == "Mumbai"]
```

### Group and aggregate
```python
df.groupby("city")["age"].mean()
df.groupby("city").agg({"age": "mean", "name": "count"})
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Create a DataFrame from a dict with 5 people (name, age, city). Print shape, columns, and first 3 rows.
2. `easy/p02-solve.py` — Load a CSV file (create a sample one if needed). Filter rows where age > 25 and city is "Mumbai". Print the result.
3. `easy/p03-solve.py` — Create a DataFrame with some NaN values. Use `fillna()` to replace NaN ages with the mean age and NaN cities with "Unknown".

### Medium
4. `medium/p01-solve.py` — Create a sales DataFrame (product, region, sales, date). Use `groupby` to find total sales by region and average sales by product.
5. `medium/p02-solve.py` — Create two DataFrames: users (id, name, city) and orders (id, user_id, amount, date). Merge them on user_id. Find top 3 users by total order amount.
6. `medium/p03-solve.py` — Load a CSV, add a new column "category" using `apply()` based on age (< 20: "teen", 20-60: "adult", > 60: "senior"). Export to a new CSV.

### Hard
7. `hard/p01-solve.py` — Create a dataset of 100 students (random names, scores in 3 subjects). Calculate: average score per student, grade (A/B/C/D/F), class average per subject, top 5 students, pass/fail count. Export results.
8. `hard/p02-solve.py` — Build a data cleaning pipeline: load a messy CSV (missing values, wrong types, duplicates, extra spaces). Clean it: strip whitespace, fix types, drop duplicates, fill missing values, and export clean data.
9. `hard/p03-solve.py` — Create a time-series DataFrame (date, product, sales). Use pivot_table to create a matrix of products vs months. Calculate month-over-month growth. Identify trending products (positive growth for 3+ consecutive months).

### How to work
- Write your complete solution from scratch below the TODO marker.
- Remove the TODO line when done.
- Install pandas: `pip install pandas`
