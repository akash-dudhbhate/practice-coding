"""
SOLUTION: Two-Pass Encode (Hard)
==============================
Pass 1: count each character (dict preserves first-appearance order).
Pass 2: join "<char><count>" pieces — never += in a loop.
"""
def encode_with_freq(text: str) -> str:
    freq = {}
    for c in text:                 # pass 1: tally
        freq[c] = freq.get(c, 0) + 1
    return "".join(f"{c}{n}" for c, n in freq.items())  # pass 2: build

if __name__ == "__main__":
    assert encode_with_freq("aabca") == "a3b1c1"
    assert encode_with_freq("zzz") == "z3"
    assert encode_with_freq("ab") == "a1b1"
    assert encode_with_freq("") == ""
    print("All tests passed!")
