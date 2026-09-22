"""
PROBLEM: Count Vowels (Easy)
=============================

CONCEPT: String iteration, .lower(), membership check (in).

# See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG).

Write a function `count_vowels(text)` that takes a string and returns
the number of vowels (a, e, i, o, u) in it. The check should be
case-insensitive (count both upper and lower case).

Examples:
    count_vowels("hello")    -> 2  (e, o)
    count_vowels("AEIOU")    -> 5
    count_vowels("rhythm")   -> 0
    count_vowels("")         -> 0

"""

def count_vowels(text):
    count = 0

    for char in text:
        char = char.lower()

        if char in "aeiou":
            count += 1

    return count

print(count_vowels("hello"))