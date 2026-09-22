"""Solution — easy/p01-rules-vs-learning.py"""


def spam_rules(text):
    spam_words = ["free", "prize", "winner", "click now", "urgent"]
    lower = text.lower()
    return "spam" if any(w in lower for w in spam_words) else "ham"


def spam_learned(text):
    learned_spam_patterns = ["free", "fr33", "prize", "pr1ze",
                             "winner", "click", "urgent", "money",
                             "cash", "offer", "deal", "buy now"]
    lower = text.lower()
    score = sum(1 for p in learned_spam_patterns if p in lower)
    return "spam" if score > 0 else "ham"
