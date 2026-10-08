"""
LESSON 06 — Stacks & Queues
MEDIUM P03 — Evaluate Postfix (Reverse Polish Notation)
============================================

CONCEPT:
  RPN writes operators AFTER their operands: "3 4 +" means 3 + 4.
  Perfect stack job — push numbers; on an operator, pop the top TWO,
  apply, push the result. Watch operand order: for "a b -" the
  computation is a - b (b is popped first, it's the RIGHT operand).

PROBLEM:
  Write a function `eval_rpn(tokens: list[str]) -> int` that evaluates
  a Reverse Polish Notation expression. tokens contain integers (as
  strings) and operators + - * /. Division truncates toward zero
  (use int(a / b), not //, for negatives).

TRY THIS INPUT:
  ```python
  print(eval_rpn(["2", "1", "+", "3", "*"]))
  print(eval_rpn(["4", "13", "5", "/", "+"]))
  print(eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
  print(eval_rpn(["5"]))
  ```

EXPECTED OUTPUT:
  ```
  9
  6
  22
  5
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
