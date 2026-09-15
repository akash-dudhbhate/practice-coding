# Lesson 05 — Hard P03: Missing data visualization
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame with intentionally missing values
# Using the modern numpy.random.Generator API
rng = np.random.default_rng(42)
n = 200
df = pd.DataFrame({
    "name": [f"User_{i}" for i in range(n)],
    "age": rng.integers(18, 70, n).astype(float),
    "income": rng.standard_normal(n) * 20000 + 50000,
    "department": rng.choice(["Sales", "Engineering", "HR", "Marketing"], n),
    "score": rng.uniform(0, 100, n),
    "rating": rng.integers(1, 6, n).astype(float),
})

# Inject missing values at different rates per column
df.loc[df.sample(40).index, "income"] = np.nan       # 20% missing
df.loc[df.sample(30).index, "score"] = np.nan         # 15% missing
df.loc[df.sample(15).index, "rating"] = np.nan        # 7.5% missing
df.loc[df.sample(5).index, "age"] = np.nan            # 2.5% missing
# "name" and "department" have no missing values

print("Missing values per column:")
print(df.isnull().sum())
print(f"\nTotal rows: {n}")

# (a) Heatmap of missing values (white = missing)
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap=["white", "gray"], yticklabels=False, ax=ax1)
ax1.set_title("Missing Values Heatmap (white = missing)")
ax1.set_xlabel("Columns")
ax1.set_ylabel("Rows")
plt.tight_layout()
plt.savefig("missing_heatmap.png", dpi=150)
print("\nHeatmap saved to missing_heatmap.png")

# (b) Bar chart showing count of missing values per column
fig2, ax2 = plt.subplots(figsize=(8, 5))
missing_counts = df.isnull().sum()
missing_counts = missing_counts[missing_counts > 0].sort_values(ascending=False)
ax2.bar(missing_counts.index, missing_counts.values, color="coral", edgecolor="white")
ax2.set_title("Missing Values Count per Column")
ax2.set_xlabel("Column")
ax2.set_ylabel("Number of Missing Values")
for i, v in enumerate(missing_counts.values):
    ax2.text(i, v + 0.5, str(v), ha="center", va="bottom")
plt.tight_layout()
plt.savefig("missing_bar.png", dpi=150)
print("Bar chart saved to missing_bar.png")

# Summary
print("\n=== Summary ===")
print("Columns with most missing data:")
for col, count in missing_counts.items():
    pct = count / n * 100
    print(f"  {col}: {count} missing ({pct:.1f}%)")
print("\nColumns with no missing data: name, department")
