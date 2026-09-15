"""
SOLUTION: Count Vowels (Easy)
==============================
Count vowels in a string (case-insensitive).
"""
def count_vowels(text: str) -> int:
    vowels = set("aeiou")
    return sum(1 for c in text.lower() if c in vowels)

if __name__ == "__main__":
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    print("All tests passed!")
