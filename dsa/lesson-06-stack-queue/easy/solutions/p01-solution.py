"""
SOLUTION: Balanced Brackets (Easy)
==========================================
Push openers; on a closer the stack top must be its match (LIFO =
most recent opener). Stack must end empty. O(n) time, O(n) space.
"""
def is_balanced(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack

if __name__ == "__main__":
    assert is_balanced("{[()]}") == True
    assert is_balanced("([)]") == False
    assert is_balanced("()[]{}") == True
    assert is_balanced("(((") == False
    assert is_balanced("") == True
    assert is_balanced("a(b[c]d)e") == True   # non-brackets ignored
    assert is_balanced(")") == False
    print("All tests passed!")
