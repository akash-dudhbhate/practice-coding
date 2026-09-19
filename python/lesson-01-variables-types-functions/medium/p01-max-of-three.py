"""
PROBLEM: Max of Three (Medium)
==============================

CONCEPT: Reuse logic from easy/p01-max-of-two. Functions calling functions.

# See concepts.md in this lesson folder for detailed explanations (WHY/WHERE/WHAT-GOES-WRONG).

# TODO: Write your complete solution from scratch below (function signature + body).
#       Remove this TODO line when done.
"""


a=10
b=30
c=3
        
# def max_of_three(a,b,c):
#     if a> b  and a>c :
#         print("a is greater")
#     elif b> a  and b>c :
#         print("b is greater")
#     elif c> a and c>b :
#         print("c is greater")
    
# (max_of_three(a,b,c)) 

# output: b is greater
                   
                   
                   
def max_of_three(a,b,c):
    if a> b  and a>c :
        print("a is greater")
    elif b> a  and b>c :
        print("b is greater")
    elif c> a and c>b :
        print("c is greater")
    
print(max_of_three(a,b,c)) 

# # output: b is greater
# also return none automatically bcoz print statement
                   
                   