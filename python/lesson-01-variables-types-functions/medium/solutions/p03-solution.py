"""
SOLUTION: Count Vowels (Medium)
================================
Count vowels in a string (case-insensitive).
"""
def count_vowels(text: str) -> int:
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    assert count_vowels("") == 0
    print("All tests passed!")
