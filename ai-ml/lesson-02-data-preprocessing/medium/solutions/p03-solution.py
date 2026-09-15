"""
Lesson 02 - Medium P03
Mixed-type column preprocessing: datetime conversion, label encoding, and scaling.

Solution:
  1. Create a DataFrame with mixed types: datetime strings, categorical, numeric.
  2. Convert datetime strings to datetime objects and extract useful features.
  3. Label-encode a categorical column.
  4. Scale numeric columns with StandardScaler.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# ---------------------------------------------------------------------------
# 1. Create sample data with mixed types
# ---------------------------------------------------------------------------
data = {
    "transaction_date": [
        "2023-01-15", "2023-03-22", "2023-06-10",
        "2023-09-05", "2023-12-01", "2023-02-28",
    ],
    "product_category": ["Electronics", "Clothing", "Food", "Electronics", "Food", "Clothing"],
    "amount": [250.50, 45.99, 12.50, 899.99, 30.00, 75.25],
    "quantity": [1, 3, 5, 1, 2, 4],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print(f"\nDtypes:\n{df.dtypes}\n")

# ---------------------------------------------------------------------------
# 2. Convert datetime strings and extract features
# ---------------------------------------------------------------------------
# Solution: Convert string dates to datetime, then extract numeric features
# that an ML model can use.
df["transaction_date"] = pd.to_datetime(df["transaction_date"])
df["year"] = df["transaction_date"].dt.year
df["month"] = df["transaction_date"].dt.month
df["day"] = df["transaction_date"].dt.day
df["day_of_week"] = df["transaction_date"].dt.dayofweek  # 0=Monday
df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)

# Drop the original datetime column (already extracted features)
df = df.drop(columns=["transaction_date"])
print("After datetime conversion and feature extraction:")
print(df)
print()

# ---------------------------------------------------------------------------
# 3. Label-encode the categorical column
# ---------------------------------------------------------------------------
# Solution: LabelEncoder maps each category to an integer. Suitable for ordinal
# categories or when the model can handle arbitrary integer encodings (e.g., trees).
le = LabelEncoder()
df["product_category_encoded"] = le.fit_transform(df["product_category"])
print(f"Category mapping: {dict(zip(le.classes_, le.transform(le.classes_)))}")
df = df.drop(columns=["product_category"])
print("\nAfter label encoding:")
print(df)
print()

# ---------------------------------------------------------------------------
# 4. Scale numeric columns
# ---------------------------------------------------------------------------
# Solution: Scale continuous numeric columns with StandardScaler. Leave
# already-binary/integer-encoded columns as-is if desired; here we scale
# amount and quantity for demonstration.
numeric_to_scale = ["amount", "quantity"]
scaler = StandardScaler()
df[numeric_to_scale] = scaler.fit_transform(df[numeric_to_scale])

print("After scaling numeric columns:")
print(df)
print(f"\nScaled column means: {df[numeric_to_scale].mean().values}")
print(f"Scaled column stds:  {df[numeric_to_scale].std().values}")
