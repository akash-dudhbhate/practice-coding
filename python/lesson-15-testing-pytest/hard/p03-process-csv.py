"""
LESSON 15 — Testing with pytest
HARD P03 — process_csv with Tests
============================================

CONCEPT:
  File-handling code is testable: a fixture writes a temp CSV,
  yields the path, and cleans up — the test just calls the function.

PROBLEM:
  Write `process_csv(filepath)` that reads a CSV with csv.DictReader
  and returns a list of dicts. Write tests using a `temp_csv`
  fixture covering: normal reading (2 rows), an empty file, and a
  malformed/edge-case file.

TRY THIS INPUT:
  ```python
  # CSV: name,age \\n Akash,25 \\n Dev,30
  print(process_csv("people.csv"))
  ```

EXPECTED OUTPUT:
  ```
  [{'name': 'Akash', 'age': '25'}, {'name': 'Dev', 'age': '30'}]
  ```

RUN TESTS: pytest <this file> -v
CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
