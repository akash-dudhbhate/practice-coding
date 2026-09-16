"""
LESSON 15 — Testing with pytest
MEDIUM P02 — Fixture with yield (setup/teardown)
============================================

CONCEPT:
  A fixture that `yield`s a value runs cleanup code after the test
  finishes — the part after yield is teardown, like finally.

PROBLEM:
  Write a fixture `temp_file` that creates a temporary file
  containing "test content", yields its path, and deletes the file
  after the test. Then write `test_read_temp_file` that reads the
  file and asserts the contents.

TRY THIS INPUT:
  ```python
  # def test_read_temp_file(temp_file):
  #     with open(temp_file) as f:
  #         assert f.read() == "test content"
  ```

EXPECTED OUTPUT:
  ```
  (pytest: 1 passed)
  ```

RUN TESTS: pytest <this file> -v
CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
