# Lesson 02 — Common Mistakes

---

## Mistake 01: Forgetting strings are immutable
```python
# WRONG
s = "hello"
s[0] = "H"  # TypeError

# CORRECT
s = "H" + s[1:]  # "Hello"
# or
s = s.replace("h", "H")
```

## Mistake 02: Not handling case
```python
# WRONG — misses uppercase
if "a" in text:  # misses "A"

# CORRECT
if "a" in text.lower():
```

## Mistake 03: Using == for string search
```python
# WRONG — exact match only
if text == "hello":  # misses "Hello", "hello ", " hello"

# CORRECT — for partial match
if "hello" in text.lower():
```

## Mistake 04: Not stripping user input
```python
# WRONG — " hello " != "hello"
if user_input == "yes":

# CORRECT
if user_input.strip().lower() == "yes":
```

## Mistake 05: Concatenating with + instead of f-strings
```python
# HARD TO READ
msg = "Hello, " + name + "! You are " + str(age) + " years old."

# BETTER — f-string
msg = f"Hello, {name}! You are {age} years old."
```

## Mistake 06: Not using .join() for multiple concatenations
```python
# SLOW — creates new string each time
result = ""
for word in words:
    result += word + " "

# FAST — joins in one operation
result = " ".join(words)
```
