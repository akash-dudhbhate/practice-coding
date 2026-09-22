"""
LESSON 16 — REST APIs
MEDIUM P03 — Fetch with Retry
============================================

CONCEPT:
  Networks flake. Retry only on transient failures (5xx, timeouts,
  connection errors) with exponential backoff: wait 1s, 2s, 4s...

PROBLEM:
  Write `fetch_with_retry(url, max_retries=3)` that GETs the url and
  returns response.json(). Retry on timeouts, connection errors, and
  5xx statuses, sleeping 2**attempt seconds between tries. Raise an
  Exception if all retries fail.

TRY THIS INPUT:
  ```python
  data = fetch_with_retry("https://httpbin.org/get")
  print(data["url"])
  ```

EXPECTED OUTPUT:
  ```
  https://httpbin.org/get
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
