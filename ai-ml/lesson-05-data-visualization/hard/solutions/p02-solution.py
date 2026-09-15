# Lesson 05 — Hard P02: Pairplot with hue
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a DataFrame with 4 numeric features and a categorical target (3 classes)
np.random.seed(42)
n = 150

# Class 0: lower values
data_0 = pd.DataFrame({
    "sepal_length": np.random.normal(5.0, 0.5, n // 3),
    "sepal_width": np.random.normal(3.3, 0.3, n // 3),
    "petal_length": np.random.normal(1.5, 0.3, n // 3),
    "petal_width": np.random.normal(0.2, 0.1, n // 3),
    "species": "setosa",
})

# Class 1: medium values
data_1 = pd.DataFrame({
    "sepal_length": np.random.normal(5.9, 0.5, n // 3),
    "sepal_width": np.random.normal(2.8, 0.3, n // 3),
    "petal_length": np.random.normal(4.3, 0.5, n // 3),
    "petal_width": np.random.normal(1.3, 0.2, n // 3),
    "species": "versicolor",
})

# Class 2: higher values
data_2 = pd.DataFrame({
    "sepal_length": np.random.normal(6.5, 0.6, n // 3),
    "sepal_width": np.random.normal(3.0, 0.3, n // 3),
    "petal_length": np.random.normal(5.5, 0.6, n // 3),
    "petal_width": np.random.normal(2.1, 0.3, n // 3),
    "species": "virginica",
})

df = pd.concat([data_0, data_1, data_2], ignore_index=True)

# Create pairplot colored by target class
pairplot = sns.pairplot(df, hue="species", diag_kind="kde", palette="Set2")
pairplot.fig.suptitle("Pairplot Colored by Species", y=1.02)
plt.savefig("pairplot_hue.png", dpi=150, bbox_inches="tight")
print("Figure saved to pairplot_hue.png")

# Brief analysis
print("\n=== Analysis ===")
print("Based on the pairplot:")
print("1. petal_length and petal_width best separate the three species.")
print("   - setosa has distinctly small petals (clearly separated).")
print("   - versicolor and virginica show some overlap but are mostly separable.")
print("2. sepal_length also helps distinguish setosa from the other two.")
print("3. sepal_width alone is the least discriminative feature (high overlap).")
print("4. The petal_length vs petal_width scatter shows the clearest class boundaries.")
