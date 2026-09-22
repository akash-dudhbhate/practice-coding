"""
LESSON 14 — Async & Concurrency
MEDIUM P02 — ThreadPoolExecutor
============================================

CONCEPT:
  Threads run blocking calls (like time.sleep or real network I/O)
  concurrently. `executor.map` applies a function to many items
  across a pool of threads.

PROBLEM:
  Write a `download(filename)` function that sleeps 0.2s (simulating
  a download) and returns "Downloaded {filename}". Your script should
  use ThreadPoolExecutor to download 5 files concurrently — the
  check measures that it is fast (concurrent), not 5x0.2s serial.

TRY THIS INPUT:
  ```python
  print(download("file_0.zip"))
  ```

EXPECTED OUTPUT:
  ```
  Downloaded file_0.zip
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
