"""
LEVEL 07 — Unsupervised Learning
HARD P03 — Topic Modeling (NMF)
========================================

CONCEPT:
  NMF (Non-negative Matrix Factorization) discovers "topics" in
  documents. Input: doc-term matrix → Output: each doc as a mix
  of topics, each topic as a mix of words.

  Steps: TfidfVectorizer → NMF(n_components) → top words per topic.

PROBLEM:
  Write `topics()` that:
    1. Documents: 4 texts about ML/AI vs cooking/food
    2. TfidfVectorizer(stop_words='english')
    3. NMF(n_components=2, random_state=42)
    4. For each topic, get top-5 words
    5. Returns (topic_words_list, doc_topic_matrix)

TRY THIS INPUT:
  ```python
  words, W = topics()
  print(words[0])       # e.g. ['python', 'machine', 'learning', ...]
  print(W.shape)        # (4, 2)
  ```

EXPECTED OUTPUT:
  ```
  Topic 0: ML/AI words (python, learning, model, data...)
  Topic 1: cooking words (recipe, food, kitchen...)
  (4, 2)
  ```

HINT:
  top_idx = nmf.components_[topic_i].argsort()[-5:][::-1]
  words = vectorizer.get_feature_names_out()

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# w, W = topics()
# print(w)
