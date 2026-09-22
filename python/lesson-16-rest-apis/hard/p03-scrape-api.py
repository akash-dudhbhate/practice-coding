"""
LESSON 16 — REST APIs
HARD P03 — Scrape API (pagination + rate limit)
============================================

CONCEPT:
  Polite scraping = pagination + pacing. Sleep between requests, and
  when a 429 arrives, wait the server's `Retry-After` seconds before
  continuing.

PROBLEM:
  Write `scrape_api(base_url, endpoint, rate_limit=0.5)` that fetches
  `{base_url}/{endpoint}` with page/per_page=100 params, accumulates
  all items until a page returns fewer than 100, sleeps `rate_limit`
  between pages, and on HTTP 429 sleeps the Retry-After header value
  then retries. Returns the full list.

TRY THIS INPUT:
  ```python
  results = scrape_api("https://api.github.com", "users/torvalds/repos")
  print(len(results))
  ```

EXPECTED OUTPUT:
  ```
  <total items>
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
