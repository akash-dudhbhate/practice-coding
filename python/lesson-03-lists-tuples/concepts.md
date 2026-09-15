# Lesson 03 — Concepts Explained (Lists & Tuples)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## List

**What:** A list is an ordered, mutable (changeable) collection of items. Items can be of any type, and a single list can mix types.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30]
mixed = [1, "hello", True, 3.14]

fruits[0]      # "apple"  (indexing starts at 0)
fruits[-1]     # "cherry" (negative index counts from the end)
fruits[1] = "blueberry"   # mutable — you can change an item
len(fruits)    # 3
```

**Why it exists:** You constantly need to group related values together — a shopping cart, a list of scores, the lines of a file. Without lists you'd need a separate variable for every item (`item1`, `item2`, ... `item1000`), which is unworkable.

**Where it's used:** Storing rows from a database, collecting user inputs, queues/stacks, holding results from a search, almost every program uses lists.

**What goes wrong without it:**
- You declare 100 variables for 100 items — impossible to loop over or pass to a function.
- You can't handle a variable number of items (you don't always know how many there will be at runtime).
- Code becomes long, repetitive, and bug-prone.

---

## Indexing & Slicing

**What:** Indexing accesses a single element by position. Slicing extracts a sub-list using `[start:stop:step]`.

```python
nums = [10, 20, 30, 40, 50]
nums[0]       # 10   (first element, index 0)
nums[2]       # 30
nums[-1]      # 50   (last element)
nums[1:4]     # [20, 30, 40]  (start inclusive, stop exclusive)
nums[:3]      # [10, 20, 30]  (from beginning)
nums[2:]      # [30, 40, 50]  (to end)
nums[::2]     # [10, 30, 50]  (every 2nd element)
nums[::-1]    # [50, 40, 30, 20, 10]  (reversed copy)
```

**Why it exists:** You often need one item (the first user, the last message) or a range (the top 10 scores, the first 5 rows). Indexing/slicing give a concise, consistent syntax for both.

**Where it's used:** Pagination (show items 10–20), getting the last element (`stack[-1]`), reversing, taking every Nth sample, trimming strings/lists.

**What goes wrong without it:**
- `IndexError: list index out of range` — accessing `nums[10]` on a 5-element list. Always check `len()` or use safe access.
- Off-by-one errors: forgetting indexing starts at 0, or that slice `stop` is exclusive.
- `nums[::-1]` returns a NEW list — it does NOT reverse `nums` in place. Confusing this with `.reverse()` causes silent bugs.

---

## append, insert, pop

**What:** These are the core list-mutation methods.

```python
stack = [1, 2, 3]
stack.append(4)        # [1, 2, 3, 4]  — add to end
stack.insert(0, 99)    # [99, 1, 2, 3, 4]  — insert at index 0
stack.pop()            # returns 4, list is now [99, 1, 2, 3]  — remove last
stack.pop(0)           # returns 99, list is now [1, 2, 3]  — remove at index
stack.remove(2)        # removes first occurrence of value 2 -> [1, 3]
```

- `append` adds one item to the end (O(1)).
- `insert` puts an item at a specific index (O(n) — shifts everything after it).
- `pop()` removes and returns the last item; `pop(i)` removes index `i`.

**Why it exists:** Collections are useless if you can't add or remove items. These three cover the most common needs: push onto a stack, insert in order, pull an item off.

**Where it's used:** Building up results in a loop (`result.append(x)`), implementing stacks/queues, removing processed items, inserting items in sorted order.

**What goes wrong without it:**
- Using `list = list + [x]` instead of `append` — creates a whole new list every iteration (slow, O(n²) in a loop).
- `insert(0, x)` in a loop is O(n) each time → O(n²) overall. For a queue, use `collections.deque` instead.
- `pop()` on an empty list raises `IndexError: pop from empty list`.
- `append([1,2])` adds the list as ONE element; `extend([1,2])` adds each element. Mixing these up gives nested lists you didn't want.

---

## sort & reverse

**What:** `sort()` sorts a list in place; `sorted()` returns a new sorted list. `reverse()` reverses in place; `reversed()` returns an iterator.

```python
nums = [3, 1, 4, 1, 5, 9]
nums.sort()            # [1, 1, 3, 4, 5, 9]  (in place, returns None)
sorted(nums)           # returns a new sorted list, nums unchanged
nums.sort(reverse=True)  # [9, 5, 4, 3, 1, 1]  (descending)

words = ["banana", "apple", "cherry"]
words.sort(key=len)    # sort by length -> ["apple", "banana", "cherry"]
words.sort(key=str.lower)  # case-insensitive sort

nums.reverse()         # reverses in place, returns None
list(reversed(nums))   # returns a new reversed list
```

**Why it exists:** Ordering data is fundamental — leaderboards, alphabetical lists, chronological events, sorting search results by relevance. `key=` lets you sort by any criterion without rewriting comparison logic.

**Where it's used:** Ranking, ordering records by date, sorting search results, preparing data for display or binary search.

**What goes wrong without it:**
- `nums.sort()` returns `None` — writing `x = nums.sort()` gives `x = None`. Use `x = sorted(nums)`.
- Sorting mixed types (`[3, "a", 1]`) raises `TypeError: '<' not supported between instances`.
- `sort()` is NOT stable-by-accident in older code — but Python's sort IS stable (equal items keep their order). Relying on stability is fine; not knowing it can confuse you.
- `reverse()` modifies in place; if you wanted a copy, use `nums[::-1]` or `list(reversed(nums))`.

---

## Tuple

**What:** A tuple is an ordered, IMMUTABLE (unchangeable) sequence. Once created, you can't add, remove, or change items.

```python
point = (3, 4)
rgb = (255, 128, 0)
single = (5,)        # note the comma — (5) is just the int 5
empty = ()

point[0]     # 3
point[1]     # 4
# point[0] = 10   -> TypeError: 'tuple' object does not support item assignment
len(point)   # 2
x, y = point  # unpacking: x=3, y=4
```

**Why it exists:** Some data should never change after creation — coordinates, RGB colors, a row from a database, function return values. Tuples signal "this is fixed" and are slightly faster and safer than lists. They're also hashable (can be dict keys / set members) when their contents are hashable.

**Where it's used:** Returning multiple values from a function (`return x, y`), fixed records (coordinates, dates), dictionary keys, `*args` parameters, swapping (`a, b = b, a`).

**What goes wrong without it:**
- Using a list where data must stay constant → a bug accidentally mutates it elsewhere, causing hard-to-trace errors.
- Trying to use a list as a dict key → `TypeError: unhashable type: 'list'`. Use a tuple instead.
- Forgetting the trailing comma: `(5)` is just `5`, not a 1-tuple. This causes subtle bugs when you expect a tuple.

---

## Immutability (List vs Tuple)

**What:** Mutability is whether an object can change after creation. Lists are mutable; tuples are immutable.

```python
lst = [1, 2, 3]
lst[0] = 99      # OK — list is mutable
lst.append(4)    # OK

tup = (1, 2, 3)
# tup[0] = 99    # TypeError — tuple is immutable
# tup.append(4)  # AttributeError — tuples have no append
```

**Why it exists:** Immutability gives guarantees. If something can't change, you can safely share it between functions, use it as a key, cache it, and reason about it without worrying another part of the code modified it. This prevents a whole class of bugs.

**Where it's used:** Configuration constants, dict keys, set members, function arguments that shouldn't be modified, concurrent code where shared state must be safe.

**What goes wrong without it:**
- Mutable default arguments: `def f(items=[]):` — the SAME list is shared across all calls. `items.append(x)` persists between calls, causing bizarre bugs. Use `None` and create a new list inside.
- Aliasing bugs: `a = [1,2,3]; b = a; b.append(4)` — `a` is now `[1,2,3,4]` too. Both names point to the same object. Tuples avoid this (can't mutate).
- Accidental modification: a function you pass a list to might change it. Passing a tuple guarantees it won't.

---

## List vs Tuple — When to Use Which

**What:** A practical decision guide.

```python
# Use a LIST when the collection will change:
shopping_cart = ["book", "pen"]
shopping_cart.append("notebook")
shopping_cart.remove("pen")

# Use a TUPLE when the collection is fixed:
coordinates = (34.05, -118.25)   # LA's lat/long won't change
def get_user(): return ("Akash", 25)   # fixed return shape
```

**Why it exists:** Choosing the right structure makes intent clear to other readers and prevents bugs. A tuple says "this won't change"; a list says "this may grow/shrink."

**Where it's used:** Heterogeneous fixed records → tuple (like a row). Homogeneous growing collections → list (like a queue).

**What goes wrong without it:**
- Using a list for fixed data invites accidental mutation.
- Using a tuple for data that needs to grow forces you to create a new tuple every time (slow and awkward).
- Picking wrong makes code harder to read — readers can't tell if the collection is meant to change.

---

## Unpacking

**What:** Unpacking assigns elements of a sequence to variables in one step.

```python
point = (3, 4, 5)
x, y, z = point       # x=3, y=4, z=5

first, *rest = [1, 2, 3, 4]   # first=1, rest=[2, 3, 4]
*init, last = [1, 2, 3, 4]    # init=[1, 2, 3], last=4

a, b = 10, 20
a, b = b, a           # swap! a=20, b=10
```

**Why it exists:** It's a clean way to pull values out of tuples/lists without indexing. Swapping two variables in one line is a classic use.

**Where it's used:** Multiple return values (`name, age = get_user()`), loop unpacking (`for key, value in items.items()`), swaps, ignoring values (`_, y = point`).

**What goes wrong without it:**
- `ValueError: too many values to unpack` — number of variables doesn't match number of items. Use `*rest` to capture extras.
- Forgetting `*` when you want the rest: `a, b = [1,2,3,4]` crashes; `a, *b = [1,2,3,4]` works.

---

## Iterating Over Lists

**What:** Looping through each element of a list.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:          # simple iteration
    print(fruit)

for i, fruit in enumerate(fruits):   # index + value
    print(i, fruit)
# 0 apple / 1 banana / 2 cherry
```

**Why it exists:** Processing every item in a collection is one of the most common programming tasks. Python's `for` loop iterates directly over elements (cleaner than C-style index loops).

**Where it's used:** Processing records, transforming data, printing, filtering, aggregating.

**What goes wrong without it:**
- Modifying a list while iterating over it: `for x in lst: lst.remove(x)` — skips items and behaves unpredictably. Iterate over a copy (`for x in lst[:]`) or build a new list.
- Using `range(len(lst))` when `enumerate` is clearer — works but is less Pythonic and error-prone.
