"""Level 18 — Agent Frameworks — Hard P03 Solution"""

class Graph:
    """Node+edge runtime (same as medium/p01): first-added = entry,
    dead-end = terminal, conditional edges beat plain edges."""

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
    """Wrap a node so it logs its own name to state['trace']."""
    def node(state):
        state = dict(state)
        state["trace"] = state.get("trace", []) + [name]
        return work(state)
    return node


def _safe_math(expr):
    """Eval digits/operators only; anything else or a bad expr -> None."""
    if not expr or any(c not in "0123456789+-*/(). " for c in expr):
        return None
    try:
        return eval(expr, {"__builtins__": {}}, {})
    except Exception:
        return None


def full_agent(task):
    """parse -> plan -> tools -> verify -> respond, with a retry cycle:
    verify's conditional edge goes back to 'tools' when the result is
    unverified and attempts < 2, otherwise on to 'respond'."""

    def do_parse(s):
        t = s["task"].lower()
        if "calculate" in t or "compute" in t:
            word = "calculate" if "calculate" in t else "compute"
            s["kind"] = "math"
            s["expr"] = s["task"].lower().split(word, 1)[1].strip()
        elif "search" in t:
            s["kind"] = "search"
            s["query"] = s["task"].split(None, 1)[1] if " " in s["task"].strip() else ""
        else:
            s["kind"] = "unknown"
        return s

    def do_plan(s):
        s["plan"] = ["parse", "use " + s["kind"], "verify", "respond"]
        return s

    def do_tools(s):
        tools = {
            "math":   lambda: _safe_math(s.get("expr", "")),
            "search": lambda: f"Results for: {s.get('query', '')}",
        }
        fn = tools.get(s["kind"])
        s["tool_result"] = fn() if fn else None
        s["attempts"] = s.get("attempts", 0) + 1
        return s

    def do_verify(s):
        s["verified"] = s.get("tool_result") is not None
        return s

    def do_respond(s):
        if s["verified"]:
            s["response"] = f"Result: {s['tool_result']}"
        else:
            s["response"] = f"Failed after {s['attempts']} attempts"
        return s

    g = Graph()
    g.add_node("parse",   _traced("parse",   do_parse))
    g.add_node("plan",    _traced("plan",    do_plan))
    g.add_node("tools",   _traced("tools",   do_tools))
    g.add_node("verify",  _traced("verify",  do_verify))
    g.add_node("respond", _traced("respond", do_respond))
    g.add_edge("parse", "plan")
    g.add_edge("plan", "tools")
    g.add_edge("tools", "verify")
    # the cycle: retry tools once if unverified, else move on
    g.add_conditional(
        "verify",
        lambda s: "tools" if (not s["verified"] and s["attempts"] < 2) else "respond",
    )
    return g.run({"task": task})

if __name__ == "__main__":
    r = full_agent("calculate 6 * 7")
    print(r["response"]); print(r["verified"]); print(r["trace"])
    bad = full_agent("fly to the moon")
    print(bad["response"]); print(bad["attempts"]); print(bad["trace"])
