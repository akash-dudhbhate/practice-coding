"""
One-Hot Encoding with pd.get_dummies
====================================
Convert a categorical column (color: red/blue/green) into binary indicator
columns using pandas get_dummies. Print the DataFrame before and after.
"""

import pandas as pd


if __name__ == "__main__":
    # Sample dataset with a categorical 'color' column
    data = {
        "id": [1, 2, 3, 4, 5, 6],
        "color": ["red", "blue", "green", "red", "green", "blue"],
        "price": [10.5, 15.0, 12.3, 8.99, 20.0, 14.5],
    }
    df = pd.DataFrame(data)

    print("=== Before one-hot encoding ===")
    print(df)
    print()

    # Apply one-hot encoding on the 'color' column
    # drop_first=False keeps all categories (full dummy encoding)
    df_encoded = pd.get_dummies(df, columns=["color"], prefix="color")

    print("=== After one-hot encoding ===")
    print(df_encoded)
    print()

    # Show the new columns created
    print("New columns:", [c for c in df_encoded.columns if c.startswith("color_")])
