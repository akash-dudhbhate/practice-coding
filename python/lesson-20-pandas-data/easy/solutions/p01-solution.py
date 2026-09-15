"""SOLUTION: Create DataFrame and inspect (Easy)"""
import pandas as pd

def main():
    data = {
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "age": [25, 30, 35, 28, 22],
        "city": ["Mumbai", "Delhi", "Bangalore", "Mumbai", "Pune"]
    }
    df = pd.DataFrame(data)
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"First 3 rows:\n{df.head(3)}")

if __name__ == "__main__":
    main()
