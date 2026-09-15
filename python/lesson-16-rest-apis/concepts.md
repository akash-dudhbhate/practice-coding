# Lesson 16 — Concepts Explained (Working with REST APIs)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## REST API

**What:** REST (Representational State Transfer) is a convention for designing web APIs. It uses HTTP methods to perform operations on resources (identified by URLs).

```
GET    /users          → list all users
GET    /users/123      → get user 123
POST   /users          → create a new user
PUT    /users/123      → update user 123 (full update)
PATCH  /users/123      → partially update user 123
DELETE /users/123      → delete user 123
```

**Why it exists:** Without a standard convention, every API would be different — `/getUsers`, `/createUser`, `/delete_user?id=123`. REST gives a predictable structure: HTTP method = action, URL = resource. Developers can guess the API without reading docs.

**Where it's used:** Every major web API — GitHub, Twitter, Stripe, Google Maps, AWS. If you're calling an API from Python, it's almost certainly REST.

**What goes wrong without it:**
- Non-RESTful APIs: `POST /getUserData` → uses POST for reading → breaks caching, breaks HTTP semantics.
- Wrong method: using GET to delete → browsers prefetch GET requests → accidental deletions.
- No consistent URL structure → every endpoint is a surprise → hard to learn, hard to maintain.

---

## HTTP Methods

**What:** Each HTTP method has a specific meaning:

| Method | Purpose | Safe* | Idempotent** |
|--------|---------|-------|-------------|
| GET | Read data | Yes | Yes |
| POST | Create data | No | No |
| PUT | Replace data | No | Yes |
| PATCH | Partially update | No | No |
| DELETE | Remove data | No | Yes |

*Safe = doesn't change data. **Idempotent = calling it multiple times has the same effect as calling once.

**Why it exists:** HTTP methods tell the server WHAT you want to do. Without them, you'd encode the action in the URL or body — inconsistent and ambiguous.

**Where it's used:** Every REST API call. `requests.get()`, `requests.post()`, etc.

**What goes wrong without it:**
- POST for reads → can't be cached → slow. POST is not "safe" → proxies won't cache it.
- PUT without full data → partial update → data loss (PUT replaces the entire resource).
- DELETE that's not idempotent → deleting twice causes errors instead of being a no-op.

---

## requests Library

**What:** `requests` is the most popular Python HTTP library. It makes API calls simple.

```python
import requests

# GET
response = requests.get("https://api.github.com/users/github")
data = response.json()    # parse JSON response
print(data["name"])       # "GitHub"

# POST with JSON body
response = requests.post("https://api.example.com/users",
    json={"name": "Akash", "email": "akash@example.com"})

# With query parameters
response = requests.get("https://api.example.com/users",
    params={"page": 1, "limit": 10})

# With headers
response = requests.get("https://api.example.com/users",
    headers={"Authorization": "Bearer token123"})
```

**Why it exists:** Without `requests`, you'd use `urllib` — verbose, complex, ugly. `requests` makes HTTP calls one-liners with sensible defaults.

**Where it's used:** Every Python project that calls APIs — web scrapers, API clients, data pipelines, ML model serving, automation scripts.

**What goes wrong without it:**
- Using `urllib` → 10 lines for what `requests` does in 1 → error-prone, hard to read.
- Forgetting `.json()` → you get a string, not a dict → `data["name"]` → `TypeError`.
- Not checking `response.status_code` → request fails silently → you process an error response as if it were success.

---

## Status Codes

**What:** Every HTTP response has a status code indicating success/failure:

| Code | Meaning | Example |
|------|---------|---------|
| 200 | OK | GET succeeded |
| 201 | Created | POST created a resource |
| 204 | No Content | DELETE succeeded (nothing to return) |
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Not authenticated |
| 403 | Forbidden | Authenticated but not allowed |
| 404 | Not Found | Resource doesn't exist |
| 429 | Too Many Requests | Rate limited |
| 500 | Internal Server Error | Server crashed |

**Why it exists:** Without status codes, you'd have to parse the response body to know if it succeeded. Status codes are machine-readable — `response.status_code == 200` is unambiguous.

**Where it's used:** Every API call. `response.ok` (True for 2xx), `response.status_code`, error handling.

**What goes wrong without it:**
- Assuming 200 means success → 201 (Created) is also success but `status_code == 200` misses it. Use `response.ok` or `response.raise_for_status()`.
- Ignoring 429 (rate limit) → you get banned from the API. Always handle 429 with backoff/retry.
- 401 vs 403 confusion: 401 = not logged in, 403 = logged in but not allowed. Handling them the same → wrong error messages.

---

## JSON Handling

**What:** JSON (JavaScript Object Notation) is the standard data format for APIs. Python dicts/lists serialize to/from JSON.

```python
import json, requests

# Parse JSON response
response = requests.get("https://api.example.com/data")
data = response.json()    # dict or list

# Send JSON in request
payload = {"name": "Akash", "age": 25}
response = requests.post("https://api.example.com/users", json=payload)

# Manual JSON operations
json_string = json.dumps({"key": "value"})    # dict → JSON string
data = json.loads(json_string)                 # JSON string → dict
```

**Why it exists:** APIs need a common data format. JSON is lightweight, human-readable, and works across all languages. Without it, every API would use a different format (XML, YAML, custom) → chaos.

**Where it's used:** Every REST API. `response.json()`, `json=...` in requests, `json.dumps()`/`json.loads()`.

**What goes wrong without it:**
- `response.text` instead of `response.json()` → you get a string → `data["name"]` → TypeError (string indices must be integers).
- `json=` vs `data=`: `json=payload` sends JSON with correct content-type. `data=payload` sends form-encoded. Using `data` when the API expects JSON → 400 error.
- Non-serializable data: `json.dumps({datetime.now()})` → `TypeError`. Datetimes must be converted to strings first.

---

## Authentication

**What:** Most APIs require authentication. Common methods:

```python
# 1. API Key (query param or header)
requests.get(url, params={"api_key": "your_key"})
requests.get(url, headers={"X-API-Key": "your_key"})

# 2. Bearer Token (JWT)
requests.get(url, headers={"Authorization": "Bearer your_jwt_token"})

# 3. Basic Auth (username/password)
from requests.auth import HTTPBasicAuth
requests.get(url, auth=HTTPBasicAuth("user", "pass"))

# 4. Session (persist auth across requests)
session = requests.Session()
session.headers.update({"Authorization": "Bearer token"})
session.get(url)    # auth header included automatically
```

**Why it exists:** Without authentication, anyone can access any data → security disaster. Auth ensures only authorized users can access/modify resources.

**Where it's used:** Every protected API — GitHub, Stripe, Twitter, your own backend.

**What goes wrong without it:**
- Hardcoding API keys in code → committed to git → leaked → someone steals your account. Use environment variables.
- Forgetting auth → 401 error → "but it works in my browser!" (browser has cookies, your script doesn't).
- Using Basic Auth over HTTP (not HTTPS) → credentials sent in plain text → intercepted. Always use HTTPS.

---

## Error Handling

**What:** Handle API errors gracefully — network failures, timeouts, rate limits, server errors.

```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()    # raises HTTPError for 4xx/5xx
    data = response.json()
except requests.Timeout:
    print("Request timed out")
except requests.HTTPError as e:
    print(f"HTTP error: {e.response.status_code}")
except requests.ConnectionError:
    print("Network error")
except requests.RequestException as e:
    print(f"Request failed: {e}")
```

**Why it exists:** Without error handling, a network glitch crashes your entire program. APIs fail, networks drop, servers crash — your code must handle these gracefully.

**Where it's used:** Every production API client. Scripts that run unattended (cron jobs, pipelines) MUST handle errors or they'll fail silently.

**What goes wrong without it:**
- No timeout → request hangs forever → program freezes. Always set `timeout=`.
- No `raise_for_status()` → 404 returns "success" → you process an error page as data → garbage results.
- Catching too broadly: `except Exception` → hides bugs. Catch specific exceptions.

---

## Pagination

**What:** APIs return large datasets in pages — e.g., 50 items per page. You fetch page by page.

```python
all_users = []
page = 1
while True:
    response = requests.get(url, params={"page": page, "per_page": 50})
    data = response.json()
    all_users.extend(data["users"])
    if page >= data["total_pages"]:
        break
    page += 1
```

**Why it exists:** Without pagination, returning 1 million users in one response → huge response → slow, memory-intensive, might crash. Pagination returns manageable chunks.

**Where it's used:** Any API with large datasets — GitHub repos, Twitter followers, database queries.

**What goes wrong without it:**
- Fetching all pages without limit → thousands of requests → rate limited → banned.
- Not checking `total_pages` → infinite loop if the API changes its pagination format.
- Forgetting to handle the last page (might be partial) → missing or duplicate items.

---

## Rate Limiting

**What:** APIs limit how many requests you can make per time period. Exceeding the limit returns 429 (Too Many Requests).

```python
import time

for item in items:
    response = requests.get(f"{url}/{item['id']}")
    if response.status_code == 429:
        retry_after = int(response.headers.get("Retry-After", 60))
        time.sleep(retry_after)
        continue    # retry
    process(response.json())
    time.sleep(0.1)    # be polite — don't hammer the API
```

**Why it exists:** Without rate limits, one user can make 10,000 requests/second → server crashes → API down for everyone. Rate limits ensure fair access.

**Where it's used:** Every public API — GitHub (5000/hour), Twitter (various), Google Maps (per-second limits).

**What goes wrong without it:**
- Ignoring 429 → you get banned → your app stops working.
- No delay between requests → you hit the rate limit immediately → 429 on every request.
- Not reading `Retry-After` header → you wait too long or too little → inefficient or still rate limited.

---

## Session Objects

**What:** A `requests.Session()` persists connections, cookies, and headers across multiple requests.

```python
session = requests.Session()
session.headers.update({"Authorization": "Bearer token"})
session.headers.update({"User-Agent": "MyApp/1.0"})

# All requests use the same connection (faster) and include auth headers
response1 = session.get("https://api.example.com/users")
response2 = session.get("https://api.example.com/posts")
# Cookies from response1 are automatically sent with response2

session.close()    # close when done
```

**Why it exists:** Without sessions, each request opens a new TCP connection → slower (handshake overhead). Sessions reuse connections (HTTP keep-alive) → faster. Also: cookies and headers persist automatically.

**Where it's used:** Any code making multiple requests to the same API — web scrapers, API clients, test suites.

**What goes wrong without it:**
- 100 requests without a session → 100 TCP connections → slow. With a session → 1 connection reused → 3-5x faster.
- Forgetting `session.close()` → connection leaks. Use `with requests.Session() as s:` for automatic cleanup.
- Cookies not persisting → login then next request fails (no session cookie) → use a Session.
