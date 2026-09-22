"""
LEVEL 00 — Setup & Math
MEDIUM P03 — Euclidean Distance
========================================

CONCEPT:
  Distance between two points = straight-line distance:

    dist = sqrt( (a₁-b₁)² + (a₂-b₂)² + ... )

  Example: [0,0] to [3,4] → sqrt(9 + 16) = sqrt(25) = 5.0

  Used in: KNN (nearest neighbors), K-Means (cluster centers),
  similarity search, RAG retrieval.

PROBLEM:
  Write `euclidean(a, b)` — distance between two equal-length lists.
  Pure Python (math.sqrt is fine).

TRY THIS INPUT:
  ```python
  print(euclidean([0,0], [3,4]))        # 5.0
  print(euclidean([1,1,1], [1,1,1]))    # 0.0
  ```

EXPECTED OUTPUT:
  ```
  5.0
  0.0
  ```

HINT:
  import math; math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(euclidean([0,0], [3,4]))
