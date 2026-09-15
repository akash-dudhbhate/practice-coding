# Lesson 02 — Concepts Explained (Strings & String Methods)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## String Indexing

**What:** Each character in a string has a position number (index), starting from 0. You can access individual characters with `[index]`.

```python
text = "hello"
text[0]  -> 'h'    # first character (index 0)
text[1]  -> 'e'    # second character (index 1)
text[4]  -> 'o'    # fifth character (index 4)
text[-1] -> 'o'    # last character (negative = from end)
text[-2] -> 'l'    # second-to-last
```

**Why it exists:** Strings are sequences of characters. You often need to access specific characters — first letter, last letter, check individual characters. Indexing gives you direct access to any position.

**Where it's used:** Checking first/last characters, extracting specific positions, validating formats (e.g., does the email start with a letter?).

**What goes wrong without it:**
- You'd have to loop through the entire string every time you want one character — extremely inefficient.
- `text[5]` on "hello" (length 5, valid indices 0-4) → `IndexError: string index out of range`. Always check length first or use negative indexing.
- Confusing 0-based indexing: `text[1]` is the SECOND character, not the first. Beginners often off-by-one here.

---

## String Slicing

**What:** Slicing extracts a SUBSTRING using `[start:stop]` or `[start:stop:step]`. The `stop` index is EXCLUSIVE (not included).

```python
text = "hello world"
text[0:5]   -> "hello"     # indices 0,1,2,3,4 (5 is exclusive)
text[6:]    -> "world"     # from index 6 to end
text[:5]    -> "hello"     # from start to index 4
text[-5:]   -> "world"     # last 5 characters
text[::2]   -> "hlowrd"    # every 2nd character
text[::-1]  -> "dlrow olleh"  # reversed (step -1)
```

**Why it exists:** You constantly need parts of strings — first name from full name, domain from email, file extension from filename. Slicing is the cleanest way to extract substrings.

**Where it's used:** Parsing filenames, extracting substrings, data cleaning, text processing, URL parsing.

**What goes wrong without it:**
- You'd loop and build character by character — 10 lines instead of 1.
- Off-by-one: `text[0:5]` gives 5 characters (0,1,2,3,4), NOT 6. The stop index is exclusive.
- `text[::-1]` reverses a string — powerful but confusing if you don't understand step. Don't use it without understanding slicing first.
- Slicing never raises IndexError — `text[0:100]` on "hello" just returns "hello" (clamps to available range).

---

## String Immutability

**What:** Strings in Python are IMMUTABLE — you CANNOT change a character in place. Any string method returns a NEW string; it doesn't modify the original.

```python
text = "hello"
text[0] = "H"  # ERROR: TypeError — can't assign to string index
text.upper()   # returns "HELLO" but text is still "hello"
text = text.upper()  # NOW text is "HELLO" (reassigned, not modified)
```

**Why it exists:** Immutability makes strings safe to share — multiple variables can point to the same string without risk of one changing it. It also enables optimization (Python can reuse identical strings in memory).

**Where it's used:** Every time you call a string method — `.upper()`, `.lower()`, `.replace()`, `.strip()` — you must capture the result.

**What goes wrong without it:**
- `text.upper()` without assigning → text is unchanged → bug. You wrote the code, expected uppercase, got lowercase.
- Forgetting to reassign: `text.strip()` instead of `text = text.strip()` → leading/trailing spaces remain.
- Trying to modify in place → TypeError crash.

---

## .upper() / .lower() / .capitalize() / .title()

**What:** Methods that change the case of a string (return a NEW string):

```python
"hello".upper()       -> "HELLO"       # all uppercase
"HELLO".lower()       -> "hello"       # all lowercase
"hello world".capitalize() -> "Hello world"  # first char uppercase
"hello world".title() -> "Hello World"  # each word capitalized
"hello".swapcase()    -> "HELLO"       # swap upper<->lower
```

**Why it exists:** Text data comes in inconsistent cases — user input, database entries, file content. Case methods normalize text for comparison, display, and storage.

**Where it's used:** Case-insensitive comparison (`"Hello".lower() == "hello".lower()`), formatting user input, normalizing database entries, display formatting.

**What goes wrong without it:**
- Case-sensitive comparison: `"Hello" == "hello"` → `False`. Always normalize with `.lower()` before comparing.
- `.title()` has quirks: `"o'brien".title()` → `"O'Brien"` (correct), but `"don't".title()` → `"Don'T"` (wrong — apostrophe triggers capitalization). Use with caution.
- Forgetting immutability: `text.upper()` doesn't change `text`. Must assign: `text = text.upper()`.

---

## .strip() / .lstrip() / .rstrip()

**What:** Remove whitespace (or specified characters) from the ends of a string:

```python
"  hello  ".strip()   -> "hello"    # both ends
"  hello  ".lstrip()  -> "hello  "  # left only
"  hello  ".rstrip()  -> "  hello"  # right only
"??hello??".strip("?") -> "hello"   # strip specific chars
```

**Why it exists:** User input almost always has accidental whitespace — trailing spaces, leading spaces, newlines. `.strip()` cleans this up before processing. Without it, `"hello " == "hello"` is `False` (trailing space).

**Where it's used:** Processing user input, reading file lines (newlines), cleaning database data, form validation.

**What goes wrong without it:**
- User types "akash " (trailing space) → login fails because "akash " != "akash" in database.
- Reading file lines: `line` has `\n` at the end → `line.strip()` removes it. Without stripping, comparisons fail.
- `.strip("abc")` removes ANY of a, b, c from both ends — not the string "abc". `"abcHelloabc".strip("abc")` → `"Hello"`.

---

## .split() / .join()

**What:** `.split()` breaks a string into a list of substrings. `.join()` combines a list into a string.

```python
"hello world".split()        -> ["hello", "world"]    # split on whitespace
"a,b,c".split(",")          -> ["a", "b", "c"]       # split on comma
"hello".split("l")          -> ["he", "", "o"]       # split on 'l'
",".join(["a", "b", "c"])   -> "a,b,c"               # join with comma
" ".join(["hello", "world"]) -> "hello world"        # join with space
"".join(["h", "e", "l", "l", "o"]) -> "hello"        # join with nothing
```

**Why it exists:** Data often comes as delimited strings (CSV, URLs, paths). `.split()` parses them into usable lists. `.join()` is the reverse — building strings from lists. They're complementary.

**Where it's used:** CSV parsing, URL parsing, tokenizing sentences, building output strings, path manipulation.

**What goes wrong without it:**
- `.split()` with no argument splits on ANY whitespace and removes empty strings. `.split(" ")` splits on exactly one space and KEEPS empty strings. `"a  b".split()` → `["a", "b"]`, but `"a  b".split(" ")` → `["a", "", "b"]`.
- `.join()` is called on the SEPARATOR, not the list: `",".join(list)`, NOT `list.join(",")`. Beginners often get this backwards.
- Splitting on multi-char delimiters: `"abc".split("bc")` → `["a", ""]` — the delimiter is consumed, leaving an empty string.

---

## .replace()

**What:** Replace all occurrences of a substring with another:

```python
"hello world".replace("world", "Python") -> "hello Python"
"a-b-c".replace("-", "_") -> "a_b_c"
"hello".replace("l", "L") -> "heLLo"    # ALL occurrences
"hello".replace("l", "L", 1) -> "heLlo" # only first occurrence (count=1)
```

**Why it exists:** Text transformation is fundamental — fixing typos, normalizing data, removing unwanted characters, template filling.

**Where it's used:** Data cleaning, template substitution, sanitizing input, URL encoding, removing special characters.

**What goes wrong without it:**
- `.replace()` replaces ALL occurrences by default. If you only want the first, use the `count` parameter.
- Case-sensitive: `"Hello".replace("h", "x")` → `"Hello"` (no change — 'H' != 'h'). Use `.lower()` first if you need case-insensitive replacement.
- Returns a new string — doesn't modify the original. Forgetting to assign: `text.replace("a", "b")` without `text = ...` → no effect.

---

## .find() / .index()

**What:** Find the position of a substring within a string:

```python
"hello world".find("world")  -> 6     # position of "world"
"hello world".find("xyz")    -> -1    # not found returns -1
"hello world".index("world") -> 6     # same as find
"hello world".index("xyz")   # raises ValueError! not found
```

**Why it exists:** You often need to know WHERE something is in a string — find the @ in an email, find the dot in a filename, check if a substring exists.

**Where it's used:** Parsing, validation, extracting substrings, checking for substrings.

**What goes wrong without it:**
- `.index()` raises `ValueError` if not found → crashes your program. Use `.find()` (returns -1) if you're not sure the substring exists.
- `.find()` returns -1 (not False) — `if "hello".find("x"):` is `True` because -1 is truthy! Use `if "x" in "hello":` for existence checks instead.
- Returns the FIRST occurrence only. To find all, you need a loop with `start` parameter.

---

## f-strings (Formatted Strings)

**What:** f-strings let you embed variables and expressions directly into strings using `{}`:

```python
name = "Akash"
age = 25
f"Hello, {name}! You are {age} years old."  -> "Hello, Akash! You are 25 years old."
f"{2 + 3}"        -> "5"           # expressions work
f"{name.upper()}" -> "AKASH"       # method calls work
f"{age:>10}"      -> "        25"  # right-align, width 10
f"{age:0>5}"      -> "00025"       # zero-padded, width 5
f"{3.14159:.2f}"  -> "3.14"        # 2 decimal places
```

**Why it exists:** Before f-strings, Python used `.format()` or `%` formatting — verbose and error-prone. f-strings are readable, fast, and support expressions directly.

**Where it's used:** Everywhere you need to build strings with variables — logging, user messages, display formatting, report generation.

**What goes wrong without it:**
- Using `.format()`: `"Hello, {}".format(name)` — works but verbose and harder to read with multiple variables.
- Forgetting the `f` prefix: `"Hello, {name}"` → literal string "Hello, {name}" (no substitution).
- Mixing quotes: `f"Hello, {name}"` is fine, but `f"He said "hi" to {name}"` → syntax error. Use different quotes: `f"He said 'hi' to {name}"`.

---

## len()

**What:** Returns the number of characters in a string (or items in a list/dict):

```python
len("hello")    -> 5
len("")         -> 0
len("a b c")    -> 5    # spaces count as characters
```

**Why it exists:** You constantly need to know the length — validation (is the password at least 8 chars?), iteration bounds, display formatting, progress bars.

**Where it's used:** Input validation, loop bounds, display logic, data checks.

**What goes wrong without it:**
- `len()` counts ALL characters including spaces, newlines, and special characters. `len("a\nb")` → 3 (a, newline, b), not 2.
- Using `len` on `None`: `len(None)` → `TypeError`. Check for None first.
- Confusing length with last index: `len("hello")` is 5, but the last index is 4 (0-based). `text[len(text)]` → IndexError.

---

## in / not in (Substring Check)

**What:** Check if a substring exists within a string:

```python
"world" in "hello world"   -> True
"xyz" in "hello world"    -> False
"abc" not in "hello"      -> True
```

**Why it exists:** You often need to check if text contains something — does the email contain "@"? Does the message contain a keyword? `in` is the cleanest way to check.

**Where it's used:** Validation, search, filtering, keyword detection, spam checking.

**What goes wrong without it:**
- Case-sensitive: `"Hello" in "hello world"` → `False` ('H' != 'h'). Use `.lower()` first: `"hello" in "hello world".lower()`.
- `in` checks for substring, not word: `"cat" in "category"` → `True`. If you need word matching, split first and check the list.
- Using `.find()` for existence checks: `if text.find("x"):` → `-1` is truthy! Use `if "x" in text:` instead.

---

## .startswith() / .endswith()

**What:** Check if a string starts or ends with a specific substring:

```python
"hello world".startswith("hello") -> True
"hello world".endswith("world")   -> True
"hello".startswith("H")          -> False  # case-sensitive
"photo.jpg".endswith((".jpg", ".png")) -> True  # tuple of options
```

**Why it exists:** Checking prefixes/suffixes is extremely common — file extensions, URL protocols, name prefixes. These methods are clearer than slicing + comparison.

**Where it's used:** File type detection, URL validation, name filtering, data validation.

**What goes wrong without it:**
- Using slicing: `text[:5] == "hello"` works but is less readable than `text.startswith("hello")`.
- Case-sensitive: `"Hello".startswith("h")` → `False`. Use `.lower()` first if needed.
- `.endswith()` accepts a tuple: `filename.endswith((".jpg", ".png", ".gif"))` → checks all three. Very useful but not obvious.

---

## .count()

**What:** Count how many times a substring appears in a string:

```python
"hello".count("l")      -> 2
"hello world".count("o") -> 2
"hello".count("z")      -> 0
"aaa".count("aa")       -> 1  # non-overlapping!
```

**Why it exists:** Frequency counting is fundamental — how many vowels, how many spaces, how many errors, how many occurrences of a word.

**Where it's used:** Text analysis, validation, statistics, data processing.

**What goes wrong without it:**
- `.count()` counts NON-OVERLAPPING occurrences: `"aaa".count("aa")` → 1, not 2. The first "aa" is matched at index 0, then counting continues from index 2, where only "a" remains.
- Case-sensitive: `"Hello".count("h")` → 0. Use `.lower()` first.
- Empty string: `"hello".count("")` → 6 (length + 1). This is a Python quirk — don't count empty strings.

---

## String Concatenation (+ and +=)

**What:** Combine strings with `+` or `+=`:

```python
"hello" + " " + "world" -> "hello world"
text = "hello"
text += " world"        # text is now "hello world"
```

**Why it exists:** You often need to combine strings — building messages, constructing URLs, assembling output. `+` is the simplest way.

**Where it's used:** Building output strings, constructing messages, URL building.

**What goes wrong without it:**
- `+` only works with strings: `"hello" + 5` → `TypeError`. Convert first: `"hello" + str(5)`.
- Repeated `+` in a loop is O(n²) — each concatenation creates a new string, copying all previous content. For many concatenations, use `.join()` instead: `"".join(list_of_strings)` is O(n).
- Forgetting spaces: `"hello" + "world"` → `"helloworld"`. You need `"hello" + " " + "world"`.

---

## .isalpha() / .isdigit() / .isalnum() / .isspace()

**What:** Check what TYPE of characters a string contains:

```python
"hello".isalpha()   -> True   # only letters
"12345".isdigit()   -> True   # only digits
"hello123".isalnum() -> True  # letters or digits
"   ".isspace()     -> True   # only whitespace
"hello123".isalpha() -> False # has digits
```

**Why it exists:** Input validation — is the name only letters? Is the phone number only digits? Is the input empty/whitespace? These methods answer these questions in one call.

**Where it's used:** Form validation, data cleaning, input parsing, security (preventing injection).

**What goes wrong without it:**
- `.isalpha()` returns `False` for strings with spaces: `"hello world".isalpha()` → `False` (space is not a letter). Use `.replace(" ", "").isalpha()` if spaces are OK.
- Empty string: `"".isdigit()` → `False`. Check for empty first.
- Unicode: `.isalpha()` returns `True` for non-ASCII letters like "é" or "ñ". If you need ASCII only, check manually.

---

## Escape Characters

**What:** Special characters in strings, preceded by `\`:

```python
"hello\nworld"    # \n = newline
"hello\tworld"    # \t = tab
"hello\"world"    # \" = double quote (inside double-quoted string)
"hello\\world"    # \\ = literal backslash
r"hello\nworld"   # raw string — \n is literal, not newline
```

**Why it exists:** Some characters can't be typed directly in a string — newlines, tabs, quotes inside quoted strings. Escape sequences let you include them.

**Where it's used:** Formatting output (newlines, tabs), file paths on Windows (`C:\\Users\\...`), regex patterns (use raw strings).

**What goes wrong without it:**
- Windows paths: `"C:\new\folder"` → `\n` becomes a newline! Use raw string: `r"C:\new\folder"` or double backslash: `"C:\\new\\folder"`.
- Forgetting to escape quotes: `"He said "hi""` → syntax error. Use `"He said \"hi\""` or `'He said "hi"'`.
- Regex: `\d`, `\w`, `\s` are regex patterns. Without raw strings, `\d` is just `d` (Python doesn't recognize `\d` as an escape, but it may in future versions). Always use `r"pattern"` for regex.
