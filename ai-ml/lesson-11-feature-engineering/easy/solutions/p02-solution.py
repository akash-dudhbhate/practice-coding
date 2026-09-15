"""
StandardScaler on DataFrame with Different Scales
==================================================
Apply StandardScaler to columns with very different ranges (age: 20-80,
income: 20000-200000). Print before/after and verify mean=0, std=1.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


if __name__ == "__main__":
    # DataFrame with columns on very different scales
    data = {
        "age": [25, 30, 45, 50, 35, 60, 80, 20, 55, 40],
        "income": [30000, 45000, 80000, 120000, 50000, 200000, 150000, 25000, 90000, 60000],
    }
    df = pd.DataFrame(data)

    print("=== Before scaling ===")
    print(df)
    print(f"Age mean:    {df['age'].mean():.2f}, std: {df['age'].std():.2f}")
    print(f"Income mean: {df['income'].mean():.2f}, std: {df['income'].std():.2f}")
    print()

    # Apply StandardScaler: z = (x - mean) / std
    scaler = StandardScaler()
    scaled_array = scaler.fit_transform(df)
    df_scaled = pd.DataFrame(scaled_array, columns=df.columns)

    print("=== After scaling ===")
    print(df_scaled)
    print()

    # Verify mean ~ 0 and std ~ 1 for each column
    for col in df_scaled.columns:
        print(f"{col}: mean={df_scaled[col].mean():.6f}, std={df_scaled[col].std():.6f}")

    print()
    # Show the learned scaler parameters
    print(f"Scaler means:  {scaler.mean_}")
    print(f"Scaler stds:   {scaler.scale_}")
