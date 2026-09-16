"""Level 02 — Python for ML — Medium P02 Solution"""

import numpy as np

def detect_outliers(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = data[(data < lower) | (data > upper)]
    cleaned = np.clip(data, lower, upper)
    return cleaned, len(outliers)

if __name__ == "__main__":
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
    cleaned, n = detect_outliers(data)
    print(f"Outliers: {n}")
    print(f"Cleaned: {cleaned}")
