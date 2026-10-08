# 42 — `:=` — where it genuinely helps (while-read loops, comprehensions)

> **Interview question:** "What does the walrus operator `:=` do, and where is it actually useful?"
> **What the interviewer is really testing:** Whether you know it's *assignment inside an expression* — and can name real use cases, not just the syntax.

## Theory — what it is

The **walrus operator** `:=` (officially the "assignment expression", added in **Python 3.8**, PEP 572) assigns a value to a variable *and* evaluates to that value in one step — letting you bind a name in the middle of an expression, like inside an `if`, `while`, or comprehension. Normal `=` is a *statement* (can't live inside an expression); `:=` is an *expression* (produces a value where it's used).

The name is a joke: `:=` looks like a walrus lying on its side — two eyes, two tusks. It was famously controversial (Guido resigned as BDFL partly over the PEP 572 fight) because Python deliberately kept `=` and `==` visually distinct and some feared `:=` would blur the line and invite Perl-style write-only code.

Used well, it removes duplicated work: compute a value once, test it, and keep it — instead of computing twice or adding a separate line before the check. Used badly (chained walruses, walrus inside lambda gymnastics), it hurts readability — which is exactly what the interview follow-up probes.

## Why it was needed

The motivating pain: **loop-and-test patterns** where you need a computed value both for the test and the body. Without `:=`, reading chunks until empty requires either an extra line inside the loop plus a duplicated call, or `iter()` with a sentinel:

```python
# before: either duplicated call...
chunk = f.read(8)
while chunk:
    process(chunk)
    chunk = f.read(8)
```

With `:=`: `while chunk := f.read(8):` — assign and test in one breath. Same win in comprehensions: `[f(x) for x in xs if f(x) > 0]` calls `f` twice per element; `[y for x in xs if (y := f(x)) > 0]` calls it once.

## Where it's used in a real project

- **Read/process until empty:** sockets, streams, `sys.stdin`, pagination APIs — `while data := sock.recv(4096):`.
- **Regex/parse guards:** `if m := pattern.match(line):` then use `m.group(1)` — avoids `match`/`if m:` two-liner.
- **Comprehensions with reused computed values:** capture `f(x)` once instead of evaluating twice.
- **`any()`/`all()` debugging:** `any(err := check(x) for x in items)` keeps the failing value.
- **DB row loops:** `while row := cursor.fetchone():`.

## Diagram

```
Normal:  compute -> test -> (maybe) compute AGAIN
   line = read()          while line:            use line
                             line = read()      <- repeated call

Walrus:  compute ONCE, test + bind together
   while (line := read()):
        ^             ^
        assigns       also evaluates -> tested by while
        line          (same value used in body)

Comprehension:
   [y for x in xs if (y := f(x)) > 0]
                        ^---- bind once, reuse in [y ...] and test
```

## Code — explained

```python
data = "hello"

# 1) if-statement binding
if (n := len(data)) > 3:
    print(n)             # 5 — n bound inside the condition

# 2) while-read until empty
chunks = iter(["a", "b", ""])
while (c := next(chunks)):
    print("got", c)      # got a / got b — stops on ""

# 3) comprehension — compute once
xs = [1, -2, 3]
print([y for x in xs if (y := x * 10) > 0])   # [10, 30]
print(y)                # 30 — leaks to enclosing scope (on purpose!)

# walrus needs parens in some spots:
# if x := 5 > 3:      # binds (5>3)=True to x — precedence trap!
if (x := 5) > 3:       # correct: x = 5, then test 5 > 3
    print(x)           # 5
```

1. `(n := len(data))` — assigns 5 to `n` and yields 5 for the `>3` test; `n` stays usable in the body.
2. `while (c := next(chunks))` — each iteration binds and tests; empty string is falsy, loop ends.
3. Comprehension binds `y = x*10` once — the `if` tests `y`, the output expression reuses `y`. No double call.
4. Walrus bindings **leak** out of comprehensions to the enclosing scope (unlike loop vars) — a documented feature.
5. Precedence trap: `x := 5 > 3` binds `True`, not `5` — wrap the assignment in parens when combining with other operators.

## Problems

### Easy — read until sentinel
**Problem:** Given an iterator of tokens, print each until the empty string `""`. Use `:=` so `next()` appears once.
**Try this input:** `iter(["go", "stop", "", "never"]);`
**Expected output:** `go` then `stop` (never reaches "never")
**Solution:**
```python
tokens = iter(["go", "stop", "", "never"])
while (t := next(tokens)):
    print(t)
# go
# stop
```
**Logic explained:**
1. `t := next(tokens)` binds the token and yields it for the `while` test in one expression.
2. `""` is falsy -> loop exits before the body — clean sentinel handling.
3. Without walrus you'd write `next` twice (before loop + at loop end) — duplication the operator exists to kill.

### Medium — regex guard
**Problem:** From a list of lines, extract digits from lines matching `key=NUM` and collect them; skip non-matching lines. Use `:=` so `match` is called once.
**Try this input:** `["port=8080", "bad line", "timeout=30"]`
**Expected output:** `[8080, 30]`
**Solution:**
```python
import re

lines = ["port=8080", "bad line", "timeout=30"]
nums = [int(m.group(1)) for line in lines
        if (m := re.match(r"\w+=(\d+)", line))]
print(nums)   # [8080, 30]
```
**Logic explained:**
1. `m := re.match(...)` binds the match object (or `None`) — falsy `None` filters out non-matching lines.
2. When truthy, `m.group(1)` is reused in the output expression — one regex evaluation per line.
3. Without walrus you'd call `re.match` twice or switch to a plain loop.

### Hard — expensive computation in a comprehension
**Problem:** `f(x)` is expensive (imagine a DB call). Keep only positive results, paired with their input: `[(x, f(x))]` — `f` must be called exactly once per element.
**Try this input:** `xs = [-1, 2, -3, 4]`, `f(x) = x * x - 5`
**Expected output:** `[(-3, 4), (4, 11)]` (f(-1) = -4 and f(2) = -1 are filtered out)
**Solution:**
```python
calls = []
def f(x):
    calls.append(x)
    return x * x - 5

xs = [-1, 2, -3, 4]
out = [(x, y) for x in xs if (y := f(x)) > 0]
print(out)            # [(-3, 4), (4, 11)]
print(calls)          # [-1, 2, -3, 4] — exactly one call per element
```
**Logic explained:**
1. `y := f(x)` binds the result once; the `if` filters on it and `(x, y)` reuses it.
2. Without walrus, `[(x, f(x)) for x in xs if f(x) > 0]` calls `f` twice per kept element — on a DB call that's 2x cost.
3. `calls` proves each input hit `f` exactly once — the real-world justification for `:=` in comprehensions.

## The 30-second interview answer

"`:=` is an assignment expression — it assigns a value and evaluates to it, so you can bind inside an `if`, `while`, or comprehension. Added in 3.8, PEP 572 — the walrus name is just the look of it. It genuinely helps where you'd otherwise compute twice or add a line: `while chunk := f.read(8)` for read-loops, `if m := pattern.match(s)` for regex guards, and comprehensions like `[y for x in xs if (y := f(x)) > 0]` where `f` should run once per element. Two gotchas: watch operator precedence — wrap the assignment in parens — and bindings leak out of comprehensions to the enclosing scope."

## Follow-up trap

**"Why was it controversial / when should you NOT use it?"** Because it blurs assignment and expression — nested walruses or walrus-in-lambda create write-only code; the PEP fight contributed to Guido stepping down as BDFL. Rule: use it only where it removes duplication. Also expect: *"what does `if x := f() or default:` do?"* — binds the whole `or` expression to `x` (precedence!), and *"walrus vs := in a lambda?"* — assignment expressions can't declare a *new* variable inside a lambda's scope.
