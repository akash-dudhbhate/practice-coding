# Lesson 16 — Approach Comparison

## Problem: Fetch Multiple URLs

### Approach 1: Sequential
```python
results = []
for url in urls:
    results.append(await fetch(url))
```
**Cons:** O(n) time — each request waits for the previous.

### Approach 2: gather
```python
results = await asyncio.gather(*[fetch(url) for url in urls])
```
**Pros:** O(1) time (all concurrent). **Cons:** All must complete before any result.

### Approach 3: as_completed
```python
for coro in asyncio.as_completed([fetch(url) for url in urls]):
    result = await coro
    process(result)
```
**Pros:** Process results as they arrive. **Cons:** More complex.

**Winner:** Approach 2 (gather) for most cases. Approach 3 when you need results ASAP.
