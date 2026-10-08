# 49 — The stdlib modules you actually use: collections, itertools, functools, pathlib, json, re

> **Interview question:** "Which parts of the Python standard library do you reach for most, and why?"
> **What the interviewer is really testing:** Whether you solve everyday problems with battle-tested stdlib tools — or hand-roll `for` loops and `os.path.join` string math that re-implement them badly.

## Theory — what it is

Python's "batteries included" standard library ships ~200 modules. Six show up in almost every real codebase:

- **`collections`** — specialized containers beyond `dict`/`list`/`set`. The two you must know: `Counter` (count hashable items in one line) and `defaultdict` (dict that auto-creates a default value for missing keys — no `if key not in d` dance).
- **`itertools`** — fast, lazy iterator building blocks: `groupby`, `islice`, `chain`, `combinations`, `zip_longest`. Lazy = they yield items one at a time instead of building a list, so they work on streams and huge data.
- **`functools`** — tools for functions: `lru_cache` (memoization as a decorator), `partial` (pre-fill arguments), `reduce`, `wraps` (preserve metadata in decorators), `cache` (unbounded memo, 3.9+).
- **`pathlib`** — object-oriented filesystem paths. `Path("a") / "b.txt"` joins with `/`, plus `.read_text()`, `.exists()`, `.glob("*.py")`, `.suffix`, `.stem`. Replaces `os.path.join` string fiddling.
- **`json`** — serialize to/from JSON: `json.dumps(obj) -> str`, `json.loads(str) -> obj`, `json.dump`/`json.load` for files. Dicts, lists, strings, numbers, booleans, `None` map to JSON; tuples become arrays; sets and datetimes need custom handling.
- **`re`** — regular expressions: `re.search`/`re.match`/`re.findall`/`re.sub`, with named groups `(?P<name>...)`, compiled patterns via `re.compile`, and `re.IGNORECASE` flags.

## Why it was needed

Every one of these exists because the hand-rolled version is a classic bug source:

- Counting with a manual dict loop is five lines where `Counter(votes).most_common(1)` is one — and `Counter` is implemented in optimized C.
- Building "all pairs" or "chunks of N" by hand produces off-by-one errors; `itertools.combinations` and `itertools.batched` (3.12+) are correct and lazy.
- Hand-memoizing a recursive function means managing a dict and a sentinel; `@lru_cache` is one line with bounded memory.
- `os.path.join(a, b)` breaks on Windows/leading slashes/edge cases; `Path` handles separators, `.resolve()`, and `.relative_to()` correctly.
- `json` exists because `eval(response_text)` on API data is a remote-code-execution vulnerability.
- Parsing strings with `split`/`find` chains gets unreadable fast; a named-group regex keeps the whole grammar in one place.

Interview signal: reaching for the right stdlib module shows you know the language's vocabulary — juniors write loops, seniors write `Counter`.

## Where it's used in a real project

- **`collections.Counter`**: log analysis, feature frequencies, "top N" questions, quick validation (`Counter(a) == Counter(b)` compares multiset equality).
- **`defaultdict`**: grouping records (`d[user_id].append(order)`), adjacency lists for graphs.
- **`itertools`**: `groupby` for run-length grouping sorted data, `islice` to peek at the first N of a stream/generator, `chain` to flatten iterables of iterables.
- **`functools.lru_cache`**: memoize expensive pure functions (fibonacci, config lookups, compiled regexes); `functools.wraps` on every decorator you write.
- **`pathlib`**: every file path in modern code — config loading, temp dirs, walking `*.csv` with `.glob`, building output paths with `/`.
- **`json`**: API request/response bodies, config files, serializing data into Redis/SQS payloads.
- **`re`**: validating emails/IDs, parsing log lines, scrubbing secrets from strings (`re.sub`), splitting on messy delimiters.

## Diagram

```
                 your code
                     |
   +---------+-------+--------+---------+--------+--------+
   |         |       |        |         |        |        |
   v         v       v        v         v        v        v
collections itertools functools pathlib  json     re
Counter     groupby   lru_cache Path     dumps    search
defaultdict islice    partial   / read_  loads    findall
OrderedDict chain     wraps     glob     load     sub
   |         |        |         |        |        |
   "count    "lazy    "decorate "files   "API     "parse
   things"   streams" funcs"    as objs" payloads" strings"
```

## Code — explained

```python
from collections import Counter, defaultdict
from itertools import groupby, islice
from functools import lru_cache
from pathlib import Path
import json, re

# collections — Counter: most common item in one line          # 1
votes = ["b", "a", "b", "c", "a", "b"]
print(Counter(votes).most_common(1))        # [('b', 3)]

# collections — defaultdict: group without KeyError checks     # 2
by_len = defaultdict(list)
for w in ["hi", "hey", "yo"]:
    by_len[len(w)].append(w)
print(dict(by_len))                         # {2: ['hi', 'yo'], 3: ['hey']}

# itertools — groupby: group consecutive equal items           # 3
runs = [(k, len(list(g))) for k, g in groupby("aaabbbcca")]
print(runs)                                 # [('a', 3), ('b', 3), ('c', 2), ('a', 1)]

# functools — lru_cache: memoization as one decorator          # 4
@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(40))                              # 102334155 (instant, not exponential)

# pathlib — paths as objects, joined with /                    # 5
p = Path("logs") / "app.log"
print(p.name, p.suffix)                     # app.log .log

# json — dict <-> JSON string                                  # 6
s = json.dumps({"id": 1, "tags": ["a"]})    # '{"id": 1, "tags": ["a"]}'
print(json.loads(s)["id"])                  # 1

# re — named groups keep parsing readable                      # 7
m = re.search(r"(?P<level>ERROR|INFO): (?P<msg>.*)", "ERROR: disk full")
print(m.group("level"), "|", m.group("msg"))  # ERROR | disk full
```

1. `Counter` consumes any iterable of hashables and gives a dict-like of counts, plus `most_common(n)`, arithmetic (`c1 - c2`), and `total()`. Reach for it the moment you write `d[x] = d.get(x, 0) + 1`.
2. `defaultdict(list)` calls the factory for missing keys — grouping becomes append-only. Perfect for `user_id -> orders` maps.
3. `groupby` groups *consecutive* runs and yields `(key, iterator)` — the inner `g` must be consumed inside the loop (hence `list(g)`), and unsorted input produces repeated groups. Reach for it for run-length encoding or grouping already-sorted records; use `defaultdict`/`Counter` when order doesn't matter.
4. `@lru_cache` memoizes on arguments — same args → cached return, no recomputation. `maxsize=None` is unbounded; `maxsize=128` evicts least-recently-used. Only for pure functions with hashable args.
5. `Path` objects overload `/` for joining and carry methods (`read_text`, `exists`, `glob`, `stem`, `with_suffix`) — no `os.path.join` string juggling.
6. `json.dumps` serializes to a string, `json.loads` parses back. Only JSON types survive — sets, bytes, and datetimes raise `TypeError` without a custom encoder.
7. `(?P<name>...)` named groups make the regex self-documenting; `re.search` scans anywhere in the string (`re.match` anchors at the start — a classic gotcha). For repeated use in a loop, `re.compile` the pattern once.

## Problems

### Easy — count without a loop
**Problem:** Given `"the cat sat on the mat with the other cat"`, return the two most frequent words and their counts — without writing a counting loop.
**Try this input:** the sentence above.
**Expected output:** `[('the', 3), ('cat', 2)]`
**Solution:**
```python
from collections import Counter

text = "the cat sat on the mat with the other cat"
print(Counter(text.split()).most_common(2))
# [('the', 3), ('cat', 2)]
```
**Logic explained:**
1. `text.split()` splits on whitespace into a list of words — Counter accepts any iterable.
2. `Counter(words)` builds `{'the': 3, 'cat': 2, 'sat': 1, ...}` — replacing the manual `counts[w] = counts.get(w, 0) + 1` loop.
3. `most_common(2)` returns the top-2 `(word, count)` pairs sorted by frequency; ties resolve by insertion order.

### Medium — run-length encode with groupby
**Problem:** Compress `"aaabbbcca"` into `a3b3c2a1` — runs of consecutive characters. (This is the classic "groupby traps" problem: what breaks if you use a dict instead?)
**Try this input:** `"aaabbbcca"`, then `"aabaa"`
**Expected output:** `a3b3c2a1`, then `a2b1a2`
**Solution:**
```python
from itertools import groupby

def rle(s: str) -> str:
    return "".join(f"{ch}{len(list(g))}" for ch, g in groupby(s))

print(rle("aaabbbcca"))   # a3b3c2a1
print(rle("aabaa"))       # a2b1a2  — 'a' appears twice, correctly
```
**Logic explained:**
1. `groupby("aabaa")` yields `('a', iter)`, `('b', iter)`, `('a', iter)` — consecutive runs only, so the second `a` run is a *separate* group. A dict/Counter would merge them into `a4b1` and corrupt the encoding.
2. `list(g)` materializes the run iterator so `len` can count it — you must consume `g` inside the expression, before groupby advances.
3. `f"{ch}{len(...)}"` formats each run; `"".join` stitches them. This is exactly how `itertools` rewards reading the docs: consecutive-only grouping is the feature, not a bug.

### Hard — parse a log line, count errors per hour
**Problem:** Given log lines like `"2024-05-01T14:23:11 ERROR db: timeout"`, extract the hour and level with one regex, then report error counts per hour — most active hour first.
**Try this input:** the five lines below.
**Expected output:** `[('14', 2), ('15', 1)]` — INFO and malformed lines are skipped; only ERROR lines count.
**Solution:**
```python
from collections import Counter
import re

LOG_RE = re.compile(r"(?P<ts>\d{4}-\d{2}-\d{2}T(?P<hour>\d{2}):\d{2}:\d{2}) (?P<level>\w+) (?P<msg>.*)")

lines = [
    "2024-05-01T14:23:11 ERROR db: timeout",
    "2024-05-01T14:45:02 INFO  api: ok",
    "2024-05-01T15:10:59 ERROR db: timeout",
    "2024-05-01T14:59:00 ERROR api: 500",
    "garbage line that won't match",
]

errors_per_hour = Counter()
for line in lines:
    m = LOG_RE.match(line)                          # anchored at start
    if not m:
        continue                                    # skip malformed lines
    if m.group("level") == "ERROR":
        errors_per_hour[m.group("hour")] += 1

print(errors_per_hour.most_common())
# [('14', 2), ('15', 1)]
```
**Logic explained:**
1. `re.compile` once outside the loop — the pattern is parsed a single time, not per line. Named groups (`hour`, `level`) document the format.
2. `LOG_RE.match` returns `None` on non-matching lines — always check before `.group()`, or you get `AttributeError` on malformed input. Real logs always have junk lines.
3. `Counter` accumulates `hour -> error count` with zero bookkeeping, and `most_common()` sorts descending for the "busiest hour" report.
4. This is the real-world shape: `re` to extract, `collections` to aggregate — a two-tool pipeline replacing ~20 lines of manual parsing.

## The 30-second interview answer

"My everyday six: `collections` for `Counter` and `defaultdict` — counting and grouping without bookkeeping loops; `itertools` for lazy stream processing — `groupby`, `islice`, `chain` — with the caveat that `groupby` only groups consecutive items; `functools` mostly for `lru_cache` memoization and `wraps` in decorators; `pathlib` for all filesystem paths — objects joined with `/` instead of `os.path` string math; `json` for serialization boundaries; and `re` with named groups when string `split` chains get unreadable. The pattern: the stdlib already solved the boring stuff correctly — my job is knowing which tool replaces the loop I'm about to write."

## Follow-up trap

**"What's the `groupby` gotcha?"** — It's the most-asked one: `itertools.groupby` only groups *consecutive* equal items, so `[1,2,1]` yields groups `(1),(2),(1)` — not the merged `(1,1),(2)` you might expect. Sort first if you want full grouping — but then it's often just a `Counter`/`defaultdict` job anyway. Second trap: **"Why `pathlib` over `os.path`?"** — don't just say "it's nicer": `Path` bundles join/normalize/read/glob into one object, `/` can't silently produce `"dirfile.txt"` the way forgotten `os.path.join` does, and `.resolve()` + `.relative_to()` handle symlink/traversal edge cases string math gets wrong. Bonus if they ask about `json`: `json.dumps` on a `set` or `datetime` raises `TypeError` — you need `default=` handlers; and `eval()` on untrusted JSON is an RCE, not a shortcut.
