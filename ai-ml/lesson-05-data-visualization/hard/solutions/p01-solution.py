# Lesson 05 — Hard P01: Full EDA function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def full_eda(df, numeric_col, categorical_col, scatter_x, scatter_y):
    """Perform complete EDA on a DataFrame.

    Prints shape, dtypes, missing values, and summary statistics.
    Creates and saves a figure with 4 subplots:
    - histogram of a numeric column
    - box plot by a categorical column
    - scatter of two numeric columns
    - correlation heatmap

    Returns a summary dictionary.
    """
    # Print basic info
    print("=" * 50)
    print("SHAPE:", df.shape)
    print("\nDTYPES:\n", df.dtypes)
    print("\nMISSING VALUES:\n", df.isnull().sum())
    print("\nDESCRIBE:\n", df.describe())
    print("=" * 50)

    # Create 4-subplot figure
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # (1) Histogram of numeric column
    axes[0, 0].hist(df[numeric_col].dropna(), bins=30, color="steelblue", edgecolor="white")
    axes[0, 0].set_title(f"Histogram of {numeric_col}")

    # (2) Box plot by categorical column
    categories = df[categorical_col].dropna().unique()
    box_data = [df[df[categorical_col] == c][numeric_col].dropna().values for c in categories]
    axes[0, 1].boxplot(box_data, labels=categories)
    axes[0, 1].set_title(f"Box Plot of {numeric_col} by {categorical_col}")

    # (3) Scatter of two numeric columns
    axes[1, 0].scatter(df[scatter_x], df[scatter_y], alpha=0.5, color="coral")
    axes[1, 0].set_title(f"Scatter: {scatter_x} vs {scatter_y}")
    axes[1, 0].set_xlabel(scatter_x)
    axes[1, 0].set_ylabel(scatter_y)

    # (4) Correlation heatmap
    numeric_df = df.select_dtypes(include=[np.number])
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", center=0, ax=axes[1, 1])
    axes[1, 1].set_title("Correlation Heatmap")

    plt.tight_layout()
    plt.savefig("eda_figure.png", dpi=150)
    print("\nFigure saved to eda_figure.png")

    # Return summary dictionary
    summary = {
        "shape": df.shape,
        "dtypes": df.dtypes.to_dict(),
        "missing": df.isnull().sum().to_dict(),
        "describe": df.describe().to_dict(),
    }
    return summary


# Demo with synthetic data
if __name__ == "__main__":
    np.random.seed(42)
    n = 300
    df = pd.DataFrame({
        "age": np.random.randint(18, 70, n),
        "income": np.random.randn(n) * 20000 + 50000,
        "score": np.random.uniform(0, 100, n),
        "experience": np.random.randint(0, 40, n),
        "department": np.random.choice(["Sales", "Engineering", "HR"], n),
    })
    # Inject some missing values
    df.loc[df.sample(20).index, "income"] = np.nan
    df.loc[df.sample(10).index, "score"] = np.nan

    result = full_eda(df, numeric_col="income", categorical_col="department",
                      scatter_x="age", scatter_y="income")
    print("\nSummary keys:", list(result.keys()))
