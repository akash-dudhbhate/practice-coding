# Lesson 17 — Intuition Checks

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
