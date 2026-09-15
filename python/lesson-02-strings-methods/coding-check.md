# Lesson 02 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01-solve.py — Count vowels
- [ ] `count_vowels("hello")` returns `2`
- [ ] `count_vowels("AEIOU")` returns `5` (case-insensitive)
- [ ] `count_vowels("rhythm")` returns `0`
- [ ] `count_vowels("")` returns `0`

### p02-solve.py — Reverse string
- [ ] `reverse_string("hello")` returns `"olleh"`
- [ ] `reverse_string("")` returns `""`
- [ ] `reverse_string("a")` returns `"a"`
- [ ] No use of `s[::-1]` or `reversed()`

### p03-solve.py — Palindrome check
- [ ] `is_palindrome("racecar")` returns `True`
- [ ] `is_palindrome("hello")` returns `False`
- [ ] `is_palindrome("")` returns `True` (empty string is a palindrome)
- [ ] `is_palindrome("Aa")` returns `True` (case-insensitive)

## Medium

### p01-solve.py — Initials
- [ ] `get_initials("John Doe")` returns `"JD"`
- [ ] `get_initials("Akash Kumar Singh")` returns `"AKS"`
- [ ] `get_initials("  hello  world  ")` returns `"HW"` (handles extra spaces)

### p02-solve.py — Word count
- [ ] `count_words("hello world")` returns `2`
- [ ] `count_words("one two three four")` returns `4`
- [ ] `count_words("")` returns `0`
- [ ] `count_words("  multiple   spaces  ")` returns `2` (handles extra spaces)

### p03-solve.py — Replace spaces with underscores
- [ ] `replace_spaces("hello world")` returns `"hello_world"`
- [ ] `replace_spaces("  hello  ")` returns `"hello"` (strips first, then replaces)
- [ ] `replace_spaces("no_spaces")` returns `"no_spaces"`

## Hard

### p01-solve.py — Anagram check
- [ ] `is_anagram("listen", "silent")` returns `True`
- [ ] `is_anagram("hello", "world")` returns `False`
- [ ] `is_anagram("a", "a")` returns `True`
- [ ] `is_anagram("abc", "ab")` returns `False` (different lengths)
- [ ] Case-insensitive: `is_anagram("Listen", "Silent")` returns `True`

### p02-solve.py — Run-length encoding
- [ ] `compress("aaabbc")` returns `"a3b2c1"`
- [ ] `compress("abc")` returns `"a1b1c1"`
- [ ] `compress("")` returns `""`
- [ ] `compress("aaaa")` returns `"a4"`

### p03-solve.py — Extract email domain
- [ ] `extract_domain("user@gmail.com")` returns `"gmail.com"`
- [ ] `extract_domain("akash.kumar@yahoo.co.in")` returns `"yahoo.co.in"`
- [ ] `extract_domain("a@b.io")` returns `"b.io"`
- [ ] Returns `""` or raises error if no `@` found

## How to verify

```bash
python easy/p01-solve.py
```

Or test from a REPL:
```bash
python -c "from easy.p01_solve import count_vowels; print(count_vowels('hello'))"
```
