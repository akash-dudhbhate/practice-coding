"""
LEVEL 11 — LLM & Prompt Engineering
EASY P03 — Temperature Explained
========================================

CONCEPT:
  Temperature controls randomness:
    0.0 → deterministic, always same output
    0.5 → balanced, some variety but coherent
    1.0 → creative, more random
    1.5 → very creative, may lose coherence

  Like a dial: low = focused, high = creative.

PROBLEM:
  Write `explain_temperature(temp)` that returns a description
  string for a given temperature value.

  Rules:
    temp <= 0.2 → "Deterministic — same output every time"
    temp <= 0.7 → "Balanced — some variety but coherent"
    temp <= 1.2 → "Creative — more random, diverse outputs"
    temp > 1.2  → "Very creative — may be incoherent"

TRY THIS INPUT:
  ```python
  print(explain_temperature(0.0))
  print(explain_temperature(0.5))
  print(explain_temperature(1.0))
  print(explain_temperature(1.5))
  ```

EXPECTED OUTPUT:
  ```
  Deterministic — same output every time
  Balanced — some variety but coherent
  Creative — more random, diverse outputs
  Very creative — may be incoherent
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(explain_temperature(0.0))
