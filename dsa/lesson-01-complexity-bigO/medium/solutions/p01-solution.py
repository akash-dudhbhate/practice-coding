"""
SOLUTION: Nested Pairs Count (Medium)
==============================
for i in range(n): for j in range(i+1, n) runs
(n-1) + (n-2) + ... + 1 + 0 = n*(n-1)/2 times -> still O(n^2).
"""
def count_pair_ops(n: int) -> int:
    return n * (n - 1) // 2

if __name__ == "__main__":
    assert count_pair_ops(5) == 10
    assert count_pair_ops(4) == 6
    assert count_pair_ops(1) == 0
    assert count_pair_ops(10) == 45
    print("All tests passed!")
