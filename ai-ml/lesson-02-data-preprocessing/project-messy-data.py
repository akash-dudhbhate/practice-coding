"""
MINI PROJECT — After Lesson 02: Data Preprocessing
====================================================
Clean a Messy Dataset
----------------------

You're given a raw CSV file with these columns:
  - age (some missing, some as strings like "25")
  - income (some missing, some as "50k" strings)
  - city (categorical: Mumbai, Delhi, Bangalore, Chennai)
  - signup_date (string dates like "2024-01-15")
  - is_active (target: 0 or 1)

TASKS:
  1. Load the CSV with pandas
  2. Convert age and income to numeric (handle errors)
  3. Fill missing values appropriately
  4. One-hot encode the city column
  5. Convert signup_date to datetime
  6. Split into X (features) and y (target)
  7. Print the cleaned DataFrame shape and first 5 rows

Create a sample CSV first, then write code to clean it.
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Create a sample messy CSV, then write the cleaning pipeline.
