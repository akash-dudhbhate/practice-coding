"""
SOLUTION: Reverse a List In Place (Easy)
========================================
Swap the ends and walk inward. `while L < R` (not <=) avoids a useless
middle self-swap on odd lengths.
"""
def reverse_in_place(arr: list) -> list:
    L, R = 0, len(arr) - 1
    while L < R:
        arr[L], arr[R] = arr[R], arr[L]
        L += 1
        R -= 1
    return arr

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    reverse_in_place(a)
    assert a == [4, 3, 2, 1]
    b = [1, 2, 3]
    reverse_in_place(b)
    assert b == [3, 2, 1]
    assert reverse_in_place([]) == []
    assert reverse_in_place([5]) == [5]
    print("All tests passed!")
