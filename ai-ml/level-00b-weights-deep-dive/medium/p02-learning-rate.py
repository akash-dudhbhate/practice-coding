"""
LEVEL 00B — Weights & Training
MEDIUM P02 (Chapter 5) — Learning Rate
========================================

CONCEPT:
  step (the "learning rate") is how far each nudge goes.
  Too small → learns forever. Just right → converges fast.
  Too big → each step overcorrects and the numbers EXPLODE.

PROBLEM:
  Write simulate(x, truth, w, b, step, rounds) → list of w after
  each round (using the same update as medium/p01).
  Then watch three learning rates on (x=1000, truth=200, w=0.3, b=0):
    step=0.0000001 → watch w creep toward 0.2
    step=0.0000003 → converges faster
    step=0.001     → EXPLODES (weights go to ±huge)

TRY THIS INPUT:
  ```python
  ws = simulate(1000, 200, 0.3, 0.0, 0.0000001, 5)
  print([round(w, 4) for w in ws])
  ```

EXPECTED OUTPUT:
  ```
  [0.29, 0.281, 0.2729, 0.26561, 0.259049]
  ```
  (each round w moves toward 0.2 — but the steps SHRINK, because
   as the residual gets smaller the correction gets smaller.
   That's why it's called "descent" — you slow down near the bottom)

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement simulate(x, truth, w, b, step, rounds)


def simulate(x, truth, w, b, step, rounds):
    """Return list of w after each of `rounds` gradient steps."""
    pass


# === TEST ===
# ws = simulate(1000, 200, 0.3, 0.0, 0.0000001, 5)
# print([round(w, 4) for w in ws])
# ws = simulate(1000, 200, 0.3, 0.0, 0.001, 3)
# print(ws)   # watch it explode
