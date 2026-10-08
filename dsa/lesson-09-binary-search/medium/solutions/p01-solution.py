"""
SOLUTION: Integer Square Root via Binary Search (Medium)
============================================
The answer space is [0, x], not an array. The predicate
"mid*mid <= x" is monotone: true...true false...false. Binary
search for the LAST mid where it's true — that's floor(sqrt(x)).
"""
def my_sqrt(x: int) -> int:
    if x < 2:
        return x
    lo, hi = 1, x
    answer = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= x:
            answer = mid     # mid works — look for a bigger one
            lo = mid + 1
        else:
            hi = mid - 1
    return answer

if __name__ == "__main__":
    assert my_sqrt(4) == 2
    assert my_sqrt(8) == 2
    assert my_sqrt(0) == 0
    assert my_sqrt(1) == 1
    assert my_sqrt(15) == 3
    assert my_sqrt(16) == 4
    assert my_sqrt(2147395599) == 46339
    print("All tests passed!")
