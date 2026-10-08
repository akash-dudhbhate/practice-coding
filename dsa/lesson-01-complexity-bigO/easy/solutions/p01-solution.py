"""
SOLUTION: Count Loop Ops (Easy)
==============================
A loop `for i in range(n)` executes its body exactly n times -> O(n).
"""
def count_ops(n: int) -> int:
    return n  # the loop body runs once per i in range(n)

if __name__ == "__main__":
    assert count_ops(10) == 10
    assert count_ops(0) == 0
    assert count_ops(1000) == 1000
    print("All tests passed!")
