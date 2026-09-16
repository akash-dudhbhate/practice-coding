"""
LESSON 14 — Async & Concurrency
MEDIUM P01 — Fetch All Concurrently
============================================

CONCEPT:
  Fan out with gather: build one coroutine per URL and await them
  all at once. asyncio.sleep simulates network delay here.

PROBLEM:
  Write an async `fetch(url)` that sleeps 0.1s and returns
  "Response from {url}", and an async `fetch_all(urls)` that fetches
  every URL concurrently with asyncio.gather and returns the list.

TRY THIS INPUT:
  ```python
  import asyncio
  urls = ["https://a.com", "https://b.com", "https://c.com"]
  print(asyncio.run(fetch_all(urls)))
  ```

EXPECTED OUTPUT:
  ```
  ['Response from https://a.com', 'Response from https://b.com', 'Response from https://c.com']
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
