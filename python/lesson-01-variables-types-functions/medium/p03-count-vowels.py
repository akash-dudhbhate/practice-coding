"""
LESSON 01 — Variables, Types & Functions
MEDIUM P03 — Count Vowels
============================================

CONCEPT:
  A string is a sequence of characters, so a `for` loop visits each
  character one at a time. Keep a counter variable, add 1 whenever the
  character is a vowel, and return the counter at the end — this
  "loop and accumulate" pattern shows up everywhere.

PROBLEM:
  Write a function `count_vowels(text: str) -> int` that returns the
  number of vowels (a, e, i, o, u) in `text`. The count must be
  case-insensitive, so 'A' counts just like 'a'.

# TODO: Write your complete solution from scratch below (function signature + body).
#       Remove this TODO line when done.
"""



# count = 0
# for char in "hello":
#     if char == "l":
#         count += 1     
# print(count) 


count=0
word="madhuri"
vowels=("a,e,i,o,u")
for char in word:
    if char in vowels:
        count += 1
    
print(count)

# output=3
