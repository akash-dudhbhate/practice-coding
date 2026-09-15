# Lesson 16 — Coding Check

## Easy

### p01-solve.py — get_user
- [ ] `get_user("github")` returns a dict with "login", "name", "public_repos" keys
- [ ] Uses `requests.get()` with the correct URL
- [ ] Parses JSON with `.json()`
- [ ] Handles non-existent user (returns None or raises clear error)

### p02-solve.py — get_repos
- [ ] `get_repos("github")` returns a list of repo names (strings)
- [ ] Extracts "name" from each repo dict
- [ ] Returns at least the first page of repos

### p03-solve.py — search_joke
- [ ] Fetches from a free joke API
- [ ] Returns joke text (string)
- [ ] Handles API errors gracefully

## Medium

### p01-solve.py — get_all_repos with pagination
- [ ] Fetches ALL repos, not just the first page
- [ ] Uses pagination params (page and per_page)
- [ ] Stops when no more repos are returned
- [ ] Returns a single list of all repo names

### p02-solve.py — create_issue
- [ ] Uses POST request with JSON body
- [ ] Includes Authorization header with token
- [ ] Handles 401 (bad token) with clear error
- [ ] Handles 403 (no permission) with clear error
- [ ] Returns issue data on success

### p03-solve.py — fetch_with_retry
- [ ] Retries on 5xx errors
- [ ] Retries on timeout
- [ ] Uses exponential backoff (1s, 2s, 4s)
- [ ] Gives up after max_retries
- [ ] Returns response on success
- [ ] Raises exception after all retries fail

## Hard

### p01-solve.py — APIClient class
- [ ] Uses `requests.Session()` internally
- [ ] Sets auth headers on session
- [ ] `get(path)` makes GET to base_url + path
- [ ] `post(path, data)` makes POST with JSON
- [ ] `put(path, data)` makes PUT with JSON
- [ ] `delete(path)` makes DELETE
- [ ] All methods include timeout
- [ ] All methods call `raise_for_status()`

### p02-solve.py — download_large_file
- [ ] Uses `stream=True` for chunked download
- [ ] Downloads in chunks (e.g., 8192 bytes)
- [ ] Shows progress (bytes downloaded)
- [ ] Writes to file correctly
- [ ] Handles network errors
- [ ] Handles file write errors

### p03-solve.py — scrape_api with rate limiting
- [ ] Fetches paginated data
- [ ] Sleeps `rate_limit` seconds between requests
- [ ] Handles 429 with Retry-After header
- [ ] Returns all results from all pages
- [ ] Stops when no more pages
