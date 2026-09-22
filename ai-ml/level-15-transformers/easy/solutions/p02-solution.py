"""Level 15 — Transformers — Easy P02 Solution"""

import numpy as np


def embed(tokens, emb_matrix):
    """Look up the embedding vector for each token id.

    tokens: list/array of int ids, shape (seq_len,)
    emb_matrix: shape (vocab_size, d_model)
    returns: shape (seq_len, d_model)
    """
    emb_matrix = np.asarray(emb_matrix)
    return emb_matrix[np.asarray(tokens)]


if __name__ == "__main__":
    emb = np.array([
        [0.0, 0.0, 0.0],   # id 0 = <unk>
        [1.0, 1.1, 1.2],   # id 1 = "the"
        [2.0, 2.1, 2.2],   # id 2 = "cat"
        [3.0, 3.1, 3.2],   # id 3 = "sat"
    ])
    print(embed([1, 3], emb))
    # [[1.  1.1 1.2]
    #  [3.  3.1 3.2]]
