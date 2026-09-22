"""
LEVEL 15 PROJECT — Mini-GPT: Text Generation from Scratch
==========================================================

Assemble every piece from this level into a working (tiny)
text generator — the same architecture as GPT, ~100x smaller.

ARCHITECTURE:
  text -> tokenize -> embed -> + positional_encode
       -> transformer_block -> last row @ W_out -> logits
       -> argmax -> append -> repeat  (autoregressive)

BUILD:
  1. VOCAB is given (12 words). Implement:
     - tokenize(text)        (easy/p01)
     - softmax_row(scores)   (easy/p03)
     - positional_encode(n,d)(medium/p02)
     - attention(Q,K,V)      (medium/p01)
     - layernorm(x)          (hard/p01 helper)
     - transformer_block(X,p)(hard/p01)
  2. build_model(): np.random.seed(42), then create weights IN
     THIS ORDER (seed makes it reproducible):
        E    = randn(12, 8)  * 0.1     # embedding matrix
        W_q  = randn(8, 8)   * 0.1
        W_k  = randn(8, 8)   * 0.1
        W_v  = randn(8, 8)   * 0.1
        W1   = randn(8, 16)  * 0.1 ;  b1 = zeros(16)
        W2   = randn(16, 8)  * 0.1 ;  b2 = zeros(8)
        W_out= randn(8, 12)  * 0.1     # to logits over vocab
  3. model_fn(tokens, model):
        ids -> E[ids] + positional_encode(len(ids), 8)
            -> transformer_block -> out[-1] @ W_out -> logits(12,)
  4. generate_text(seed_text, model, n):
        tokenize the seed, then n times:
          logits = model_fn(tokens); append argmax(logits)
        decode ids back to words with ID2WORD, join with " "

TEST RUN:
  ```python
  model = build_model()
  print(generate_text("the cat", model, 4))
  print(generate_text("a dog", model, 3))
  ```

EXPECTED OUTPUT:
  ```
  the cat is is is dog
  a dog is is is
  ```

  (Random weights → gibberish-ish output is CORRECT here. The
  point is the pipeline works end to end. A trained model would
  produce real sentences — same code, learned weights.)

STRETCH:
  - Sample from next_token_probs(logits, 0.8) instead of argmax
    (np.random.choice) for varied output.
  - Add a second transformer_block and watch output change.
"""

import numpy as np

# --- given ---
VOCAB = {"<unk>": 0, "the": 1, "cat": 2, "dog": 3, "sat": 4,
         "ran": 5, "on": 6, "mat": 7, "a": 8, "big": 9,
         "is": 10, ".": 11}
ID2WORD = {i: w for w, i in VOCAB.items()}
D_MODEL = 8
D_FF = 16


# === WRITE YOUR CODE BELOW ===
# Copy/adapt your solutions from the problems above.

def tokenize(text):
    # TODO: easy/p01
    pass


def softmax_row(scores):
    # TODO: easy/p03
    pass


def positional_encode(seq_len, d_model):
    # TODO: medium/p02
    pass


def attention(Q, K, V):
    # TODO: medium/p01
    pass


def layernorm(x, eps=1e-6):
    # TODO: hard/p01 helper
    pass


def transformer_block(X, params):
    # TODO: hard/p01
    pass


def build_model():
    # TODO: seed(42); create E, W_q, W_k, W_v, W1, b1, W2, b2, W_out
    pass


def model_fn(tokens, model):
    # TODO: ids -> E[ids] + PE -> transformer_block -> last row @ W_out
    pass


def generate_text(seed_text, model, n):
    # TODO: tokenize, loop n times (argmax + append), decode to words
    pass


if __name__ == "__main__":
    model = build_model()
    print(generate_text("the cat", model, 4))   # the cat is is is dog
    print(generate_text("a dog", model, 3))     # a dog is is is
