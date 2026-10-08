"""
SOLUTION: First Unique Character (Easy)
=======================================
Pass 1 counts every character; pass 2 returns the index of the first
character with count 1. The second pass over the string (in order) is
what finds the FIRST unique — the dict itself has no order-of-arrival
information for equal keys.
"""
def first_unique_char(s: str) -> int:
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for i, c in enumerate(s):
        if freq[c] == 1:
            return i
    return -1

if __name__ == "__main__":
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1
    assert first_unique_char("") == -1
    assert first_unique_char("z") == 0
    print("All tests passed!")
