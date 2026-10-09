# 03 — Coding a Trie: the `is_end` Flag

> 5-minute read. The one flag that makes it correct.

## The idea, plain words

Here's the sneaky question: after inserting only `"apple"`, is `"app"`
in your trie?

**No** — and also **yes**, depending what you mean. The path `a→p→p`
*exists* (it's a real prefix), but no word *ends* there. A trie must
tell these apart, and one boolean per node does it:

- `search(word)` → path exists **AND** `is_end` is True
- `startsWith(prefix)` → path exists (ignore `is_end`)

That distinction **is** the data structure.

## The full class (~20 lines)

```python
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False              # "a full word ends HERE"

    def insert(self, word):
        node = self
        for c in word:
            node = node.children.setdefault(c, Trie())
        node.is_end = True               # flag the LAST node only

    def _walk(self, s):                  # node at end of path, or None
        node = self
        for c in s:
            if c not in node.children:
                return None              # path dies → False
            node = node.children[c]
        return node

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.is_end

    def startsWith(self, prefix):
        return self._walk(prefix) is not None

t = Trie()
t.insert("apple")
print(t.search("apple"))      # True
print(t.search("app"))        # False — path exists but no word ends there
print(t.startsWith("app"))    # True  — it IS a prefix
```

## Hand-trace — insert "apple", then three queries

What that code just did, step by step:

```
insert("apple"): root→a→p→p→l→e, mark e.is_end=True

search("apple"):    walk a→p→p→l→e → node found, is_end=True  → True
search("app"):      walk a→p→p     → node found, is_end=False → False
startsWith("app"):  walk a→p→p     → node found               → True
```

## Why it exists

One private `_walk` answers both questions; the only difference is
whether `is_end` gets checked. Without the flag you could never
represent `"app"` and `"apple"` living on the same path.

## Where it's used

The killer app: **word-search-with-a-dictionary** (`hard/p01`). Plain
DFS×each-word re-walks the same prefixes thousands of times. With a
trie, the moment a grid path isn't a prefix of *any* word, the DFS dies
— that's the pruning that turns TLE into accepted. (One trap there:
mark a board cell visited, recurse, then **put the letter back** so
other paths can use it.)

## Common mistake

Confusing `is_end` with "has children" or "path exists." After inserting
`"apple"` only, `search("app")` **must** be False — if yours returns
True, you're checking path-existence, not word-end. Also: use a `dict`
of children, not a fixed 26-slot array — it's general and nearly as
fast.

## Your turn

After `insert("apple")` and `insert("app")`, what does `search("app")`
return — and which node changed to make it so?

<details><summary>Answer</summary>
**True.** The second insert walks the *existing* `a→p→p` path and flips
`is_end` to True on the second `p` node. No new nodes are created — the
words fully share their path now.
</details>

---

**← Prev** [02 — A trie: a tree made of letters](02-trie-a-tree-of-letters.md) ·
**Next →** [04 — What a bit actually is](04-what-is-a-bit.md)
