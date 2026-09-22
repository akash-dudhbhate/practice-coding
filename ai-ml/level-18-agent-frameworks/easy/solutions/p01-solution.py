"""Level 18 — Agent Frameworks — Easy P01 Solution"""

class State:
    """Dict-based state container that records every write in .history."""

    def __init__(self, initial=None):
        self.data = dict(initial) if initial else {}
        self.history = []          # list of (key, value) tuples, in write order

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.history.append((key, value))
        return self

if __name__ == "__main__":
    s = State({"task": "build a graph"})
    s.set("plan", ["step1", "step2"])
    s.set("step", 1)
    print(s.get("task"))
    print(s.get("missing", "nope"))
    print(s.history)
