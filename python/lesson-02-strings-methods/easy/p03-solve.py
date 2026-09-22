"""
PROBLEM: Palindrome Check (Easy)
==================================

CONCEPT: String comparison, .lower(), .strip(), slicing or loops.

# See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG).

Write a function `is_palindrome(text)` that returns True if the string
is a palindrome (reads the same forwards and backwards), False otherwise.

The check should be case-insensitive. An empty string is a palindrome.

Examples:
    is_palindrome("racecar") -> True
    is_palindrome("hello")   -> False
    is_palindrome("")        -> True
    is_palindrome("Aa")      -> True  (case-insensitive)

"""

def is_palindrome(text):
    text = text.lower()

    return text == text[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("Aa"))