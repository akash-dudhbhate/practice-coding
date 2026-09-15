# Lesson 06 — Coding Check

Use this to verify your solutions before asking me to review. Each problem file has its own expected behavior — check against these.

## Easy

### p01-solve.py (greet)
- [ ] `greet("Akash")` returns `"Hello, Akash!"`
- [ ] `greet("Sam", "Hi")` returns `"Hi, Sam!"`
- [ ] `greeting` has a default value

### p02-solve.py (sum_all)
- [ ] `sum_all(1, 2, 3)` returns `6`
- [ ] `sum_all()` returns `0`
- [ ] `sum_all(10)` returns `10`
- [ ] Uses `*nums`

### p03-solve.py (square)
- [ ] `square(5)` returns `25`
- [ ] `square(0)` returns `0`
- [ ] `square` is a lambda assigned to a variable

## Medium

### p01-solve.py (make_tag)
- [ ] `make_tag("a", "link", href="x.com")` returns `'<a href="x.com">link</a>'`
- [ ] `make_tag("p", "hi")` returns `'<p>hi</p>'` (no attrs → no space)
- [ ] `make_tag("img", "", src="a.png", alt="x")` includes both attrs
- [ ] Uses `**attrs`

### p02-solve.py (safe_append)
- [ ] `safe_append(1)` returns `[1]`
- [ ] Calling `safe_append(1)` twice returns separate lists (no shared default)
- [ ] `safe_append(2, [1])` returns `[1, 2]`
- [ ] Uses `lst=None` pattern (no mutable default)

### p03-solve.py (apply_func)
- [ ] `apply_func(lambda x: x*2, [1,2,3])` returns `[2, 4, 6]`
- [ ] `apply_func(str, [1,2])` returns `["1", "2"]`
- [ ] `apply_func(len, ["ab","a"])` returns `[2, 1]`
- [ ] Does not mutate the input list

## Hard

### p01-solve.py (make_counter)
- [ ] `c = make_counter(); c()` returns `1`; `c()` returns `2`
- [ ] Two counters are independent: `c1=make_counter(); c2=make_counter(); c1(); c2()` → `1` and `1`
- [ ] `make_counter(10)()` returns `11`
- [ ] Uses a closure

### p02-solve.py (compose)
- [ ] `compose(lambda x: x+1, lambda x: x*2)(3)` returns `7`
- [ ] `compose(lambda x: x*3, lambda x: x+1)(2)` returns `9`
- [ ] Returns a function (not a value)

### p03-solve.py (build_profile / format_profile)
- [ ] `build_profile("Akash", age=25, city="LA")` returns `{"name":"Akash","age":25,"city":"LA"}`
- [ ] `format_profile({"name":"Akash","age":25})` returns `"Akash (age=25)"`
- [ ] `format_profile({"name":"Sam"})` returns `"Sam"`
- [ ] Multiple attrs appear in the formatted string

## How to verify

Run each file with your own test calls:
```bash
python easy/p01-solve.py
```

Or test from a REPL:
```bash
python -c "from easy.p01_solve import greet; print(greet('Akash'))"
```
