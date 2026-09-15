"""
SOLUTION: Char Frequency (Hard)
=================================
Return char frequencies for non-space chars, sorted by frequency desc.
"""
def char_frequency(s: str) -> list:
    freq = {}
    for c in s:
        if c != " ":
            freq[c] = freq.get(c, 0) + 1
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))

if __name__ == "__main__":
    assert char_frequency("aab bc") == [("a", 2), ("b", 2), ("c", 1)]
    assert char_frequency("") == []
    print("All tests passed!")
