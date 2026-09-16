"""Level 15 — Transformers — Hard P03 Solution"""

import numpy as np


def generate(seed_tokens, model_fn, n):
    """Autoregressive generation: feed tokens in, take the argmax next token,
    append it, repeat n times.

    seed_tokens: list of int token ids (the prompt)
    model_fn: callable(tokens) -> logits array of shape (vocab_size,)
    n: how many new tokens to generate
    returns: list of ids — seed tokens + n generated tokens
    """
    tokens = list(seed_tokens)
    for _ in range(n):
        logits = model_fn(tokens)
        next_id = int(np.argmax(logits))   # greedy decoding
        tokens.append(next_id)
    return tokens


if __name__ == "__main__":
    VOCAB_SIZE = 10

    def toy_model(tokens):
        """Fake 'model': always predicts (last token + 1) % VOCAB_SIZE."""
        logits = np.zeros(VOCAB_SIZE)
        logits[(tokens[-1] + 1) % VOCAB_SIZE] = 5.0
        return logits

    print(generate([3], toy_model, 4))   # [3, 4, 5, 6, 7]
