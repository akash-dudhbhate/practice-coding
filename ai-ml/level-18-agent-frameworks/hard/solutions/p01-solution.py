"""Level 18 — Agent Frameworks — Hard P01 Solution"""

def parallel_nodes(nodes_dict):
    """Fan-out/fan-in node factory.

    Each branch fn runs on a COPY of the input state (branches can't
    see each other's writes). Every branch's returned dict is merged
    into the output; per-branch outputs land under out["results"][name].
    """
    def parallel(state):
        merged = dict(state)
        results = {}
        for name, fn in nodes_dict.items():
            branch_out = fn(dict(state))      # isolated copy per branch
            results[name] = branch_out
            merged.update(branch_out)         # fan-in: later wins
        merged["results"] = results
        merged["trace"] = merged.get("trace", []) + ["parallel"]
        return merged
    return parallel

if __name__ == "__main__":
    p = parallel_nodes({
        "a": lambda s: {"x": s["n"] + 1},
        "b": lambda s: {"y": s["n"] * 10},
    })
    out = p({"n": 5})
    print(out["x"], out["y"])
    print(out["results"])
    print(out["trace"])
