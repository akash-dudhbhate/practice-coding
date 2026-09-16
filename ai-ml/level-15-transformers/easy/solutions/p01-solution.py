"""Level 15 — Transformers — Easy P01 Solution"""

# Tiny vocabulary: word -> token id. "<unk>" catches unknown words.
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


def tokenize(text):
    return [VOCAB.get(word, VOCAB["<unk>"]) for word in text.lower().split()]


if __name__ == "__main__":
    print(tokenize("the cat sat"))      # [1, 2, 3]
    print(tokenize("a dog"))            # [7, 6]
    print(tokenize("the bird sat"))     # [1, 0, 3]  ("bird" -> <unk>)
