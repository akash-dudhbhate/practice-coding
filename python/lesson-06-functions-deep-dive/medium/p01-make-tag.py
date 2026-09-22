"""
LESSON 06 — Functions Deep Dive
MEDIUM P01 — Make HTML Tag
============================================

CONCEPT:
  `**kwargs` collects any number of keyword arguments into a dict.
  Loop over `attrs.items()` to build the attribute part of the tag.

PROBLEM:
  Write a function `make_tag(tag, text, **attrs)` that returns an
  HTML string like `<tag k="v" ...>text</tag>`. With no attributes,
  return `<tag>text</tag>`.

TRY THIS INPUT:
  ```python
  print(make_tag("a", "link", href="x.com"))
  print(make_tag("p", "hi"))
  ```

EXPECTED OUTPUT:
  ```
  <a href="x.com">link</a>
  <p>hi</p>
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
