# Lesson 14 — Coding Check

## Easy

### p01-solve.py — async_greet
- [ ] `async_greet("Akash")` returns "Hello, Akash" (after ~1 second)
- [ ] Uses `async def` and `await asyncio.sleep(1)`
- [ ] Runs via `asyncio.run()`

### p02-solve.py — Start/End with timing
- [ ] Prints "Start" then "End" after 0.5 seconds
- [ ] Total time is ~0.5 seconds (not more)

### p03-solve.py — Concurrent sleep
- [ ] Two functions with different sleep times (e.g., 1s and 2s)
- [ ] Run concurrently with `asyncio.gather()`
- [ ] Total time is ~2 seconds (max, not sum of 3s)

## Medium

### p01-solve.py — fetch_all
- [ ] Fetches multiple URLs concurrently
- [ ] Returns results in the same order as input URLs
- [ ] Total time is ~max(single fetch time), not sum
- [ ] Uses `asyncio.gather()`

### p02-solve.py — ThreadPoolExecutor
- [ ] 5 "downloads" run concurrently
- [ ] Uses `ThreadPoolExecutor` with `max_workers=5`
- [ ] Total time is ~max(single download), not 5x

### p03-solve.py — ProcessPoolExecutor
- [ ] Squares of 1-20 computed in parallel
- [ ] Uses `ProcessPoolExecutor`
- [ ] Results are correct: [1, 4, 9, ..., 400]

## Hard

### p01-solve.py — Rate limiter with Semaphore
- [ ] 10 tasks are processed
- [ ] At most 3 run concurrently at any time
- [ ] Uses `asyncio.Semaphore(3)`
- [ ] All 10 tasks complete

### p02-solve.py — Async scraper with timeout
- [ ] Fetches 5 URLs concurrently
- [ ] Each request has a 5-second timeout
- [ ] Handles timeout gracefully (catches `asyncio.TimeoutError`)
- [ ] Returns only successful results
- [ ] Uses `asyncio.wait_for()`

### p03-solve.py — Producer-consumer
- [ ] Producer generates 10 items and puts them in `asyncio.Queue`
- [ ] Two consumers process items from the queue
- [ ] All 10 items are processed
- [ ] Producer and consumers run concurrently
- [ ] Uses `asyncio.Queue` for coordination
