# lesson-17-database-sqlite — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Status Codes
```python
# 200 = ?
# 404 = ?
# 500 = ?
```
<details><summary>Answer</summary>
200 = OK, 404 = Not Found, 500 = Server Error. 2xx = success, 4xx = client error, 5xx = server error.
</details>

## Check 02: requests vs urllib
Why prefer `requests` over `urllib`?
<details><summary>Answer</summary>
`requests` has a simpler API, better session handling, automatic JSON parsing, and cleaner error handling. `urllib` is built-in but clunky.
</details>

## Check 03: BeautifulSoup parser
```python
soup = BeautifulSoup(html, "html.parser")
soup = BeautifulSoup(html, "lxml")
```
<details><summary>Answer</summary>
`lxml` is faster but requires installation. `html.parser` is built-in. Use `lxml` for production, `html.parser` for quick scripts.
</details>

## Check 04: Rate Limiting
```python
for url in urls:
    requests.get(url)  # no delay
```
<details><summary>Answer</summary>
**Bad practice** — can get you banned. Add `time.sleep(1)` between requests, or use rate limiting.
</details>

## Check 05: API Key in URL
```python
r = requests.get(f"https://api.example.com?key={API_KEY}")
```
<details><summary>Answer</summary>
**Security risk** — API key in URL is logged by servers, proxies, and browser history. Use headers instead: `requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})`.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): No User-Agent
```python
import requests
r = requests.get("https://example.com")
```
<details><summary>Answer</summary>
**Bug:** Some sites block requests without a User-Agent header.
**Fix:** `requests.get(url, headers={"User-Agent": "Mozilla/5.0"})`.
</details>

## Debug 02 (Medium): Not Checking Status
```python
r = requests.get(url)
data = r.json()
```
<details><summary>Answer</summary>
**Bug:** If the request fails (404, 500), `r.json()` raises or returns error data.
**Fix:** `r.raise_for_status()` before parsing.
</details>

## Debug 03 (Hard): Selector Too Specific
```python
price = soup.select_one("div.container > div.row > div.col-md-4 > span.price").text
```
<details><summary>Answer</summary>
**Bug:** Selector is too brittle — any HTML change breaks it.
**Fix:** Use a more robust selector like `soup.select_one(".price")` or `[data-price]`.
</details>

---

## Common Mistakes — the traps learners hit

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

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): String SQL Injection Risk
### Before
```python
cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
```
### After
```python
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
```

## Refactor 02 (Medium): No Connection Context
### Before
```python
conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()
cursor.execute("...")
conn.commit()
conn.close()  # might not run if error
```
### After
```python
with sqlite3.connect("db.sqlite") as conn:
    conn.execute("...")
    # auto-commits, auto-closes
```

## Refactor 03 (Hard): Raw SQL Everywhere
### Before
```python
def get_user(id):
    c = conn.execute("SELECT * FROM users WHERE id = ?", (id,))
    return c.fetchone()
def get_post(id):
    c = conn.execute("SELECT * FROM posts WHERE id = ?", (id,))
    return c.fetchone()
```
### After
```python
# Use SQLAlchemy ORM or at least a repository pattern
class Repository:
    def __init__(self, conn, table):
        self.conn = conn
        self.table = table
    def get(self, id):
        return self.conn.execute(
            f"SELECT * FROM {self.table} WHERE id = ?", (id,)
        ).fetchone()
```

---

## Approach Comparison — different ways to solve it

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
