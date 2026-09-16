"""Level 18 — Agent Frameworks — Medium P03 Solution"""

class Graph:
    """Same runtime as medium/p01 — nodes, edges, conditional edges,
    first-added = entry, dead-end = terminal."""

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.conditionals = {}
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
                current = None
        return state


def _traced(name, work):
    """Wrap a state update so the node also logs itself to state['trace']."""
    def node(state):
        state = dict(state)
        state["trace"] = state.get("trace", []) + [name]
        return work(state)
    return node


def build_agent_graph():
    """input -> plan -> execute -> output"""
    g = Graph()

    def do_input(s):
        s["input"] = s["task"]
        return s

    def do_plan(s):
        s["plan"] = ["step1", "step2"]
        return s

    def do_execute(s):
        s["result"] = f"executed: {s['input']}"
        return s

    def do_output(s):
        s["output"] = s["result"]
        return s

    g.add_node("input",   _traced("input",   do_input))
    g.add_node("plan",    _traced("plan",    do_plan))
    g.add_node("execute", _traced("execute", do_execute))
    g.add_node("output",  _traced("output",  do_output))
    g.add_edge("input", "plan")
    g.add_edge("plan", "execute")
    g.add_edge("execute", "output")
    return g

if __name__ == "__main__":
    g = build_agent_graph()
    result = g.run({"task": "summarize notes"})
    print(result["trace"])
    print(result["output"])
