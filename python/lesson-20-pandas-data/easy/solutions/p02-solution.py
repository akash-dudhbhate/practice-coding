"""SOLUTION: Load CSV and filter (Easy)"""
import pandas as pd
import os

def main():
    csv_path = "sample.csv"
    if not os.path.exists(csv_path):
        pd.DataFrame({
            "name": ["Alice", "Bob", "Charlie", "Diana"],
            "age": [25, 30, 22, 28],
            "city": ["Mumbai", "Delhi", "Mumbai", "Mumbai"]
        }).to_csv(csv_path, index=False)

    df = pd.read_csv(csv_path)
    filtered = df[(df["age"] > 25) & (df["city"] == "Mumbai")]
    print(filtered)

if __name__ == "__main__":
    main()
