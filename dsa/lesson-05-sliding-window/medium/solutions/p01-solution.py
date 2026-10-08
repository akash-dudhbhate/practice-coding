"""
SOLUTION: Longest Substring Without Repeating Characters (Medium)
==========================================
Variable window. last[c] = most recent index of c. When s[right] was
last seen inside the window, jump left past it. Each index enters
and leaves once → O(n).
"""
def length_of_longest_substring(s):
    last = {}          # char -> most recent index
    left, best = 0, 0
    for right, c in enumerate(s):
        if c in last and last[c] >= left:
            left = last[c] + 1          # shrink: jump past the old occurrence
        last[c] = right                 # enter: record latest index
        best = max(best, right - left + 1)
    return best

if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("dvdf") == 3   # stale-index trap
    assert length_of_longest_substring("abba") == 2   # left must not move backward
    print("All tests passed!")
