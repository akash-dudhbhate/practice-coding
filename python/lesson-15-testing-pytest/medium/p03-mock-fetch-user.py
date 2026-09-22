"""
LESSON 15 — Testing with pytest
MEDIUM P03 — Mock an API Call
============================================

CONCEPT:
  `unittest.mock.patch` replaces a real function (like
  `requests.get`) with a fake you control — tests stay fast and need
  no network.

PROBLEM:
  Write a function `fetch_user(user_id)` that calls
  `requests.get(f"https://api.example.com/users/{user_id}")` and
  returns `resp.json()`. Then write `test_fetch_user` that patches
  `requests.get` so no real HTTP request happens, and asserts the
  returned dict's data.

TRY THIS INPUT:
  ```python
  # inside the test:
  # mock_resp.json.return_value = {"id": 1, "name": "Akash"}
  # assert fetch_user(1)["name"] == "Akash"
  ```

EXPECTED OUTPUT:
  ```
  (pytest: 1 passed)
  ```

RUN TESTS: pytest <this file> -v
CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
