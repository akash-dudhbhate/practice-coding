"""SOLUTION: string_utils module (Easy)"""
# This file acts as both the module and the test script

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

if __name__ == "__main__":
    assert reverse_string("hello") == "olleh"
    assert count_vowels("hello") == 2
    print("All tests passed!")
