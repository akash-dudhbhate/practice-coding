"""
SOLUTION: Palindrome Check (Easy)
=================================
Two pointers at the ends; each skips non-alphanumeric chars; compare
lowercased. O(1) extra space — no cleaned copy.
"""
def is_palindrome(s: str) -> bool:
    L, R = 0, len(s) - 1
    while L < R:
        while L < R and not s[L].isalnum():
            L += 1
        while L < R and not s[R].isalnum():
            R -= 1
        if s[L].lower() != s[R].lower():
            return False
        L += 1
        R -= 1
    return True

if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("0P") is False
    assert is_palindrome("") is True
    print("All tests passed!")
