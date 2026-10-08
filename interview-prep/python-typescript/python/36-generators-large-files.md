# 36 — Processing a 10GB file with generators

> **Interview question:** "You have a 10GB log file and 2GB of RAM. How do you process it in Python without running out of memory?"
> **What the interviewer is really testing:** Whether you know that file objects are already lazy iterators, that `readlines()`/`read()` materialize everything, and that generator pipelines let you filter/transform/aggregate line-by-line with constant memory.

## Theory — what it is

`open(path)` returns a file object that is itself an **iterator**: `for line in f` pulls one line at a time from the OS buffer — the whole file never enters RAM. Three ways to read, three memory profiles:

- `f.read()` — reads the **entire file** into one string: O(file size) memory. Fatal on 10GB.
- `f.readlines()` — reads the entire file into a **list of lines**: also O(file size). Same problem.
- `for line in f:` — reads **one line per iteration**: O(longest line) memory. This is the only safe option.

A **generator** extends this laziness to your own processing. A function with `yield` produces values one at a time on demand — pause, hand out a value, resume where it left off. You can chain generators into a **pipeline**: `lines → parsed → filtered → aggregated`, where each stage only ever holds one item. Memory stays flat regardless of input size; you trade "hold everything" for "pull what you need, when you need it."

"Jargon" decoded: **lazy** = compute/produce only when asked. **materialize** = turn a lazy sequence into a concrete list in memory. **streaming** = processing data as it flows, one piece at a time.

## Why it was needed

Two walls: memory and startup latency. Loading 10GB needs 10GB+ of RAM (plus Python object overhead — often 2-3× the file size for a list of strings). Even if it fits, the user waits for the full load before any processing starts.

A streaming pipeline solves both: memory is bounded by the longest line (~KB), and the first result can be produced while the disk is still reading the middle of the file. It also composes — `filter`, `map`, `sum` all accept iterables, so generator stages slot together like Unix pipes (`cat file | grep x | wc -l` is exactly this idea).

## Where it's used in a real project

- **Log analysis**: count errors, extract user IDs, find slow requests in multi-GB server logs.
- **ETL/data pipelines**: read → parse → validate → transform → write, one record at a time.
- **CSV processing**: `csv.reader(f)` is already lazy — wrap it in generator stages.
- **Database exports**: cursor fetching rows lazily (`fetchmany`/server-side cursor) instead of `fetchall`.

## Diagram

```
read() / readlines():               streaming pipeline:

10GB file ──► RAM [██████████]      10GB file ──► f (one line)
10GB+ objects, OOM risk                    │
                                           ▼
                              gen: parse   (one record)
                                           │
                                           ▼
                              gen: filter  (one record, maybe dropped)
                                           │
                                           ▼
                              aggregate    (one counter/sum)
                                           │
                                           ▼
                                    constant memory
                                    ≈ size of ONE line
```

## Code — explained

```python
def read_errors(path):                            # 1
    with open(path) as f:                         # 2
        for line in f:                            # 3
            yield line.rstrip("\n")               # 4

def only_errors(lines):                           # 5
    for line in lines:
        if "ERROR" in line:
            yield line                            # 6

def count_by_code(lines):                         # 7
    counts = {}
    for line in lines:
        code = line.split()[0]
        counts[code] = counts.get(code, 0) + 1
    return counts                                 # 8

lines = read_errors("app.log")                    # 9
errors = only_errors(lines)                       # 10
print(count_by_code(errors))                      # 11
```

1. A generator function — calling it does NOT read the file; it returns a generator object.
2. `with` guarantees the file closes when the generator is exhausted or garbage collected.
3. `for line in f` — the file object yields one line at a time; memory = one line.
4. `yield` hands the cleaned line downstream and *pauses* — the file position and loop state are frozen until the next pull.
5. Stage two: a filter generator that wraps stage one.
6. Non-matching lines are simply never yielded — dropped records cost nothing.
7. Stage three: a *terminal* consumer — it pulls from the pipeline and aggregates.
8. Aggregation keeps only a small dict, not the records — the pipeline's memory stays O(1) even at 10GB.
9. Both `read_errors` and `only_errors` are lazy: lines flow one at a time, pulled by `count_by_code`'s loop.
10. Nothing has been read yet — the file is still untouched.
11. Only NOW does data flow: each `for` iteration pulls one line through both stages, counts it, and discards it.

## Problems

### Easy — stream a count
**Problem:** Count lines containing `"WARN"` in a file without loading it into memory.
**Try this input:** a file with lines `["INFO ok", "WARN slow", "ERROR bad", "WARN retry"]`
**Expected output:** `2`
**Solution:**
```python
def count_matching(path, needle):
    count = 0
    with open(path) as f:
        for line in f:            # one line at a time
            if needle in line:
                count += 1
    return count

print(count_matching("app.log", "WARN"))
```
**Logic explained:**
1. `for line in f` streams — memory is one line, not the file.
2. Only `count` persists — an integer, not the data.
3. Same answer as `sum(1 for l in f if "WARN" in l)` — a generator expression version.

### Medium — pipeline with a transform
**Problem:** From lines like `"alice,ERROR,timeout"`, yield only the usernames of ERROR lines, deduplicated in streaming fashion (use a `set` of seen names — small even for 10GB).
**Try this input:**
```
alice,ERROR,timeout
bob,INFO,ok
alice,ERROR,refused
carol,ERROR,crash
```
**Expected output:**
```
alice
carol
```
**Solution:**
```python
def error_users(path):
    seen = set()
    with open(path) as f:
        for line in f:
            user, level, *_ = line.rstrip().split(",")
            if level == "ERROR" and user not in seen:
                seen.add(user)
                yield user

for u in error_users("events.csv"):
    print(u)
```
**Logic explained:**
1. `user, level, *_ = ...` unpacks the first two fields, ignoring the rest (`*_` swallows extras — even malformed lines with more commas survive).
2. `seen` holds only unique usernames — a few KB even for millions of lines, since duplicates never grow it.
3. `alice` is yielded once; her second ERROR line is filtered by `seen`. `bob` is filtered by the level check.
4. Output order is first-appearance order: `alice`, then `carol`.

### Hard — top-N without loading the file
**Problem:** Each line is `"username bytes"` (e.g. `"alice 1500"`). Find the top 3 users by total bytes — without ever holding more than a dict of totals plus a heap of 3 items.
**Try this input:**
```
alice 100
bob 900
alice 50
carol 300
dave 700
```
**Expected output:**
```
[('bob', 900), ('dave', 700), ('carol', 300)]
```
**Solution:**
```python
import heapq

def top_users(path, n=3):
    totals = {}
    with open(path) as f:
        for line in f:
            user, amount = line.split()
            totals[user] = totals.get(user, 0) + int(amount)
    return heapq.nlargest(n, totals.items(), key=lambda kv: kv[1])

print(top_users("usage.log"))
```
**Logic explained:**
1. Pass one — stream the file, aggregate per user into `totals`. Memory = number of *unique users*, not lines (fine unless there are billions of users — then you'd need a different strategy like external sort).
2. `alice` appears twice → totals `150`; `bob` → `900`, `carol` → `300`, `dave` → `700`.
3. `heapq.nlargest(3, ...)` keeps only a 3-element heap internally — O(n) extra memory where n=3, not O(users).
4. Result sorted descending by bytes: `[('bob', 900), ('dave', 700), ('carol', 300)]`.
5. The pattern: stream for I/O, keep only *aggregates* in memory — the file can be infinite; the summary is bounded.

## The 30-second interview answer

"File objects are already iterators — `for line in f` reads one line at a time, so memory is bounded by the longest line, not the file size. I'd never call `read()` or `readlines()` on a big file. I'd build a generator pipeline: one generator reads and yields raw lines, the next parses/filters and yields records, and a terminal consumer aggregates — count, sum, or a bounded structure like a heap for top-N. Each stage holds one item at a time, so memory stays O(1) whether the file is 10MB or 10GB, and results start flowing immediately instead of after a full load. It's the same idea as Unix pipes — `cat | grep | wc` never loads the file either."

## Follow-up trap

**"What if one 'record' spans multiple lines?"** — Then a line-iterator isn't enough; write a generator that accumulates lines until a record boundary (e.g., a blank line or a start marker) and yields the complete record — still O(record) memory, not O(file).

**"Generators keep memory flat — what's the catch?"** — They're single-use and forward-only: once consumed, a generator is exhausted (you can't loop it twice or index it). If you need random access or multiple passes, you either re-open the file / re-create the generator, or materialize *into a bounded structure* — or admit the data is too big for memory and reach for a database, `pandas.read_csv(chunksize=...)`, or a tool like `polars`/`dask` with streaming execution.
