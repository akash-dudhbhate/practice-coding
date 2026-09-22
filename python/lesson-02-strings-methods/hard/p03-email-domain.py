"""
LESSON 02 — Strings & String Methods
HARD P03 — Extract Email Domain
============================================

CONCEPT:
  .split("@") cuts an email address at the @ sign, giving [user, domain].
  Checking `"@" in email` first guards against malformed input — a good
  habit whenever you index into a split result.

PROBLEM:
  Write a function `extract_domain(email: str) -> str` that returns the
  part after the @ sign. "user@gmail.com" -> "gmail.com". If there's no
  @ in the string, return "".

TRY THIS INPUT:
  ```python
  print(extract_domain("user@gmail.com"))
  print(extract_domain("test@company.co.uk"))
  print(extract_domain("noatsign"))
  ```

EXPECTED OUTPUT:
  ```
  gmail.com
  company.co.uk

  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
