# Lesson 05 — Coding Check

Use this to verify your solutions before asking for review. Run each file and check the outputs against these criteria.

## Easy

### p01-solve.py — Basic line plot
- [ ] Creates x with `np.linspace(0, 10, 100)`.
- [ ] Plots both sin(x) and cos(x) with `plt.plot()`.
- [ ] Has a legend (`plt.legend()`).
- [ ] Has x-label, y-label, and title.
- [ ] Has grid (`plt.grid(True)`).
- [ ] Saves figure with `plt.savefig("filename.png")`.
- [ ] Test: figure file is created in the directory.
- [ ] Test: both curves are visible (different colors or line styles).

### p02-solve.py — Histogram
- [ ] Generates 1000 random numbers with `np.random.normal(50, 15, 1000)` or `default_rng().normal(50, 15, 1000)`.
- [ ] Plots histogram with `bins=30`.
- [ ] Adds vertical line at the mean with `plt.axvline(np.mean(data), ...)`.
- [ ] Labels x-axis and y-axis.
- [ ] Saves figure.
- [ ] Test: the histogram shape is approximately bell-shaped (normal distribution).
- [ ] Test: the vertical line is near the center of the distribution (around 50).

### p03-solve.py — Scatter plot
- [ ] Generates two correlated arrays (e.g., `weight = height * 0.4 + noise`).
- [ ] Plots with `plt.scatter()` and `alpha=0.5`.
- [ ] Computes correlation with `np.corrcoef()` or `pd.Series.corr()`.
- [ ] Displays correlation value on the plot (in title or annotation).
- [ ] Saves figure.
- [ ] Test: points form a visible upward (or downward) trend.
- [ ] Test: correlation coefficient is displayed and is > 0.5 (strong correlation).

## Medium

### p01-solve.py — Correlation heatmap
- [ ] Creates a DataFrame with 5 numeric columns.
- [ ] At least 2 columns are intentionally correlated.
- [ ] Computes `df.corr()`.
- [ ] Uses `sns.heatmap()` with `annot=True`, `cmap="coolwarm"`, `center=0`.
- [ ] `vmin=-1, vmax=1` set for proper color scale.
- [ ] Saves figure.
- [ ] Test: diagonal values are all 1.0 (self-correlation).
- [ ] Test: the intentionally correlated columns show high correlation (> 0.7) in red.

### p02-solve.py — Box plots by category
- [ ] Creates DataFrame with a numeric column and a categorical column (3+ categories).
- [ ] Uses `sns.boxplot(data=df, x="category", y="numeric")` or equivalent.
- [ ] Has title and axis labels.
- [ ] Saves figure.
- [ ] Test: plot shows 3+ boxes (one per category).
- [ ] Test: boxes show median line, Q1/Q3 box, and whiskers.
- [ ] Test: any outliers are shown as individual points beyond whiskers.

### p03-solve.py — Subplots
- [ ] Uses `fig, axes = plt.subplots(2, 2, figsize=(...))`.
- [ ] Subplot (1): histogram on `axes[0, 0]`.
- [ ] Subplot (2): scatter plot on `axes[0, 1]`.
- [ ] Subplot (3): box plot on `axes[1, 0]`.
- [ ] Subplot (4): line plot on `axes[1, 1]`.
- [ ] Uses `plt.tight_layout()` to prevent overlap.
- [ ] Saves figure.
- [ ] Test: all 4 subplots are populated (not empty).
- [ ] Test: no label overlap visible.

## Hard

### p01-solve.py — Full EDA function
- [ ] Function takes a DataFrame as input.
- [ ] Prints `df.shape`, `df.dtypes`, `df.isnull().sum()`, `df.describe()`.
- [ ] Creates a 2×2 subplot figure.
- [ ] Subplot 1: histogram of a numeric column.
- [ ] Subplot 2: box plot of a numeric column by a categorical column.
- [ ] Subplot 3: scatter plot of two numeric columns.
- [ ] Subplot 4: correlation heatmap.
- [ ] Returns a summary dictionary (e.g., `{"shape": ..., "missing": ..., "corr_max": ...}`).
- [ ] Saves figure.
- [ ] Test: function runs without error on a sample DataFrame.
- [ ] Test: returned dictionary has meaningful values (shape tuple, missing counts, etc.).
- [ ] Test: saved figure has all 4 subplots populated.

### p02-solve.py — Pairplot with hue
- [ ] Creates or loads a DataFrame with 4 numeric features and 1 categorical target.
- [ ] Uses `sns.pairplot(df, hue="target_column")`.
- [ ] Saves figure with `plt.savefig()` (pairplot returns a PairGrid; use `.fig.savefig()` or `plt.savefig()`).
- [ ] Writes a brief text analysis of which features separate classes.
- [ ] Test: pairplot shows 4×4 grid of subplots.
- [ ] Test: diagonal shows distributions (histograms/KDEs) colored by class.
- [ ] Test: off-diagonal shows scatter plots colored by class.
- [ ] Test: analysis text identifies at least one feature that separates classes well.

### p03-solve.py — Missing data visualization
- [ ] Creates a DataFrame with intentionally missing values (varying amounts per column).
- [ ] Visualization (a): `sns.heatmap(df.isnull(), cbar=False)` — shows missing pattern.
- [ ] Visualization (b): bar chart of missing value counts per column (`df.isnull().sum()`).
- [ ] Saves both figures.
- [ ] Writes a summary of which columns have the most missing data.
- [ ] Test: heatmap shows white/yellow stripes where data is missing.
- [ ] Test: bar chart shows different heights for different columns (varying missing counts).
- [ ] Test: summary correctly identifies the column with the most missing values.
- [ ] Test: the column with the most injected NaN has the tallest bar in the chart.

## How to verify

Run each file to test your solution:
```bash
python easy/p01-solve.py
python medium/p01-solve.py
python hard/p01-solve.py
```
Check that saved figure files exist:
```bash
ls *.png
```
