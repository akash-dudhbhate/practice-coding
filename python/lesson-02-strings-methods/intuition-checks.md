# Lesson 02 — Intuition Checks

> Don't run the code. Answer mentally first.

---

## Check 01: String Immutability
```python
s = "hello"
s[0] = "H"
```
What happens?
- (A) s becomes "Hello"
- (B) TypeError
- (C) Nothing

<details><summary>Answer</summary>
**(B) TypeError** — Strings are immutable in Python. You can't change individual characters. Use `s = "H" + s[1:]`.
</details>

---

## Check 02: Slicing
```python
s = "abcdef"
print(s[1:4])
print(s[:3])
print(s[3:])
print(s[::-1])
```
What prints (4 lines)?

<details><summary>Answer</summary>
```
bcd
abc
def
fedcba
```
`[start:stop]` — stop is exclusive. `[:3]` = first 3. `[3:]` = from index 3 to end. `[::-1]` = reverse.
</details>

---

## Check 03: String Methods Chaining
```python
s = "  Hello World  "
print(s.strip().lower().replace(" ", "_"))
```
What prints?

<details><summary>Answer</summary>
```
hello_world
```
Methods chain left to right: strip removes spaces, lower makes lowercase, replace swaps spaces for underscores.
</details>

---

## Check 04: Concatenation
```python
print("2" + "3")
print(2 + 3)
print("2" + 3)
```
What happens (3 lines)?

<details><summary>Answer</summary>
```
23
5
TypeError
```
`"2" + "3"` = string concatenation. `2 + 3` = addition. `"2" + 3` = TypeError (can't add str and int). Use `str(3)` or `int("2")`.
</details>

---

## Check 05: f-strings
```python
name = "Akash"
age = 25
print(f"{name=}, {age=}")
```
What prints? (Python 3.8+)

<details><summary>Answer</summary>
```
name='Akash', age=25
```
`{name=}` is a debug feature — prints the variable name and value. Great for debugging.
</details>
