"""
PROBLEM: Reverse String (Easy)
================================

CONCEPT: String building, loops, string immutability.

# See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG).

Write a function `reverse_string(text)` that takes a string and returns
the reversed version. Do NOT use slicing (`s[::-1]`) or `reversed()`.

Instead, build the reversed string by looping through the characters
from the end to the beginning.

Examples:
    reverse_string("hello") -> "olleh"
    reverse_string("")      -> ""
    reverse_string("a")     -> "a"

"""
def reverse_string(text):
    reversed_text = ""

    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]

    return reversed_text

print(reverse_string("hello"))