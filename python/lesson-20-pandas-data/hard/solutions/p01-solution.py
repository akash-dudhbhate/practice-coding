"""SOLUTION: Student grades analysis (Hard)"""
import pandas as pd
import numpy as np
import random

def get_grade(avg):
    if avg >= 90: return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else: return "F"

def main():
    random.seed(42)
    names = [f"Student{i}" for i in range(100)]
    math = [random.randint(40, 100) for _ in range(100)]
    science = [random.randint(40, 100) for _ in range(100)]
    english = [random.randint(40, 100) for _ in range(100)]

    df = pd.DataFrame({"name": names, "math": math, "science": science, "english": english})
    df["average"] = df[["math", "science", "english"]].mean(axis=1)
    df["grade"] = df["average"].apply(get_grade)

    print("Class average per subject:")
    print(df[["math", "science", "english"]].mean())

    print("\nTop 5 students:")
    print(df.nlargest(5, "average")[["name", "average", "grade"]])

    pass_count = (df["average"] >= 60).sum()
    fail_count = (df["average"] < 60).sum()
    print(f"\nPass: {pass_count}, Fail: {fail_count}")

    df.to_csv("student_results.csv", index=False)
    print("\nExported to student_results.csv")

if __name__ == "__main__":
    main()
