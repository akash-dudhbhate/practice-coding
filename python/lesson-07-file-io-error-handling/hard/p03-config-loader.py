"""
LESSON 07 — File I/O & Error Handling
HARD P03 — Config Loader
============================================

CONCEPT:
  Wrap low-level errors (missing file, bad JSON) in one
  domain-specific error so callers have a single thing to catch.

PROBLEM:
  Define `class ConfigError(Exception)` and a function
  `config_loader(path)` that reads a JSON config file and returns
  the dict. Rules:
    - Missing file or invalid JSON → raise ConfigError with a
      helpful message.
    - If the parsed config has no "host" key → raise ConfigError.

TRY THIS INPUT:
  ```python
  # file contains: {"host": "localhost", "port": 8080}
  cfg = config_loader("cfg.json")
  print(cfg["host"])
  ```

EXPECTED OUTPUT:
  ```
  localhost
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
