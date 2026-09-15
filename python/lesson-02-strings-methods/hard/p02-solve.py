"""
PROBLEM: Run-Length Encoding (Hard)
=====================================

CONCEPT: String building, loops, counting pattern, edge cases.

# See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG).

Write a function `compress(text)` that performs basic run-length encoding.
For each group of consecutive identical characters, output the character
followed by the count.

Examples:
    compress("aaabbc") -> "a3b2c1"
    compress("abc")    -> "a1b1c1"
    compress("")       -> ""
    compress("aaaa")   -> "a4"
    compress("aabbb")  -> "a2b3"

Hint: Loop through the string, count consecutive identical characters,
and build the result string as you go.

"""

# TODO: Write your complete solution from scratch below (function signature + body).
#       Remove this TODO line when done.
