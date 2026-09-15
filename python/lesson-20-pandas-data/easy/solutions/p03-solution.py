"""SOLUTION: Fill NaN values (Easy)"""
import pandas as pd
import numpy as np

def main():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Diana"],
        "age": [25, np.nan, 35, np.nan],
        "city": ["Mumbai", np.nan, "Delhi", "Pune"]
    })
    print("Before:\n", df)
    df["age"] = df["age"].fillna(df["age"].mean())
    df["city"] = df["city"].fillna("Unknown")
    print("\nAfter:\n", df)

if __name__ == "__main__":
    main()
