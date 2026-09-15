"""SOLUTION: Apply with custom function (Medium)"""
import pandas as pd
import os

def categorize(age):
    if age < 20: return "teen"
    elif age <= 60: return "adult"
    else: return "senior"

def main():
    csv_path = "people.csv"
    if not os.path.exists(csv_path):
        pd.DataFrame({
            "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
            "age": [18, 35, 65, 25, 70]
        }).to_csv(csv_path, index=False)

    df = pd.read_csv(csv_path)
    df["category"] = df["age"].apply(categorize)
    df.to_csv("people_categorized.csv", index=False)
    print(df)

if __name__ == "__main__":
    main()
