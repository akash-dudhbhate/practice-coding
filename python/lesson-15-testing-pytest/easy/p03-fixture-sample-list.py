"""
LESSON 15 — Testing with pytest
EASY P03 — Fixture: sample_list
============================================

CONCEPT:
  A `@pytest.fixture` function provides test data. Any test that
  names the fixture as a parameter receives its return value.

PROBLEM:
  Write a fixture `sample_list` returning [3, 1, 4, 1, 5], then two
  tests using it: `test_max` asserting max() == 5 and `test_len`
  asserting len() == 5.

TRY THIS INPUT:
  ```python
  # pytest will inject the fixture:
  # def test_max(sample_list):
  #     assert max(sample_list) == 5
  ```

EXPECTED OUTPUT:
  ```
  (pytest: 2 passed)
  ```

RUN TESTS: pytest <this file> -v
CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
