"""
LESSON 15 — Testing with pytest
HARD P01 — BankAccount Test Suite
============================================

CONCEPT:
  A test suite combines fixtures (shared setup) with parametrize
  (input tables) and pytest.raises (error paths) to cover a class
  thoroughly.

PROBLEM:
  Write a `BankAccount` class (`__init__(owner, balance=0)`,
  `deposit`, `withdraw` — both raise ValueError on invalid input)
  AND a test suite covering: deposit, withdraw, insufficient funds,
  negative deposit — using an `account` fixture and parametrize for
  several valid deposit amounts.

TRY THIS INPUT:
  ```python
  acc = BankAccount("Test", 100)
  acc.deposit(50)
  print(acc.balance)
  ```

EXPECTED OUTPUT:
  ```
  150
  ```

RUN TESTS: pytest <this file> -v
CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
