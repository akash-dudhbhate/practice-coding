"""
SOLUTION: Identify Big-O (Easy)
==============================
Watch what doubling n does to the op count:
flat -> O(1), +1 per doubling -> O(log n), x2 -> O(n),
x4 -> O(n^2), squared -> O(2^n).
"""
def classify_growth(ops_n: int, ops_2n: int, ops_4n: int) -> str:
    if ops_n == ops_2n == ops_4n:
        return "O(1)"
    if ops_2n - ops_n == 1 and ops_4n - ops_2n == 1:
        return "O(log n)"
    if ops_2n == 2 * ops_n and ops_4n == 2 * ops_2n:
        return "O(n)"
    if ops_2n == 4 * ops_n and ops_4n == 4 * ops_2n:
        return "O(n^2)"
    if ops_2n == ops_n * ops_n and ops_4n == ops_2n * ops_2n:
        return "O(2^n)"
    return "unknown"

if __name__ == "__main__":
    assert classify_growth(7, 7, 7) == "O(1)"
    assert classify_growth(10, 11, 12) == "O(log n)"
    assert classify_growth(50, 100, 200) == "O(n)"
    assert classify_growth(25, 100, 400) == "O(n^2)"
    assert classify_growth(8, 64, 4096) == "O(2^n)"
    print("All tests passed!")
