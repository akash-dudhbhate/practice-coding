"""
LEVEL 15 — Transformers from Scratch
EASY P01 — Tokenize: Text to Token IDs
========================================

CONCEPT:
  Models can't read text — they only see numbers. A tokenizer
  chops text into pieces ("tokens") and maps each piece to an
  integer id using a fixed vocabulary (a word -> id dict).
  Real tokenizers (BPE, SentencePiece) learn sub-word pieces;
  here we use whole words so you can see the mechanics.

PROBLEM:
  Write `tokenize(text)` that:
    1. Lowercases the text and splits on whitespace
    2. Maps each word to its id in VOCAB
    3. Words not in VOCAB map to VOCAB["<unk>"] (id 0)
    4. Returns a list of ints

TRY THIS INPUT:
  ```python
  print(tokenize("the cat sat"))
  print(tokenize("a dog"))
  print(tokenize("the bird sat"))
  ```

EXPECTED OUTPUT:
  ```
  [1, 2, 3]
  [7, 6]
  [1, 0, 3]
  ```

HINT:
  List comprehension + dict.get(word, VOCAB["<unk>"])

CHECK: python3 check.py easy/p01
"""

# Given: tiny vocabulary (word -> token id)
VOCAB = {
    "<unk>": 0,
    "the": 1,
    "cat": 2,
    "sat": 3,
    "on": 4,
    "mat": 5,
    "dog": 6,
    "a": 7,
    "is": 8,
    "big": 9,
}

# === WRITE YOUR CODE BELOW ===

def tokenize(text):
    """text: string like "the cat sat" -> returns list of token ids."""
    # TODO: split text, look up each word in VOCAB, return id list
    pass


# === TEST ===
# print(tokenize("the cat sat"))
# print(tokenize("the bird sat"))
