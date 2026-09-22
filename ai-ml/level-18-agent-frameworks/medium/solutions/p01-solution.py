"""Level 18 — Agent Frameworks — Medium P01 Solution"""

class Graph:
    """A node+edge runtime. Nodes are state->state functions; edges say
    who runs next. Conditional edges (a router function) take priority
    over plain edges. First node added is the entry point; a node with
    no outgoing edge is terminal."""

    def __init__(self):
        self.nodes = {}          # name -> fn(state) -> state
        self.edges = {}          # name -> next name (always)
        self.conditionals = {}   # name -> router fn(state) -> next name
        self.entry = None

    def add_node(self, name, fn):
        self.nodes[name] = fn
        if self.entry is None:
            self.entry = name
        return self

    def add_edge(self, frm, to):
        self.edges[frm] = to
        return self

    def add_conditional(self, frm, router_fn):
        self.conditionals[frm] = router_fn
        return self

    def run(self, state, max_steps=100):
        current = self.entry
        steps = 0
        while current is not None:
            state = self.nodes[current](state)
            steps += 1
            if steps > max_steps:
                raise RuntimeError(f"max_steps ({max_steps}) exceeded — cycle?")
            if current in self.conditionals:
                current = self.conditionals[current](state)
            elif current in self.edges:
                current = self.edges[current]
            else:
                current = None    # terminal node
        return state

if __name__ == "__main__":
    g = Graph()
    g.add_node("start", lambda s: {**s, "n": s["n"] + 1})
    g.add_node("big",   lambda s: {**s, "label": "big"})
    g.add_node("small", lambda s: {**s, "label": "small"})
    g.add_conditional("start", lambda s: "big" if s["n"] > 5 else "small")
    print(g.run({"n": 10}))
    print(g.run({"n": 1}))
