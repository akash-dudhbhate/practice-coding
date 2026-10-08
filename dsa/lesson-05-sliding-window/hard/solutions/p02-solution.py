"""
SOLUTION: Longest Substring With At Most K Distinct Characters (Hard)
==========================================
Variable window, invalid when len(count) > k. Delete zero-count keys
so len(count) stays honest → O(n).
"""
def length_of_longest_k_distinct(s, k):
    if k == 0 or not s:
        return 0
    left, best, count = 0, 0, {}
    for right, c in enumerate(s):
        count[c] = count.get(c, 0) + 1          # enter
        while len(count) > k:                   # too many distinct → shrink
            d = s[left]
            count[d] -= 1
            if count[d] == 0:
                del count[d]                    # keep len(count) truthful
            left += 1
        best = max(best, right - left + 1)
    return best

if __name__ == "__main__":
    assert length_of_longest_k_distinct("eceba", 2) == 3
    assert length_of_longest_k_distinct("aa", 1) == 2
    assert length_of_longest_k_distinct("abcadcacacaca", 3) == 11
    assert length_of_longest_k_distinct("aabbcc", 2) == 4
    assert length_of_longest_k_distinct("", 2) == 0
    assert length_of_longest_k_distinct("abc", 0) == 0
    print("All tests passed!")
