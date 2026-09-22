"""
LEVEL 04 PROJECT — SMS Spam Detector
========================================

Train a real spam classifier end-to-end on a tiny embedded
dataset. No files needed — data is in this file.

DATA: 16 SMS messages labeled spam=1 / ham=0 below.

BUILD:
  1. `train(messages, labels)` — TfidfVectorizer + LogisticRegression
     in a sklearn Pipeline; fit on all data; return the pipeline.
  2. `predict(pipeline, texts)` — return list of "spam"/"ham" strings.
  3. `evaluate(pipeline, messages, labels)` — print accuracy and
     show which messages were misclassified.

EXPECTED OUTPUT:
  ```
  Train accuracy: 1.00
  predict(["win money now", "see you at lunch"]) → ['spam', 'ham']
  ```

WHY A PIPELINE: vectorizer + model in one object — predict() takes
raw text. This is how production spam filters are structured.

BONUS THINKING: train accuracy 1.00 on 16 samples means nothing —
what would you do to estimate REAL accuracy? (Write your answer
in a comment.)
"""

MESSAGES = [
    ("WINNER! You won $1000 cash prize! Call now", 1),
    ("Claim your free reward today!!!", 1),
    ("Congratulations, you're selected for a prize", 1),
    ("FREE money, act now, limited offer", 1),
    ("You have won a lottery ticket, claim prize", 1),
    ("URGENT: your account won cash, click here", 1),
    ("Win big! Free entry to cash giveaway", 1),
    ("Prize alert! You've won! Text back NOW", 1),
    ("Hey, are we still on for lunch?", 0),
    ("Can you pick up milk on the way home?", 0),
    ("Meeting moved to 3pm tomorrow", 0),
    ("Happy birthday! Hope you have a great day", 0),
    ("Don't forget the dentist appointment", 0),
    ("Thanks for the notes from class", 0),
    ("Are you coming to the game tonight?", 0),
    ("I'll call you after work", 0),
]


def train(messages, labels):
    """Return a fitted sklearn Pipeline (Tfidf + LogisticRegression)."""
    # TODO
    pass


def predict(pipeline, texts):
    """Return ['spam'/'ham', ...] for each text."""
    # TODO
    pass


def evaluate(pipeline, messages, labels):
    """Print accuracy + misclassified messages."""
    # TODO
    pass


if __name__ == "__main__":
    texts = [m for m, _ in MESSAGES]
    y = [l for _, l in MESSAGES]
    pipe = train(texts, y)
    evaluate(pipe, texts, y)
    print(predict(pipe, ["win money now", "see you at lunch"]))
