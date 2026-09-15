# Lesson 01 — Coding Check

Use this to verify your solutions before asking me to review. Each problem file has its own expected behavior — check against these.

## Easy

### p01-max-of-two.py
- [ ] `max_of_two(3, 7)` returns `7`
- [ ] `max_of_two(10, 2)` returns `10`
- [ ] `max_of_two(5, 5)` returns `5`
- [ ] No use of built-in `max()`

### p02-even-or-odd.py
- [ ] `is_even(4)` returns `True`
- [ ] `is_even(7)` returns `False`
- [ ] `is_even(0)` returns `True`

### p03-celsius-to-fahrenheit.py
- [ ] `celsius_to_fahrenheit(0)` returns `32.0`
- [ ] `celsius_to_fahrenheit(100)` returns `212.0`
- [ ] Returns a float

## Medium

### p01-max-of-three.py
- [ ] `max_of_three(1, 2, 3)` returns `3`
- [ ] Reuses `max_of_two` (no raw if/else for 3-way comparison)
- [ ] `max_of_three(7, 7, 7)` returns `7`

### p02-leap-year.py
- [ ] `is_leap_year(2000)` returns `True` (div by 400)
- [ ] `is_leap_year(1900)` returns `False` (div by 100, not 400)
- [ ] `is_leap_year(2024)` returns `True` (div by 4, not 100)
- [ ] `is_leap_year(2023)` returns `False`

### p03-count-vowels.py
- [ ] `count_vowels("hello")` returns `2`
- [ ] `count_vowels("AEIOU")` returns `5` (case-insensitive)
- [ ] `count_vowels("rhythm")` returns `0`
- [ ] `count_vowels("")` returns `0`

## Hard

### p01-fizzbuzz.py
- [ ] `fizzbuzz(5)` returns `["1", "2", "Fizz", "4", "Buzz"]`
- [ ] `fizzbuzz(15)` ends with `"FizzBuzz"` at index 14
- [ ] Returns a list of strings

### p02-reverse-string.py
- [ ] `reverse_string("hello")` returns `"olleh"`
- [ ] `reverse_string("")` returns `""`
- [ ] No use of `s[::-1]` or `reversed()`

### p03-is-prime.py
- [ ] `is_prime(2)` returns `True`
- [ ] `is_prime(1)` returns `False`
- [ ] `is_prime(4)` returns `False`
- [ ] `is_prime(13)` returns `True`

## How to verify

Run each file with your own test calls:
```bash
python easy/p01-max-of-two.py
```

Or test from a REPL:
```bash
python -c "from easy.p01_max_of_two import max_of_two; print(max_of_two(3, 7))"
```
