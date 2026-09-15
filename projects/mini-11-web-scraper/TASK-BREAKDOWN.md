# Web Scraper (Python) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-11-web-scraper/
├── scraper.py, parser.py, exporter.py, main.py
└── README.md
```

---

## Implementation Steps

### Step 1: Setup

pip install requests beautifulsoup4. Test with a simple page.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: Fetch Page

requests.get with timeout, headers (User-Agent). Handle errors (404, timeout).

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Parse HTML

BeautifulSoup: find titles, links, text. CSS selectors for specific elements.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: Extract Data

Extract structured data: title, price, rating, link. Store as list of dicts.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Pagination

Follow 'next' links. Limit max pages. Rate limiting (time.sleep).

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Export to CSV

Write data to CSV with csv module. Include headers. Handle special characters.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Export to JSON

Optional: also export to JSON with json.dumps.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: CLI Interface

argparse: URL, output file, max pages, format (csv/json).

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: Rate Limiting

Respect robots.txt. Add delay between requests. Max retries.

**Checkpoint:** Step 9 is complete when the described functionality works.

### Step 10: Error Handling

Network errors, parse errors, missing elements. Continue on error.

**Checkpoint:** Step 10 is complete when the described functionality works.

---

## Final Checklist

- [ ] Fetch page with requests
- [ ] Parse with BeautifulSoup
- [ ] Extract structured data
- [ ] Handle pagination
- [ ] Export to CSV
- [ ] Rate limiting (delays)
- [ ] CLI with argparse
- [ ] Error handling (graceful)
- [ ] Respects robots.txt

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
