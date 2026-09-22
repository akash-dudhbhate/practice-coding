"""
LEVEL 00A — What is AI?
EASY P01 — Rules vs Learning
============================

CONCEPT:
  Regular code: a human writes rules ("if X then Y").
  ML code: the program learns the rules from examples.

PROBLEM:
  See the difference yourself. Two functions below:
    - `spam_rules(text)` — hand-written rules (you write them)
    - `spam_learned(text)` — pretends to use learned patterns
       (we'll give you the logic — you just see it work)

  Write `spam_rules(text)` — return "spam" if the text contains
  any of these words: "free", "prize", "winner", "click now",
  "urgent". Otherwise return "ham". Case-insensitive.

TRY THIS INPUT:
  ```python
  print(spam_rules("FREE prize for you"))
  print(spam_rules("meet me at lunch"))
  ```

EXPECTED OUTPUT:
  ```
  spam
  ham
  ```

WHY THIS MATTERS:
  Your rules work — until a spammer writes "fr33" or "pr1ze".
  Then you patch your rules. ML doesn't need patching — it learns
  new patterns from new examples. That's the whole point.

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: implement spam_rules(text)


def spam_rules(text):
    """Return 'spam' or 'ham' using hand-written rules."""
    pass


def spam_learned(text):
    """Simulated 'learned' spam detector — uses patterns a model
    would discover, including leet-speak (fr33, pr1ze)."""
    learned_spam_patterns = ["free", "fr33", "prize", "pr1ze",
                             "winner", "click", "urgent", "money",
                             "cash", "offer", "deal", "buy now"]
    lower = text.lower()
    score = sum(1 for p in learned_spam_patterns if p in lower)
    return "spam" if score > 0 else "ham"


# === TEST ===
# print(spam_rules("FREE prize for you"))
# print(spam_rules("meet me at lunch"))
# print(spam_rules("You won fr33 money"))
