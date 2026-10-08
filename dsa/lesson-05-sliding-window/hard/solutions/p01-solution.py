"""
SOLUTION: Minimum Window Substring (Hard)
==========================================
need = counts required by t. window = counts in current window.
formed = how many required chars have window[c] == need[c].
Expand until formed == len(need), then shrink while still valid,
recording the best (smallest) window. O(len(s) + len(t)).
"""
def min_window(s, t):
    if not s or not t or len(t) > len(s):
        return ""
    need = {}
    for c in t:
        need[c] = need.get(c, 0) + 1

    window = {}
    formed = 0                  # chars whose window count reached need count
    required = len(need)
    left = 0
    best_len, best_left = float("inf"), 0

    for right, c in enumerate(s):
        window[c] = window.get(c, 0) + 1
        if c in need and window[c] == need[c]:
            formed += 1
        while formed == required:             # window covers t → squeeze it
            if right - left + 1 < best_len:
                best_len = right - left + 1
                best_left = left
            d = s[left]
            window[d] -= 1
            if d in need and window[d] < need[d]:
                formed -= 1                   # lost a required char
            left += 1
    return "" if best_len == float("inf") else s[best_left:best_left + best_len]

if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("ab", "b") == "b"
    assert min_window("aa", "aa") == "aa"        # multiplicity matters
    assert min_window("bba", "ab") == "ba"
    print("All tests passed!")
