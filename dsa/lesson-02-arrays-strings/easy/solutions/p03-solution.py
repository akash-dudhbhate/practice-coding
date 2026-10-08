"""
SOLUTION: Char Frequency (Easy)
==============================
One scan, one dict tally -> O(n). dict.get(c, 0) handles first sightings.
"""
def char_freq(text: str) -> dict:
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1
    return freq

if __name__ == "__main__":
    assert char_freq("aab") == {"a": 2, "b": 1}
    assert char_freq("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert char_freq("") == {}
    assert char_freq("Aa") == {"A": 1, "a": 1}
    print("All tests passed!")
