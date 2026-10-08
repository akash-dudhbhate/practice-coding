"""
SOLUTION: Countdown (Easy)
==============================
Contract: returns list [n..1]. Base: n == 0 -> []. Each level prepends
its n onto the deeper list — the base's [] is the tail everyone glues to.
"""
def countdown(n: int) -> list:
    if n == 0:
        return []
    return [n] + countdown(n - 1)

if __name__ == "__main__":
    assert countdown(5) == [5, 4, 3, 2, 1]
    assert countdown(1) == [1]
    assert countdown(0) == []
    assert countdown(3) == [3, 2, 1]
    print("All tests passed!")
