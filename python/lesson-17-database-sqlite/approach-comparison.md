# Lesson 17 — Approach Comparison

## Problem: Parse HTML Table

### Approach 1: BeautifulSoup
```python
soup = BeautifulSoup(html, "lxml")
table = soup.find("table")
rows = table.find_all("tr")
```

### Approach 2: pandas
```python
import pandas as pd
tables = pd.read_html(html)
df = tables[0]
```

**Winner:** Approach 2 (pandas) for tabular data — one line. Approach 1 for complex parsing.

---

## Problem: Fetch with Retry

### Approach 1: Manual loop
```python
for attempt in range(3):
    try:
        r = requests.get(url)
        r.raise_for_status()
        break
    except requests.RequestException:
        time.sleep(2 ** attempt)
```

### Approach 2: tenacity library
```python
from tenacity import retry, stop_after_attempt, wait_exponential
@retry(stop=stop_after_attempt(3), wait=wait_exponential)
def fetch(url):
    r = requests.get(url)
    r.raise_for_status()
    return r
```

**Winner:** Approach 2 — cleaner, more configurable.
