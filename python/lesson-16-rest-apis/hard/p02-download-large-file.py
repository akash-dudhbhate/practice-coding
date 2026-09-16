"""
LESSON 16 — REST APIs
HARD P02 — Download Large File
============================================

CONCEPT:
  `stream=True` + `response.iter_content(chunk_size)` downloads in
  pieces so a huge file never sits fully in memory. Sum chunk sizes
  for progress.

PROBLEM:
  Write `download_large_file(url, filepath)` that streams a download
  to disk in chunks, prints byte progress, and returns the filepath.
  Handle network errors (connection error, timeout) cleanly.

TRY THIS INPUT:
  ```python
  path = download_large_file("https://example.com/big.zip", "/tmp/big.zip")
  print(path)
  ```

EXPECTED OUTPUT:
  ```
  Downloaded: ... bytes
  Done! Saved to /tmp/big.zip
  /tmp/big.zip
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
