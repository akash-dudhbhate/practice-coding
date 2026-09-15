"""SOLUTION: is_palindrome with tests (Easy)"""
import pytest

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Tests
def test_palindrome_normal():
    assert is_palindrome("racecar") == True

def test_palindrome_empty():
    assert is_palindrome("") == True

def test_palindrome_case_insensitive():
    assert is_palindrome("RaceCar") == True

if __name__ == "__main__":
    test_palindrome_normal()
    test_palindrome_empty()
    test_palindrome_case_insensitive()
    print("All tests passed!")
