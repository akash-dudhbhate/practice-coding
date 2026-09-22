"""
LESSON 14 — Async & Concurrency
HARD P02 — Async Scraper with Timeout
============================================

CONCEPT:
  `asyncio.wait_for(coro, timeout)` cancels the coroutine if it runs
  too long, raising TimeoutError — catch it so one slow URL doesn't
  sink the batch.

PROBLEM:
  Write an async `fetch_with_timeout(url, timeout=5)` that awaits a
  simulated fetch (asyncio.sleep(0.1) wrapped in wait_for) returning
  "OK: {url}", or "TIMEOUT: {url}" on TimeoutError. Then an async
  `scrape_all(urls)` that gathers results for all URLs.

TRY THIS INPUT:
  ```python
  import asyncio
  urls = [f"https://api{i}.example.com" for i in range(5)]
  print(asyncio.run(scrape_all(urls)))
  ```

EXPECTED OUTPUT:
  ```
  ['OK: https://api0.example.com', 'OK: https://api1.example.com', 'OK: https://api2.example.com', 'OK: https://api3.example.com', 'OK: https://api4.example.com']
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
