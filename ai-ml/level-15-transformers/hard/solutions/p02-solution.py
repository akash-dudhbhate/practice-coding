"""Level 15 — Transformers — Hard P02 Solution"""

import numpy as np


def next_token_probs(logits, temperature):
    """Turn raw logits into a probability distribution over the vocab.

    logits: (vocab_size,) raw model scores
    temperature: >0. <1 sharpens (confident), >1 flattens (creative)
    returns: (vocab_size,) probabilities summing to 1
    """
    z = np.asarray(logits, dtype=float) / temperature
    e = np.exp(z - np.max(z))
    return e / e.sum()


if __name__ == "__main__":
    logits = np.array([2.0, 1.0, 0.1, -1.0])
    print("T=1.0:", next_token_probs(logits, 1.0))   # [0.6381 0.2347 0.0954 0.0318]
    print("T=0.5:", next_token_probs(logits, 0.5))   # sharper
    print("T=2.0:", next_token_probs(logits, 2.0))   # flatter
