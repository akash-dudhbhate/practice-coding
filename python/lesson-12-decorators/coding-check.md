# Lesson 12 — Coding Check

## Easy

### p01-solve.py — @shout decorator
- [ ] `@shout` applied to a function returning "hello" makes it return "HELLO"
- [ ] Original function is not modified (decorator wraps it)
- [ ] Uses `*args, **kwargs` in wrapper

### p02-solve.py — @timer decorator
- [ ] Prints execution time after function runs
- [ ] Returns the original function's result (not just timing)
- [ ] Uses `time.time()` for measurement

### p03-solve.py — @log_call decorator
- [ ] Prints function name before calling
- [ ] Prints return value after calling
- [ ] Returns the original result

## Medium

### p01-solve.py — @repeat(n) decorator
- [ ] `@repeat(3)` calls the function 3 times
- [ ] Returns the LAST result
- [ ] Uses 3 levels of nesting (factory → decorator → wrapper)
- [ ] Uses `@wraps`

### p02-solve.py — @cache decorator
- [ ] First call computes and caches the result
- [ ] Second call with same args returns cached result (no re-computation)
- [ ] Different args still compute fresh results
- [ ] Cache is stored in a dict

### p03-solve.py — @validate_positive decorator
- [ ] Function with positive args works normally
- [ ] Function with negative arg raises ValueError
- [ ] Function with zero raises ValueError
- [ ] Non-numeric args are ignored (no error)

## Hard

### p01-solve.py — @CountCalls class decorator
- [ ] `func.count` starts at 0
- [ ] After calling 3 times, `func.count` is 3
- [ ] Uses `__init__` and `__call__`
- [ ] Original function still returns its result

### p02-solve.py — @retry decorator
- [ ] Function that always succeeds → called once, no retry
- [ ] Function that fails twice then succeeds → called 3 times total
- [ ] Function that always fails → retried `times` times, then raises the exception
- [ ] Uses `time.sleep(delay)` between retries

### p03-solve.py — Stacked decorators
- [ ] Both `@log` and `@timer` applied to same function
- [ ] Output shows function name (from @log)
- [ ] Output shows execution time (from @timer)
- [ ] Function returns correct result
- [ ] Both decorators use `@wraps`
