# Lesson 05 — Concepts Explained (Data Visualization)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Matplotlib Basics

**What:**
Matplotlib is Python's foundational plotting library. You create figures and axes, plot data on them, and customize labels, titles, colors, and styles.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Basic line plot
plt.figure(figsize=(8, 4))
plt.plot(x, y, label="sin(x)", color="blue", linewidth=2)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Sine Wave")
plt.legend()
plt.grid(True)
plt.show()

# Multiple plots on one figure
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(x, np.sin(x), color="blue")
axes[0].set_title("Sine")
axes[1].plot(x, np.cos(x), color="red")
axes[1].set_title("Cosine")
plt.tight_layout()
plt.show()
```

**Why it exists:** Numbers alone don't reveal patterns. A table of 10,000 numbers is incomprehensible; a scatter plot instantly shows clusters, trends, and outliers. Visualization is how humans understand data — it's the first step of any data analysis.

**Where it's used:**
- EDA (Exploratory Data Analysis) — understanding data before modeling.
- Model evaluation — plotting learning curves, residuals, predictions vs actuals.
- Reporting — communicating findings to stakeholders.
- Debugging ML models — visualizing where the model fails.

**What goes wrong without it:**
- Training a model on data you've never visualized → you miss outliers, non-linear patterns, class imbalance → model performs poorly and you don't know why.
- Not setting `figsize` → plots are tiny and unreadable → you miss important patterns.
- Forgetting `plt.show()` in scripts → plot doesn't display (in non-interactive mode).
- Not using `tight_layout()` → labels overlap and are unreadable.

---

## Histograms

**What:**
A histogram shows the distribution of a single numeric variable — how often each value range occurs. It divides data into "bins" and counts how many values fall in each bin.

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(loc=50, scale=15, size=1000)

plt.figure(figsize=(8, 4))
plt.hist(data, bins=30, color="steelblue", edgecolor="white", alpha=0.7)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Distribution of Values")
plt.axvline(np.mean(data), color="red", linestyle="--", label=f"Mean={np.mean(data):.1f}")
plt.legend()
plt.show()

# Seaborn histogram with KDE (kernel density estimate)
import seaborn as sns
sns.histplot(data, bins=30, kde=True)
```

**Why it exists:** You need to understand the shape of your data — is it normal, skewed, bimodal? Are there outliers? Is it centered where you expect? The histogram is the fastest way to answer these questions.

**Where it's used:**
- Checking if a feature is normally distributed (important for some algorithms).
- Detecting skewness → decide if log-transform is needed.
- Identifying outliers → values far from the main distribution.
- Comparing distributions across groups (overlaid histograms).

**What goes wrong without it:**
- Assuming normal distribution when data is heavily skewed → model assumptions violated → poor predictions.
- Too few bins → distribution looks blocky, you miss multi-modal patterns.
- Too many bins → distribution looks noisy, you see random fluctuations instead of the true shape.
- Not checking the target variable distribution → severe class imbalance goes unnoticed → model predicts only the majority class.

---

## Scatter Plots

**What:**
A scatter plot shows the relationship between two numeric variables — each point is one observation with its x and y values. It reveals correlations, clusters, and outliers.

```python
import matplotlib.pyplot as plt
import numpy as np

height = np.random.normal(170, 10, 200)
weight = height * 0.4 + np.random.normal(0, 5, 200)

plt.figure(figsize=(8, 6))
plt.scatter(height, weight, alpha=0.6, edgecolors="black")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Height vs Weight")
plt.show()

# Colored by category
import seaborn as sns
tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="time")
```

**Why it exists:** The relationship between two variables is the most fundamental question in data analysis. "Does height correlate with weight?" "Do bigger houses cost more?" Scatter plots answer this instantly — correlation, non-linearity, clusters, and outliers are all visible.

**Where it's used:**
- Checking feature-target relationships → does the feature predict the target?
- Detecting non-linear patterns → a curved scatter means a linear model won't work well.
- Identifying clusters → groups of points suggest subpopulations.
- Finding outliers → points far from the main cloud.
- Multiclass problems → color points by class to see if classes are separable.

**What goes wrong without it:**
- Assuming a linear relationship when the scatter shows a curve → linear model underfits → poor predictions.
- Not checking for outliers → a few extreme points distort the correlation → misleading analysis.
- Too many points without `alpha` → the plot is a solid blob → can't see density → use `alpha=0.3` or a 2D histogram instead.
- Plotting two unrelated variables and seeing a "pattern" → spurious correlation → always check with correlation coefficient, not just the visual.

---

## Correlation and Heatmaps

**What:**
Correlation measures how strongly two variables move together — from -1 (opposite) to +1 (together) to 0 (no relationship). A heatmap visualizes the correlation matrix as a color grid.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "height": [170, 165, 180, 175, 160],
    "weight": [70, 65, 80, 75, 60],
    "age": [25, 30, 35, 28, 40],
    "income": [50000, 60000, 70000, 55000, 80000]
})

# Correlation matrix
corr_matrix = df.corr()
print(corr_matrix)
#         height  weight   age  income
# height    1.00    0.99  0.10    0.20
# weight    0.99    1.00  0.15    0.25

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", center=0, vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()
```

**Why it exists:** With 20 features, checking pairwise scatter plots is impractical (190 plots). The correlation matrix summarizes all pairwise relationships in one table. The heatmap makes it visual — red = positive, blue = negative, white = no correlation.

**Where it's used:**
- Feature selection → drop one of two highly correlated features (redundant).
- Detecting multicollinearity → features correlated with each other destabilize linear models.
- Finding predictive features → features highly correlated with the target are good predictors.
- EDA → understanding the overall structure of the data.

**What goes wrong without it:**
- Two highly correlated features (r=0.99) in a linear model → multicollinearity → unstable coefficients → model is sensitive to small data changes → unreliable.
- Correlation = 0 doesn't mean "no relationship" → only "no LINEAR relationship" → a U-shaped pattern has r=0 but a strong relationship → always check with scatter plots too.
- Correlation is not causation → height and shoe size correlate, but one doesn't cause the other → don't make causal claims from correlation.
- Including the target in the correlation heatmap and "discovering" it correlates with itself → trivially r=1 → meaningless.

---

## Box Plots

**What:**
A box plot shows the distribution of a variable through five statistics: minimum, first quartile (Q1), median, third quartile (Q3), and maximum. Outliers are shown as individual points beyond the "whiskers."

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Single box plot
sns.boxplot(data=df, x="department", y="salary")
plt.title("Salary Distribution by Department")
plt.show()

# Box plot structure:
#   ──── max (whisker)
#    |
#   [┼─]  Q3 (top of box), median (line), Q1 (bottom of box)
#    |
#   ──── min (whisker)
#   ○     outlier (beyond 1.5 × IQR)
```

**Why it exists:** Box plots compactly show the center, spread, and outliers of a distribution. They're especially useful for comparing distributions across groups — you can see which department has higher salaries, wider spread, or more outliers at a glance.

**Where it's used:**
- Comparing a metric across categories (salary by department, test scores by school).
- Detecting outliers → points beyond the whiskers.
- Checking for skewness → if the median is not centered in the box, the data is skewed.
- EDA before modeling → understanding feature distributions per class.

**What goes wrong without it:**
- Using only mean and std → you miss skewness, outliers, and multi-modality → wrong assumptions about the data.
- Not checking for outliers → extreme values distort the model → box plots make them obvious.
- Comparing groups with only bar charts (mean) → you miss that one group has huge variance while another is tight → box plots show the full picture.
- Misreading the whiskers → whiskers are NOT min/max; they extend to 1.5×IQR → points beyond are outliers, not the absolute extremes.

---

## Seaborn for Statistical Plots

**What:**
Seaborn is built on top of matplotlib and provides high-level functions for statistical visualization — less code, better defaults, more informative plots.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
tips = sns.load_dataset("tips")

# Pairplot — scatter plots of all pairs + histograms on diagonal
sns.pairplot(tips, hue="time")  # colored by time category
plt.show()

# Violin plot — box plot + kernel density estimate
sns.violinplot(data=tips, x="day", y="total_bill")
plt.show()

# Bar plot with confidence intervals
sns.barplot(data=tips, x="day", y="total_bill", hue="sex")
plt.show()

# Regression plot — scatter + linear fit + confidence interval
sns.regplot(data=tips, x="total_bill", y="tip")
plt.show()

# Count plot — bar chart of category counts
sns.countplot(data=tips, x="day")
plt.show()
```

**Why it exists:** Matplotlib requires many lines for a good-looking statistical plot. Seaborn does it in one line with better aesthetics, automatic labeling, and built-in statistical estimates (confidence intervals, regression lines). It also handles pandas DataFrames natively — you pass column names instead of arrays.

**Where it's used:**
- `pairplot` — quick overview of all pairwise relationships (the first plot you make in EDA).
- `violinplot` — comparing distributions across groups with density information.
- `regplot` — visualizing a linear relationship with the fit line and uncertainty.
- `countplot` — checking class balance in classification problems.
- `heatmap` — correlation matrices, confusion matrices.

**What goes wrong without it:**
- Writing 20 lines of matplotlib for what seaborn does in 1 → wasted time, inconsistent styling.
- `pairplot` on a dataset with 30 features → 30×30 = 900 subplots → takes forever to render and is unreadable → select a subset of features first.
- Seaborn functions return an Axes object, not a Figure → `plt.savefig()` works but `fig.savefig()` doesn't unless you get the figure first → confusion when saving plots.
- Using `sns.barplot` thinking it shows counts → it actually shows the MEAN of y for each x category → use `sns.countplot` for counts.

---

## EDA Workflow (Exploratory Data Analysis)

**What:**
EDA is the systematic process of understanding your data before modeling. You visualize distributions, relationships, missing patterns, and outliers to decide what preprocessing and modeling choices to make.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Step 1: Overview
print(df.shape)          # rows × columns
print(df.dtypes)         # data types
print(df.describe())     # statistics
print(df.isnull().sum()) # missing values per column

# Step 2: Univariate — one variable at a time
df.hist(figsize=(12, 8), bins=30)  # all numeric columns
plt.tight_layout()
plt.show()

# Step 3: Bivariate — two variables
sns.scatterplot(data=df, x="feature1", y="target")
plt.show()

# Step 4: Correlation
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", center=0)
plt.show()

# Step 5: Categorical vs numeric
sns.boxplot(data=df, x="category_col", y="target")
plt.show()

# Step 6: Missing data pattern
sns.heatmap(df.isnull(), cbar=False)  # white = missing
plt.show()
```

**Why it exists:** Jumping straight to modeling without EDA is like building a house without surveying the land. EDA reveals what preprocessing you need (scaling, encoding, imputation), which model to choose (linear vs non-linear), and what problems to watch for (imbalance, outliers, leakage).

**Where it's used:**
- At the start of every ML project, before any modeling.
- When getting a new dataset — always explore before assuming.
- During model debugging — visualize residuals, errors, and predictions.
- Before feature engineering — understand what features might be useful.

**What goes wrong without it:**
- Skipping EDA → you don't know the data has severe class imbalance → model predicts only majority class → 99% accuracy, 0% recall on minority.
- Not checking correlations → you include redundant features → multicollinearity → unstable model.
- Not visualizing the target distribution → you don't realize it's heavily skewed → regression model is biased.
- Not checking for missing data patterns → missingness is systematic (not random) → imputation introduces bias.
- Not looking at outliers → a few extreme values dominate the model → poor generalization.
