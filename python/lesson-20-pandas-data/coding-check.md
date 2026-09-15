# Lesson 20 — Coding Check

## Easy

### p01-solve.py — Create DataFrame
- [ ] DataFrame has 5 rows with columns: name, age, city
- [ ] `df.shape` returns (5, 3)
- [ ] `df.columns` includes all three column names
- [ ] `df.head(3)` shows first 3 rows

### p02-solve.py — Filter CSV
- [ ] Loads CSV with pd.read_csv()
- [ ] Filters age > 25 correctly
- [ ] Filters city == "Mumbai" correctly
- [ ] Combines both conditions with &

### p03-solve.py — Handle NaN
- [ ] DataFrame has some NaN values
- [ ] NaN ages replaced with mean age
- [ ] NaN cities replaced with "Unknown"
- [ ] No NaN values remain after fillna

## Medium

### p01-solve.py — Sales groupby
- [ ] DataFrame has product, region, sales, date columns
- [ ] Total sales by region (groupby + sum)
- [ ] Average sales by product (groupby + mean)
- [ ] Results are correct (verify manually)

### p02-solve.py — Merge and top users
- [ ] Two DataFrames created (users, orders)
- [ ] Merged on user_id
- [ ] Total order amount per user calculated
- [ ] Top 3 users by total amount identified
- [ ] Handles users with no orders (NaN or 0)

### p03-solve.py — Apply and export
- [ ] New "category" column added using apply()
- [ ] Categories: teen (<20), adult (20-60), senior (>60)
- [ ] Exported to CSV with index=False
- [ ] File is created and readable

## Hard

### p01-solve.py — Student analysis
- [ ] 100 students with random data
- [ ] Average score per student calculated
- [ ] Grade assigned (A/B/C/D/F based on average)
- [ ] Class average per subject
- [ ] Top 5 students identified
- [ ] Pass/fail count (pass = all subjects >= 40)
- [ ] Results exported to CSV

### p02-solve.py — Data cleaning pipeline
- [ ] Loads messy CSV
- [ ] Strips whitespace from string columns
- [ ] Fixes data types (e.g., age as int, date as datetime)
- [ ] Drops duplicate rows
- [ ] Fills missing values appropriately
- [ ] Exports clean data to new CSV
- [ ] Reports what was cleaned (rows dropped, values filled)

### p03-solve.py — Time-series analysis
- [ ] DataFrame with date, product, sales columns
- [ ] Pivot table: products (rows) vs months (columns)
- [ ] Month-over-month growth calculated
- [ ] Trending products identified (3+ consecutive months of positive growth)
- [ ] Results are correct and clearly presented
