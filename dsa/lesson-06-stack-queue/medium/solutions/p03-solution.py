"""
SOLUTION: Evaluate Postfix / RPN (Medium)
==========================================
Push operands; on an operator pop TWO — the second pop is the LEFT
operand (order matters for - and /). Push result back. One pass, O(n).
Division truncates toward zero → int(a / b).
"""
def eval_rpn(tokens):
    stack = []
    for tok in tokens:
        if tok in "+-*/":
            b = stack.pop()             # right operand (pushed last)
            a = stack.pop()             # left operand
            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)     # NOT b - a
            elif tok == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))  # truncates toward zero
        else:
            stack.append(int(tok))
    return stack[-1]

if __name__ == "__main__":
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
    assert eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
    assert eval_rpn(["5"]) == 5
    assert eval_rpn(["3", "4", "-"]) == -1       # operand order matters
    assert eval_rpn(["7", "2", "/"]) == 3
    assert eval_rpn(["-7", "2", "/"]) == -3      # toward zero, not floor
    print("All tests passed!")
