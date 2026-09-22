"""SOLUTION: Data cleaning pipeline (Hard)"""
import pandas as pd
import os

def main():
    messy_path = "messy.csv"
    if not os.path.exists(messy_path):
        pd.DataFrame({
            "name": ["  Alice  ", "Bob", "Charlie", "Alice", "Diana"],
            "age": ["25", "30", "nan", "25", "abc"],
            "email": ["alice@e.com", "bob@e.com", "", "alice@e.com", "diana@e.com"],
            "salary": ["50000", "60000", "55000", "50000", ""]
        }).to_csv(messy_path, index=False)

    df = pd.read_csv(messy_path)
    print("Original:\n", df)

    # Strip whitespace from string columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    # Fix types
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

    # Drop duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df["age"] = df["age"].fillna(df["age"].mean())
    df["salary"] = df["salary"].fillna(df["salary"].median())
    df["email"] = df["email"].replace("", "unknown@e.com").fillna("unknown@e.com")

    print("\nCleaned:\n", df)
    df.to_csv("clean_data.csv", index=False)
    print("\nExported to clean_data.csv")

if __name__ == "__main__":
    main()
