# Data Cleaning Pipeline (Python) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-13-data-cleaning-pipeline/
├── cleaner.py, pipeline.py, main.py, sample_data.csv
└── README.md
```

---

## Implementation Steps

### Step 1: Load Data

pd.read_csv with error handling. Show shape, columns, dtypes.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: Inspect Data

Show missing values, duplicates, outliers, data types. Summary stats.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Handle Missing Values

Drop rows with too many NaN. Fill numeric with median, categorical with mode.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: Remove Duplicates

Identify and drop duplicate rows. Log count before/after.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Fix Data Types

Convert date strings to datetime. Convert numeric columns. Category for low-cardinality.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Handle Outliers

IQR method: identify, cap (winsorize) or remove. Log count.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Standardize Text

Strip whitespace, normalize case, fix encoding issues in string columns.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Export Clean Data

Save to CSV. Generate cleaning report (what was changed, counts).

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: CLI Interface

argparse: input file, output file, --report. Configurable cleaning options.

**Checkpoint:** Step 9 is complete when the described functionality works.

---

## Final Checklist

- [ ] Load CSV with pandas
- [ ] Handle missing values (median/mode)
- [ ] Remove duplicates
- [ ] Fix data types (dates, numbers)
- [ ] Handle outliers (IQR)
- [ ] Standardize text columns
- [ ] Export cleaned CSV
- [ ] Cleaning report generated
- [ ] CLI with argparse

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
