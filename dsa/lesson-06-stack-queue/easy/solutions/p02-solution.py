"""
SOLUTION: Reverse a String With a Stack (Easy)
==========================================
Push all chars (LIFO), pop them all → reversed. O(n) time/space.
"""
def reverse_with_stack(s):
    stack = []
    for c in s:
        stack.append(c)          # push left to right
    out = []
    while stack:
        out.append(stack.pop())  # pop right to left
    return "".join(out)

if __name__ == "__main__":
    assert reverse_with_stack("hello") == "olleh"
    assert reverse_with_stack("abc") == "cba"
    assert reverse_with_stack("") == ""
    assert reverse_with_stack("racecar") == "racecar"
    assert reverse_with_stack("a") == "a"
    print("All tests passed!")
