# Lesson 04 — Coding Check

Use this to verify your solutions before asking for review. Run each file and check the outputs against these criteria.

## Easy

### p01-solve.py — Load and inspect DataFrame
- [ ] Creates DataFrame from a dictionary with at least 4 columns.
- [ ] Prints `df.shape` → should be `(5, 4)`.
- [ ] Prints `df.columns` → all 4 column names.
- [ ] Prints `df.dtypes` → shows types for each column.
- [ ] Prints `df.describe()` → statistics for numeric columns (count, mean, std, min, etc.).
- [ ] Test: DataFrame has 5 rows and 4 columns.
- [ ] Test: numeric columns (age, salary) show in describe(); string column (name) does not.

### p02-solve.py — Filter rows
- [ ] Filter (a): `df[df["salary"] > 60000]` → only rows with salary > 60000.
- [ ] Filter (b): `df[df["department"] == "Engineering"]` → only Engineering rows.
- [ ] Filter (c): `df[(df["salary"] > 60000) & (df["department"] == "Engineering")]` → uses `&` with parentheses.
- [ ] Test: if input has Alice(55000, Sales), Bob(70000, Eng), Charlie(80000, Eng), filter (c) returns Bob and Charlie only.
- [ ] Test: no `and`/`or` used (must be `&`/`|`).

### p03-solve.py — Handle missing values
- [ ] Numeric columns filled with median: `df[col].fillna(df[col].median())`.
- [ ] Categorical columns filled with "Unknown": `df[col].fillna("Unknown")`.
- [ ] Returns cleaned DataFrame with no NaN values.
- [ ] Returns count of NaN filled per column.
- [ ] Test: input `{"age": [25, None, 35], "city": ["NYC", None, "LA"]}` → age NaN filled with 30.0 (median), city NaN filled with "Unknown".
- [ ] Test: `df.isnull().sum().sum() == 0` on the output.

## Medium

### p01-solve.py — GroupBy aggregations
- [ ] (a) Total revenue per product: `df.groupby("product")["revenue"].sum()` or `df.assign(revenue=df["quantity"]*df["price"]).groupby("product")["revenue"].sum()`.
- [ ] (b) Average quantity per region: `df.groupby("region")["quantity"].mean()`.
- [ ] (c) Transactions per product per region: `df.groupby(["product", "region"]).size()` or `.count()`.
- [ ] Test: (a) returns a Series indexed by product with revenue totals.
- [ ] Test: (b) returns a Series indexed by region with average quantities.
- [ ] Test: (c) returns a Series or DataFrame with product-region as index and counts as values.

### p02-solve.py — Merge DataFrames
- [ ] Uses `pd.merge()` with `how="left"` and `on="dept_id"`.
- [ ] Unmatched departments filled with "Unassigned": `df["dept_name"].fillna("Unassigned")`.
- [ ] Test: employee with no matching dept_id → dept_name is "Unassigned", not NaN.
- [ ] Test: all employees appear in the output (left join preserves left rows).
- [ ] Test: merged DataFrame has columns: emp_id, name, dept_id, dept_name.

### p03-solve.py — Feature extraction from dates
- [ ] Converts date strings: `pd.to_datetime(df["date"])`.
- [ ] Extracts year: `df["date"].dt.year`.
- [ ] Extracts month: `df["date"].dt.month`.
- [ ] Extracts day_of_week: `df["date"].dt.dayofweek`.
- [ ] Extracts is_weekend: `df["date"].dt.dayofweek >= 5`.
- [ ] Extracts quarter: `df["date"].dt.quarter`.
- [ ] Test: input "2024-01-15" (Monday) → year=2024, month=1, day_of_week=0, is_weekend=False, quarter=1.
- [ ] Test: input "2024-01-13" (Saturday) → is_weekend=True, day_of_week=5.

## Hard

### p01-solve.py — Customer analytics pipeline
- [ ] Groups by customer_id for aggregations.
- [ ] total_spent: `df.groupby("customer_id")["amount"].sum()`.
- [ ] num_transactions: `df.groupby("customer_id")["amount"].count()`.
- [ ] avg_transaction: `df.groupby("customer_id")["amount"].mean()`.
- [ ] first_purchase_date: `df.groupby("customer_id")["date"].min()`.
- [ ] days_since_last_purchase: computed from `df.groupby("customer_id")["date"].max()` relative to a reference date.
- [ ] Test: output has one row per unique customer_id.
- [ ] Test: all 5 feature columns are present in the output.
- [ ] Test: total_spent = avg_transaction × num_transactions for each customer.

### p02-solve.py — Merge with aggregation
- [ ] Merges users with purchases on user_id (left join to keep all users).
- [ ] total_purchases: count of purchases per user.
- [ ] avg_purchase_amount: mean amount per user.
- [ ] purchase_frequency: number of purchases / months since signup.
- [ ] Handles users with no purchases (fill with 0 or NaN appropriately).
- [ ] Test: output has one row per user.
- [ ] Test: users with no purchases have total_purchases = 0.
- [ ] Test: purchase_frequency is a positive number for users with purchases.

### p03-solve.py — Pivot table and crosstab
- [ ] (a) Pivot table: `df.pivot_table(values="sales", index="month", columns="product", aggfunc="sum")`.
- [ ] (b) Crosstab with average: `pd.crosstab(df["product"], df["region"], values=df["sales"], aggfunc="mean")`.
- [ ] (c) Best-selling product per region: `df.loc[df.groupby("region")["sales"].idxmax()]` or similar.
- [ ] Test: (a) pivot table has months as rows, products as columns.
- [ ] Test: (b) crosstab has products as rows, regions as columns, average sales as values.
- [ ] Test: (c) returns one row per region with the top product and its sales.
- [ ] Test: no NaN values in the best-seller result (each region has a winner).

## How to verify

Run each file to test your solution:
```bash
python easy/p01-solve.py
python medium/p01-solve.py
python hard/p01-solve.py
```
