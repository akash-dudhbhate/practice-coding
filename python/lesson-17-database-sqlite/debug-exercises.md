# Lesson 17 — Debug Exercises

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
