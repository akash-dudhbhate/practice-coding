"""
LEVEL 15 — Transformers from Scratch
HARD P03 — Autoregressive Generation Loop
========================================

CONCEPT:
  This is how ChatGPT actually writes text: ONE TOKEN AT A TIME.

    tokens = seed
    repeat n times:
        logits = model_fn(tokens)     # scores for the NEXT token
        next_id = argmax(logits)      # greedy pick
        tokens.append(next_id)        # feed it back in

  Each new token becomes part of the input for the next step —
  "autoregressive" = the model consumes its own output. Real
  systems may sample instead of argmax, but the loop is identical.

PROBLEM:
  Write `generate(seed_tokens, model_fn, n)`:
    - seed_tokens: list of int ids (the prompt)
    - model_fn: callable(tokens) -> logits array (vocab_size,)
    - n: number of NEW tokens to generate
    - Greedy decode: append argmax(logits) each step
    - OUTPUT: full token list = seed + n generated ids

TRY THIS INPUT:
  ```python
  VOCAB_SIZE = 10
  def toy_model(tokens):
      # fake model: always predicts (last token + 1) % 10
      logits = np.zeros(VOCAB_SIZE)
      logits[(tokens[-1] + 1) % VOCAB_SIZE] = 5.0
      return logits
  print(generate([3], toy_model, 4))
  ```

EXPECTED OUTPUT:
  ```
  [3, 4, 5, 6, 7]
  ```

HINT:
  tokens = list(seed_tokens); loop n times; np.argmax picks the
  highest-logit id; append and repeat. Don't forget int() around
  the argmax.

CHECK: python3 check.py hard/p03
"""

import numpy as np

# === WRITE YOUR CODE BELOW ===

def generate(seed_tokens, model_fn, n):
    """Autoregressive greedy generation. Returns seed + n new ids."""
    # TODO: loop n times — call model_fn, argmax logits, append
    pass


# === TEST ===
# VOCAB_SIZE = 10
# def toy_model(tokens):
#     logits = np.zeros(VOCAB_SIZE)
#     logits[(tokens[-1] + 1) % VOCAB_SIZE] = 5.0
#     return logits
# print(generate([3], toy_model, 4))
