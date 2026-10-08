"""
SOLUTION: Growth Rates (Easy)
==============================
Real numbers for each Big-O class at size n.
"""
import math

def growth_values(n: int) -> dict:
    lg = int(math.log2(n))
    return {
        "O(1)": 1,
        "O(log n)": lg,
        "O(n)": n,
        "O(n log n)": n * lg,
        "O(n^2)": n * n,
        "O(2^n)": 2 ** n,
    }

if __name__ == "__main__":
    expected = {"O(1)": 1, "O(log n)": 3, "O(n)": 8,
                "O(n log n)": 24, "O(n^2)": 64, "O(2^n)": 256}
    assert growth_values(8) == expected
    assert growth_values(16)["O(n^2)"] == 256
    assert growth_values(16)["O(2^n)"] == 65536
    print("All tests passed!")
