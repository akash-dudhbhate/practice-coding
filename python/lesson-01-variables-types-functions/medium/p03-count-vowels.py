"""
PROBLEM: Count Vowels (Medium)
==============================

CONCEPT: Strings, loops, counting, conditionals.

# See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG).

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
