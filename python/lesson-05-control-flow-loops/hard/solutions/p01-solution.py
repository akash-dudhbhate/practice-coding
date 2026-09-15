"""
SOLUTION: Is Palindrome (Hard)
================================
Check if s reads the same forwards and backwards using two pointers.
"""
def is_palindrome(s: str) -> bool:
    s = s.lower()
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    print("All tests passed!")
