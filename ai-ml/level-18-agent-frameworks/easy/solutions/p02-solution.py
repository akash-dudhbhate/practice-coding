"""Level 18 — Agent Frameworks — Easy P02 Solution"""

class Node:
    """A named wrapper around a state -> state function.

    The name lets the graph record which actions ran; __call__ makes
    the node itself usable anywhere a function is expected.
    """

    def __init__(self, name, fn):
        self.name = name
        self.fn = fn

    def run(self, state):
        return self.fn(state)

    def __call__(self, state):
        return self.run(state)

if __name__ == "__main__":
    n = Node("shout", lambda s: {**s, "text": s["text"].upper()})
    print(n.name)
    print(n.run({"text": "hi"}))
    print(n({"text": "go"}))
