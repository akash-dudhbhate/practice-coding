# Lesson 05 — Data Visualization

## What you'll learn
- How to create plots with matplotlib (line, scatter, histogram, box plot).
- How to use seaborn for statistical visualizations (pairplot, violin, heatmap).
- How to perform EDA — systematically explore data before modeling.
- How to interpret correlation matrices and identify feature relationships.

## Lesson

### Why visualization matters
Numbers alone hide patterns. A scatter plot can reveal a non-linear relationship that a correlation coefficient misses. A histogram can show skewness that a mean and std don't capture. Visualization is how you understand your data before feeding it to a model.

### The EDA checklist
1. **Overview** — shape, types, missing values, basic statistics.
2. **Univariate** — distribution of each variable (histograms, box plots).
3. **Bivariate** — relationships between pairs (scatter plots, box plots by category).
4. **Multivariate** — correlation heatmap, pairplot for all pairwise relationships.
5. **Missing data** — visualize where NaN values appear (is it random or systematic?).
6. **Outliers** — box plots and scatter plots to find extreme values.

### Matplotlib vs Seaborn
- **Matplotlib**: low-level, full control, more code. Good for custom plots.
- **Seaborn**: high-level, statistical, beautiful defaults, works with DataFrames. Good for quick EDA.
- Use seaborn for exploration, matplotlib for publication-quality customization.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Write your complete solution from scratch in each file.

### Easy (start here)
1. `easy/p01-solve.py` — **Basic line plot**: Create x values from 0 to 10 (100 points) and plot y = sin(x) and y = cos(x) on the same figure with a legend, labels, title, and grid. Save the figure to a file.
2. `easy/p02-solve.py` — **Histogram**: Generate 1000 random numbers from a normal distribution (mean=50, std=15). Plot a histogram with 30 bins, add a vertical line for the mean, and label axes. Save the figure.
3. `easy/p03-solve.py` — **Scatter plot**: Generate two correlated arrays (e.g., height and weight with noise). Plot a scatter plot with alpha=0.5, axis labels, and a title. Compute and display the correlation coefficient on the plot. Save the figure.

### Medium
4. `medium/p01-solve.py` — **Correlation heatmap**: Create a DataFrame with 5 numeric columns (some correlated, some not). Compute the correlation matrix and plot it as a seaborn heatmap with annotations, using the "coolwarm" colormap centered at 0. Save the figure.
5. `medium/p02-solve.py` — **Box plots by category**: Create a DataFrame with a numeric column and a categorical column (3+ categories). Plot a box plot of the numeric values grouped by category using seaborn. Add a title and labels. Save the figure.
6. `medium/p03-solve.py` — **Subplots**: Create a 2×2 subplot grid showing: (1) a histogram, (2) a scatter plot, (3) a box plot, (4) a line plot — all from the same dataset. Use `plt.subplots(2, 2)` and `tight_layout()`. Save the figure.

### Hard
7. `hard/p01-solve.py` — **Full EDA function**: Write a function that takes a DataFrame and performs complete EDA: prints shape, dtypes, missing values, and describe(); creates and saves a figure with 4 subplots (histogram of a numeric column, box plot by a categorical column, scatter of two numeric columns, and a correlation heatmap). Return a summary dictionary.
8. `hard/p02-solve.py` — **Pairplot with hue**: Load (or create) a DataFrame with 4 numeric features and a categorical target (2-3 classes). Create a seaborn pairplot colored by the target class. Save the figure. Write a brief analysis of which features best separate the classes based on the pairplot.
9. `hard/p03-solve.py` — **Missing data visualization**: Create a DataFrame with intentionally missing values (some columns have more missing than others). Create two visualizations: (a) a heatmap of missing values (white=missing, using `sns.heatmap(df.isnull())`), and (b) a bar chart showing the count of missing values per column. Save both figures. Write a summary of which columns have the most missing data.

### How to work
- Open a problem file, read the problem description in the docstring header.
- Write your complete solution from scratch (function signature + body).
- Remove the TODO line when done.
- Run `python <filename>` to test your solution.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
