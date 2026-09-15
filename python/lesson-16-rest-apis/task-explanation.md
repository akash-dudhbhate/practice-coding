# Lesson 16 — Working with REST APIs

## What you'll learn
- REST API conventions and HTTP methods
- requests library (GET, POST, PUT, DELETE)
- Status codes and error handling
- JSON handling
- Authentication (API keys, bearer tokens, basic auth)
- Pagination
- Rate limiting
- Session objects

## Lesson

### GET request
```python
import requests
response = requests.get("https://api.github.com/users/github")
data = response.json()
```

### POST with JSON
```python
response = requests.post(url, json={"name": "Akash"})
```

### With auth
```python
response = requests.get(url, headers={"Authorization": "Bearer token"})
```

### Error handling
```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"Error: {e}")
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Write a function `get_user(username)` that fetches a GitHub user profile via `https://api.github.com/users/{username}` and returns the JSON data.
2. `easy/p02-solve.py` — Write a function `get_repos(username)` that fetches a GitHub user's repositories and returns a list of repo names.
3. `easy/p03-solve.py` — Write a function `search_joke(keyword)` that fetches a joke from a free joke API (e.g., Official Joke API) and returns the joke text.

### Medium
4. `medium/p01-solve.py` — Write a function `get_all_repos(username)` that fetches ALL repos for a user, handling pagination (GitHub API returns 30 per page by default, max 100).
5. `medium/p02-solve.py` — Write a function `create_issue(owner, repo, title, body, token)` that creates a GitHub issue using POST with auth. Handle errors (401, 403, 422).
6. `medium/p03-solve.py` — Write a function `fetch_with_retry(url, max_retries=3)` that retries on failure (5xx or timeout) up to max_retries times with exponential backoff (1s, 2s, 4s).

### Hard
7. `hard/p01-solve.py` — Write an `APIClient` class that uses a `requests.Session()`, sets auth headers, and provides methods: `get(path)`, `post(path, data)`, `put(path, data)`, `delete(path)`. Include automatic error handling and timeout.
8. `hard/p02-solve.py` — Write a function `download_large_file(url, filepath)` that downloads a file in chunks (stream=True), shows progress (bytes downloaded), and handles network errors.
9. `hard/p03-solve.py` — Write a function `scrape_api(base_url, endpoint, rate_limit=0.5)` that fetches paginated data with rate limiting (sleep between requests), handles 429 with Retry-After, and returns all results.

### How to work
- Write your complete solution from scratch below the TODO marker.
- Remove the TODO line when done.
- Test with real free APIs (GitHub API, Official Joke API, JSONPlaceholder).
