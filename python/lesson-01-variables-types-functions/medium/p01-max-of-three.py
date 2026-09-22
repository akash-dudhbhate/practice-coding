"""
LESSON 01 — Variables, Types & Functions
MEDIUM P01 — Max of Three Numbers
============================================

CONCEPT:
  Functions can call other functions — that's how big programs are
  built from small pieces. If you already have max_of_two(a, b), the
  max of three numbers is just max_of_two(max_of_two(a, b), c):
  first find the bigger of a and b, then compare that with c.

PROBLEM:
  Write a function `max_of_three(a: int, b: int, c: int) -> int` that
  returns the largest of the three integers. Write your own max_of_two
  helper in this file and reuse it — do NOT use the built-in max().

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
                   
                   
