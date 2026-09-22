"""Level 15 — Transformers — Medium P02 Solution"""

import numpy as np


def positional_encode(seq_len, d_model):
    """Sin/cos positional encoding from 'Attention Is All You Need'.

    PE[pos, 2i]   = sin(pos / 10000^(2i/d_model))
    PE[pos, 2i+1] = cos(pos / 10000^(2i/d_model))
    returns: shape (seq_len, d_model)
    """
    pe = np.zeros((seq_len, d_model))
    pos = np.arange(seq_len)[:, None]          # (seq, 1)
    i = np.arange(d_model)[None, :]            # (1, d)
    # pair up dims: 0&1 share freq, 2&3 share freq, ...
    angle = pos / np.power(10000.0, (2 * (i // 2)) / d_model)
    pe[:, 0::2] = np.sin(angle[:, 0::2])
    pe[:, 1::2] = np.cos(angle[:, 1::2])
    return pe


if __name__ == "__main__":
    pe = positional_encode(4, 6)
    print("shape:", pe.shape)        # (4, 6)
    print("row 0:", pe[0])           # [0 1 0 1 0 1]
    print("row 1:", pe[1])           # [0.8415 0.5403 0.0464 0.9989 0.0022 1.]
