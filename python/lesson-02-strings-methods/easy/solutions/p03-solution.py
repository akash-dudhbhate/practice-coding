"""
SOLUTION: Palindrome Check (Easy)
==================================
Check if a string reads the same forwards and backwards.
"""
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A Santa at NASA") == True
    assert is_palindrome("") == True
    print("All tests passed!")
