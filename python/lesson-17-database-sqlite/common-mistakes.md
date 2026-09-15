# Lesson 17 — Common Mistakes

## Mistake 01: No timeout
```python
# WRONG — can hang forever
requests.get(url)

# CORRECT
requests.get(url, timeout=10)
```

## Mistake 02: Not handling errors
```python
# WRONG — crashes on error
data = requests.get(url).json()

# CORRECT
try:
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    data = r.json()
except requests.RequestException as e:
    log.error(e)
```

## Mistake 03: Scraping too fast
```python
# WRONG — gets IP banned
for url in urls:
    requests.get(url)

# CORRECT — be polite
import time
for url in urls:
    requests.get(url)
    time.sleep(1)
```

## Mistake 04: Hardcoded API keys
```python
# WRONG — key in source code
API_KEY = "abc123"

# CORRECT — use environment variables
import os
API_KEY = os.environ["API_KEY"]
```

## Mistake 05: Not respecting robots.txt
```python
# Always check robots.txt before scraping
# https://example.com/robots.txt
```
