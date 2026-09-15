"""
SOLUTION: Anagram Check (Hard)
================================
Check if two strings are anagrams (same characters, different order).
"""
def is_anagram(s1: str, s2: str) -> bool:
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "world") == False
    assert is_anagram("Dormitory", "Dirty room") == True
    print("All tests passed!")
