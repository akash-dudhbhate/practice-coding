"""Level 18 — Agent Frameworks — Easy P03 Solution"""

def linear_graph(nodes):
    """Chain nodes in order. Returns a state -> state function, so the
    pipeline itself can be used as a node inside a bigger graph."""
    def pipeline(state):
        for node in nodes:
            state = node(state)
        return state
    return pipeline

if __name__ == "__main__":
    add_one = lambda s: {**s, "x": s["x"] + 1}
    times_3 = lambda s: {**s, "x": s["x"] * 3}
    minus_2 = lambda s: {**s, "x": s["x"] - 2}

    pipe = linear_graph([add_one, times_3, minus_2])
    print(pipe({"x": 1}))          # {'x': 4}
    print(pipe({"x": 0}))          # {'x': 1}
