"""
LEVEL 15 — Transformers from Scratch
HARD P02 — Temperature Sampling
========================================

CONCEPT:
  A language model outputs LOGITS — one raw score per vocab word.
  Before sampling the next token we divide by a temperature T
  and softmax:

    p = softmax(logits / T)

    T = 1.0  ->  honest probabilities
    T < 1.0  ->  sharper: top token dominates (safe, repetitive)
    T > 1.0  ->  flatter: unlikely tokens get a shot (creative,
                 but can ramble)

  WHY it exists: pure argmax gives the same output every time;
  temperature is the dial between "boring but correct" and
  "surprising but risky". It's the 'temperature' knob in every
  LLM API.

PROBLEM:
  Write `next_token_probs(logits, temperature)`:
    - INPUT: logits (vocab_size,) floats; temperature > 0
    - OUTPUT: (vocab_size,) probabilities summing to 1
    - Stable softmax (subtract max AFTER dividing by temperature)

TRY THIS INPUT:
  ```python
  logits = np.array([2.0, 1.0, 0.1, -1.0])
  print("T=1.0:", next_token_probs(logits, 1.0))
  print("T=0.5:", next_token_probs(logits, 0.5))
  print("T=2.0:", next_token_probs(logits, 2.0))
  ```

EXPECTED OUTPUT:
  ```
  T=1.0: [0.6381 0.2347 0.0954 0.0318]
  T=0.5: [0.8619 0.1166 0.0193 0.0021]
  T=2.0: [0.4512 0.2737 0.1745 0.1007]
  ```

HINT:
  z = np.asarray(logits) / temperature; then stable softmax on z.

CHECK: python3 check.py hard/p02
"""

import numpy as np

# === WRITE YOUR CODE BELOW ===

def next_token_probs(logits, temperature):
    """logits: (vocab_size,) raw scores; temperature > 0.
    Returns probability array of the same shape."""
    # TODO: softmax(logits / temperature), numerically stable
    pass


# === TEST ===
# logits = np.array([2.0, 1.0, 0.1, -1.0])
# print(next_token_probs(logits, 1.0))
