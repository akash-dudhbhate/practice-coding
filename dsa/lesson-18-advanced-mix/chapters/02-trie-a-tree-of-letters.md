# 02 — A Trie: a Tree Made of Letters

> 4-minute read. One new data structure.

## The idea, plain words

Think about your phone's **autocomplete**. You type `ca` and it offers
"cat", "car", "cataract". How does it find *every word starting with
ca* that fast — from a dictionary of millions?

A **trie** (from "re**trie**val", pronounced "try") is a tree where
every edge is a letter. Walk down from the root spelling your prefix —
the node you land on knows everything sharing that prefix, because
**shared letters are stored once**.

```
words: cat, car, bad        (* = "a full word ends here")

        root
       /    \
      c      b
      |      |
      a      a
     / \     |
    t*  r*   d*
```

"cat" and "car" share the `c→a` path — stored once, then they fork.
"bad" lives on its own branch.

## Watch an insert — "cat", then "car"

```
insert("cat"):  root → c (new) → a (new) → t (new, mark *)
insert("car"):  root → c (exists, reuse) → a (exists, reuse)
                → r (new, mark *)
```

The second insert walks the shared `c→a` part for free and only builds
the new `r` edge. That's the whole trick.

## In Python — a node is just a dict

Each node = a `{letter: child}` dictionary, plus one flag (next
chapter). Watch the structure build itself:

```python
root = {}
for word in ["cat", "car", "bad"]:
    node = root
    for c in word:
        node = node.setdefault(c, {})   # reuse or create the child
    node["*"] = True                    # "a word ends here"
print(root)
```

```
{'c': {'a': {'t': {'*': True}, 'r': {'*': True}}},
 'b': {'a': {'d': {'*': True}}}}
```

Compare with the diagram — same tree, written as nested dicts.

## Why it exists

A `set` of words answers "is this *exact word* present?" in O(word
length). But it cannot answer "is this *prefix* present?" or "list every
word starting with 'app'" without scanning everything.

A trie walks prefix questions letter by letter: `startsWith("app")`
costs 3 hops whether the dictionary holds 10 words or 10 million. The
size of the dictionary stops mattering.

## Where it's used

Autocomplete/typeahead, spell-checkers, IP routing tables (longest
prefix wins), word-search puzzles — anywhere "is this path still a
prefix of *some* word?" must be answered in O(1) per step.

## Common mistake

Thinking a trie saves time on *exact-match* lookups — it doesn't beat a
hash set there. Its superpower is **prefix** questions only. Wrong tool
for "is this word in the set?"

## Your turn

Draw (or mentally picture) the trie after inserting `"do"`, `"dog"`,
`"dot"`. How many letter-edges branch off the `o` node?

<details><summary>Answer</summary>
Two edges: `o → g*` and `o → t*`. All three words share `root→d→o`;
`"do"` itself marks `o` as an end-of-word node (the `*` matters — next
chapter). Root gets exactly one child (`d`), `o` gets two (`g`, `t`).
</details>

---

**Next →** [03 — Coding a trie: the `is_end` flag](03-trie-code-is-end.md)
