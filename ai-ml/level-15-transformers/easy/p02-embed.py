"""
LEVEL 15 — Transformers from Scratch
EASY P02 — Embedding Lookup
========================================

CONCEPT:
  Token ids are arbitrary integers — id 2 ("cat") is not "twice"
  id 1 ("the"). To give tokens meaning, each id gets a learned
  vector: a row in an embedding matrix. Looking up embeddings is
  just fancy indexing: emb_matrix[token_ids].

  WHY: vectors let the model compute similarity (dot products)
  between tokens — that powers attention later.

PROBLEM:
  Write `embed(tokens, emb_matrix)` that:
    - INPUT: tokens = list/array of int ids, shape (seq_len,)
             emb_matrix = 2D array, shape (vocab_size, d_model)
    - OUTPUT: array shape (seq_len, d_model) — row i is the
              embedding of tokens[i]

TRY THIS INPUT:
  ```python
  import numpy as np
  emb = np.array([[0.0, 0.0, 0.0],
                  [1.0, 1.1, 1.2],
                  [2.0, 2.1, 2.2],
                  [3.0, 3.1, 3.2]])
  print(embed([1, 3], emb))
  ```

EXPECTED OUTPUT:
  ```
  [[1.  1.1 1.2]
   [3.  3.1 3.2]]
  ```

HINT:
  One line: emb_matrix[np.array(tokens)] — numpy fetches each
  row listed in the index array.

CHECK: python3 check.py easy/p02
"""

import numpy as np

# === WRITE YOUR CODE BELOW ===

def embed(tokens, emb_matrix):
    """tokens: list of int ids. emb_matrix: (vocab_size, d_model).
    Returns (seq_len, d_model)."""
    # TODO: fancy-index emb_matrix with the token ids
    pass


# === TEST ===
# emb = np.arange(12).reshape(4, 3).astype(float)
# print(embed([1, 3], emb))
