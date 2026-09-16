"""
LESSON 06 — Functions Deep Dive
HARD P03 — Build Profile + Format
============================================

CONCEPT:
  `**kwargs` builds a dict from keyword arguments, and `**dict`
  unpacks a dict back into keyword-style entries. Together they make
  flexible record builders.

PROBLEM:
  Write TWO functions:
    - `build_profile(name, **info)` — returns a dict containing the
      key "name" plus every key/value from `info`.
    - `format_profile(profile)` — returns a string like
      "name (key1=val1, key2=val2)" using the dict from build_profile.

TRY THIS INPUT:
  ```python
  p = build_profile("Akash", role="dev", level=5)
  print(p["name"], p["role"])
  print(format_profile(p))
  ```

EXPECTED OUTPUT:
  ```
  Akash dev
  Akash (role=dev, level=5)
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
